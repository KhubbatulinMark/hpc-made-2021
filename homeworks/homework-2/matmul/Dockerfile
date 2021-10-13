FROM ubuntu:20.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt update && apt install -y \
                     libblas-dev \
                     build-essential \
                     libboost-dev \
                     libboost-program-options-dev \
                     libgtest-dev \
                     cmake

WORKDIR /app
COPY . .