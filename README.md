Fork Notes
============
Exploring the idea that you just write the raw bytes to stdout and then ffmpeg(video)/magick(images) writes them to a file. This way you don't need to set up the piping nonsense, you can do it just with shell scripts. This way it is portable accross programming languages.

TODO: explore the idea of streaming video via ffmpeg realtime. Don't need to wait for the last frame before starting watching the video.


ffmpeg sample
=============
This in example of writing raw frames to ffmpeg to generate video. It
is the sample code for my post
[Using ffmpeg for Advent of Code visualisation](https://sjmulder.nl/2022/aoc-ffmpeg.html).

Legal
-----
By Sijmen J. Mulder (ik@sjmulder.nl). I, the copyright holder of this
work, hereby release it into the public domain. This applies worldwide.

In case this is not legally possible: I grant anyone the right to use
this work for any purpose, without any conditions, unless such
conditions are required by law.
