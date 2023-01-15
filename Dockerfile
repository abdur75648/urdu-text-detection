FROM nvidia/cuda:12.0.0-devel-ubuntu20.04
USER root
RUN ln -sf /usr/share/zoneinfo/Asia/Kolkata /etc/localtime
RUN apt-get update -y && apt-get upgrade -y
RUN apt-get install -y apt-utils git curl ca-certificates bzip2 cmake tree htop bmon iotop g++
RUN apt-get install -y ffmpeg libglib2.0-0 libsm6 libxext6 libxrender-dev
RUN apt-get install -y python3-pip && pip3 install --upgrade pip
RUN pip install pandas ninja yacs cython matplotlib tqdm opencv-python networkx shapely pycocotools scipy
RUN pip install torch==1.10.1 torchvision==0.11.2 torchaudio==0.10.1
RUN pip install numpy==1.22.0