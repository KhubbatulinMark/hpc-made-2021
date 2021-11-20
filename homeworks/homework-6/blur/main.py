import os
import sys
import math
from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter, FileType, ArgumentTypeError

import numpy as np
from PIL import Image
import pycuda.autoinit
import pycuda.driver as drv
import pycuda.compiler as compiler


def load_image(filepath):
    img = np.array(Image.open(filepath))
    return img


def split_img(img):
    red_channel = img[:, :, 0].copy()
    green_channel = img[:, :, 1].copy()
    blue_channel = img[:, :, 2].copy()
    return red_channel, green_channel, blue_channel


def gaussian_blur_callback(arguments):
    """Callback for gaussian blur"""
    return gaussian_blur(arguments.image_filepath, arguments.output_filepath, arguments.size)


def gaussian_blur(image_filepath, output_filepath, kernel_size):
    os.makedirs('result', exist_ok=True)
    img = load_image(image_filepath)

    sigma = 2
    kernel_size = int(kernel_size)
    kernel_matrix = np.empty((kernel_size, kernel_size), np.float32)
    kernel_half_width = kernel_size // 2
    for i in range(-kernel_half_width, kernel_half_width + 1):
        for j in range(-kernel_half_width, kernel_half_width + 1):
            kernel_matrix[i + kernel_half_width][j + kernel_half_width] = (
                    np.exp(-(i ** 2 + j ** 2) / (2 * sigma ** 2))
                    / (2 * np.pi * sigma ** 2)
            )
    gaussian_kernel = kernel_matrix / kernel_matrix.sum()

    height, width = img.shape[:2]
    dim_block = 32
    dim_grid_x = math.ceil(width / dim_block)
    dim_grid_y = math.ceil(height / dim_block)

    mod = compiler.SourceModule(open('gaussian-blur.cu').read())
    apply_filter = mod.get_function('applyFilter')

    r, g, b = split_img(img)

    for channel in (r, g, b):
        apply_filter(
            drv.In(channel),
            drv.Out(channel),
            np.uint32(width),
            np.uint32(height),
            drv.In(gaussian_kernel),
            np.uint32(kernel_size),
            block=(dim_block, dim_block, 1),
            grid=(dim_grid_x, dim_grid_y)
        )

    output_array = np.empty_like(img)
    output_array[:, :, 0] = r
    output_array[:, :, 1] = g
    output_array[:, :, 2] = b

    Image.fromarray(output_array).save(os.path.join('result', output_filepath))


def setup_parser(parser):
    """Function for setup the parser"""
    sub_parsers = parser.add_subparsers(help="choose command")

    gaussian_blur_parse = sub_parsers.add_parser(
        "gaussian",
        help="Gaussian Blur image",
        formatter_class=ArgumentDefaultsHelpFormatter,
    )
    gaussian_blur_parse.add_argument(
        "-i", "--input", dest="image_filepath",
        help="Path to image for loading",
        metavar='IMAGE'
    )
    gaussian_blur_parse.add_argument(
        "-o", "--output", dest="output_filepath",
        help="Path to store blurred image",
        metavar='OUTPUT'
    )
    gaussian_blur_parse.add_argument(
        "-s", "--size", dest="size",
        help="Kernel Size",
        metavar='SIZE',
    )
    gaussian_blur_parse.set_defaults(callback=gaussian_blur_callback)


def main():
    """Main function of the module"""
    parser = ArgumentParser(
        prog="blur",
        description="Make difference blur",
        formatter_class=ArgumentDefaultsHelpFormatter,
    )
    setup_parser(parser)
    arguments = parser.parse_args()
    arguments.callback(arguments)


if __name__ == "__main__":
    main()
