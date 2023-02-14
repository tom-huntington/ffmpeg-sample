#!/bin/sh

rm output.mp4
python3.11 sample.py | ffmpeg -loglevel warning -stats -f rawvideo -pixel_format rgb24 -video_size 1280x720 -framerate 30 -i - -pix_fmt yuv420p output.png

