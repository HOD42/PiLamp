#!/usr/bin/env python

import sys
import time
from colorsys import hsv_to_rgb

from mote import Mote

def usage():
    print("Usage: {} <r> <g> <b>".format(sys.argv[0]))
    sys.exit(1)

if len(sys.argv) != 4:
    usage()

# Exit if non integer value. int() will raise a ValueError
try:
    r1, g1, b1 = [int(x) for x in sys.argv[1:]]
except ValueError:
    usage()

# Exit if any of r, g, b are greater than 255
if max(r1,g1,b1) > 255:
    usage()

print("Setting Mote to {r},{g},{b}".format(r=r1,g=g1,b=b1))


mote = Mote()

mote.configure_channel(1, 16, False)
mote.configure_channel(2, 16, False)
mote.configure_channel(3, 16, False)
mote.configure_channel(4, 16, False)

try:
    while True:
        #h = time.time() * 50
        h = time.time() * 5
        for pixel in range(16):
            for channel in range(4):
                #hue = (h + (channel * 4) + (pixel * 16)) % 360
                #hue = (h + (channel / 64) + (pixel * 8)) % 360
                hue = (h + (channel / 128) + (pixel * 8)) % 360
                #hue = (h + (channel / 30) + (pixel * 8)) % 360
                #r, g, b = [int(c * r1) for c in hsv_to_rgb(hue/360.0, 1.0, 1.0)]
                r, g, b = [int(c * r1) for c in hsv_to_rgb(hue/360.0, 1.0, 1.0)]
                mote.set_pixel(channel + 1, pixel, r, g, b)
        mote.show()
        time.sleep(0.01)

except KeyboardInterrupt:
    mote.clear()
    mote.show()
