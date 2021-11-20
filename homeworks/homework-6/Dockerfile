FROM nvcr.io/nvidia/pytorch:21.05-py3
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install build-essential ffmpeg libsm6 \
        libsndfile1 libxext6 -y

COPY requirements.txt .
RUN python -m pip install --upgrade pip

RUN --mount=type=cache,target=/root/.cache pip install -r requirements.txt

WORKDIR /opt/app