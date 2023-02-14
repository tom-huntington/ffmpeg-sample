#!/bin/sh

rm out.png
python3.11 sample.py | magick.exe convert -depth 8 -size 1280x720+0 rgb:- out.png
wslview out.png

