#!/usr/bin/env python
import sys
import time
from colorsys import hsv_to_rgb
from mote import Mote
def usage():
    print("Usage: {} <br>".format(sys.argv[0]))
    sys.exit(1)
if len(sys.argv) != 2:
    usage()
# Exit if non integer value. int() will raise a ValueError
try:
    br = int(sys.argv[1])
except ValueError:
    usage()
# Exit if greater than 255
if br > 255:
    usage()
print("Brightness=",br)
mote = Mote()
mote.configure_channel(1, 16, False)
mote.configure_channel(2, 16, False)
mote.configure_channel(3, 16, False)
mote.configure_channel(4, 16, False)
try:
    while True:
        h = time.time() * 30
        for channel in range(4):
            if channel%2 == 0:
                for pixel in range(16):
                    hue = (h + (channel * 5760) + (pixel * 4)) % 360
                    r, g, b = [int(c * br) for c in hsv_to_rgb(hue/360.0, 1.0, 1.0)]
                    mote.set_pixel(channel + 1, pixel, r, g, b)
            else:
                for pixel in range(16):
                    hue = (h - (channel * 5760) - (pixel * 4)) % 360
                    r, g, b = [int(c * br) for c in hsv_to_rgb(hue/360.0, 1.0, 1.0)]
                    mote.set_pixel(channel + 1, pixel, r, g, b)
        mote.show()
        time.sleep(0.04)
        #time.sleep(1)
except KeyboardInterrupt:
    mote.clear()
    mote.show()
