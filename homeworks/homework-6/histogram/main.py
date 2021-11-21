import os
import sys
import math
from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter, FileType, ArgumentTypeError

import numpy as np
import cv2
from PIL import Image
import pycuda.autoinit
import pycuda.driver as cuda
import pycuda.driver as drv
import pycuda.compiler as compiler

import matplotlib.pyplot as plt


def load_image(filepath):
    img = np.array(Image.open(filepath))
    return img


def split_img(img):
    red_channel = img[:, :, 0].copy().astype(np.int32)
    green_channel = img[:, :, 1].copy().astype(np.int32)
    blue_channel = img[:, :, 2].copy().astype(np.int32)
    return red_channel, green_channel, blue_channel


def save_channel(img, filepath, color_map):
    plt.figure(figsize=(16, 8))
    plt.imshow(img, cmap=color_map)
    plt.axis('off')
    plt.savefig(filepath, aspect='auto', bbox_inches='tight')
    plt.close()


def plot_histogram_callback(arguments):
    """Callback for gaussian blur"""
    return histogram(arguments.image_filepath, arguments.output_directory)


def histogram(image_filepath, output_dir):

    os.makedirs(output_dir, exist_ok=True)

    histogramModule = compiler.SourceModule(open('histogram.cu').read())
    histogram = histogramModule.get_function('histogram')

    bin_count = 256

    bins = np.linspace(0, 256, bin_count + 1, dtype=np.int32)
    cuda_bins = cuda.mem_alloc(bins.nbytes)
    cuda.memcpy_htod(cuda_bins, bins)

    hist = np.zeros(bin_count, dtype=np.int32)
    cuda_hist = cuda.mem_alloc(hist.nbytes)
    cuda.memcpy_htod(cuda_hist, hist)

    img = load_image(image_filepath)
    r, g, b = split_img(img)

    for channel, name, color_map in zip([r, g, b], ['red', 'green', 'blue'], ['Reds', 'Greens', 'Blues']):

        img_path = os.path.join('result', name + '_channel.jpeg')
        save_channel(channel, img_path, color_map)

        cuda_channel = cuda.mem_alloc(channel.nbytes)
        cuda.memcpy_htod(cuda_channel, channel)

        height, width = channel.shape[:2]
        block_size = 32
        block = (block_size, block_size, 1)
        grid = ((width + block_size - 1) // block[0], (height + block_size - 1) // block[1])

        histogram(
            np.int32(bin_count),
            cuda_bins,
            np.int32(channel.shape[0]),
            np.int32(channel.shape[1]),
            cuda_channel,
            cuda_hist,
            block=block,
            grid=grid
        )
        cuda.memcpy_dtoh(hist, cuda_hist)

        plt.figure(figsize=(16, 9))
        plt.plot(bins[:-1], hist, c=name)
        plt.fill_between(bins[:-1], hist, color=name)
        histogram_filepath = os.path.join('result', name + '_histogram.jpeg')
        plt.savefig(histogram_filepath, aspect='auto', bbox_inches='tight')
        

def setup_parser(parser):
    """Function for setup the parser"""
    sub_parsers = parser.add_subparsers(help="choose command")

    histogram_parse = sub_parsers.add_parser(
        "histogram",
        help="Plot histogram",
        formatter_class=ArgumentDefaultsHelpFormatter,
    )
    histogram_parse.add_argument(
        "-i", "--input", dest="image_filepath",
        help="Path to image for loading",
        metavar='IMAGE'
    )
    histogram_parse.add_argument(
        "-o", "--output", dest="output_directory",
        help="Path to store outputs",
        metavar='OUTPUT'
    )
    histogram_parse.set_defaults(callback=plot_histogram_callback)


def main():
    """Main function of the module"""
    parser = ArgumentParser(
        prog="histogram",
        description="Plot histogram",
        formatter_class=ArgumentDefaultsHelpFormatter,
    )
    setup_parser(parser)
    arguments = parser.parse_args()
    arguments.callback(arguments)


if __name__ == "__main__":
    main()
