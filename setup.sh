#!/bin/bash

# Update and install necessary packages
apt install ffmpeg -y
apt update -y
apt upgrade -y

python -m pip install --upgrade pip
pip install yt-dlp ffmpeg srt openai-whisper setuptools-rust moviepy ultralytics torch opencv-python filterpy

# Run the main Python script
python main.py
