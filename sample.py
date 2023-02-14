import sys
frame = bytearray(1280*720*3);
def write_frame(y, x, t, val):
    index = y * 1280 * 3 + x * 3 + t
    frame[index] = val

for t in range(300):
    frame = bytearray(1280*720*3);

    for y in range(50, 150):
        for x in range(30, 200):
            write_frame(y+t, x+t, 0, 255);
            write_frame(y+t, x+t, 1, 255);
            write_frame(y+t, x+t, 2, 0);

    sys.stdout.buffer.write(frame)
    break
