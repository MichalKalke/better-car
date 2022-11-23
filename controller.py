import board 
import neopixel
import time
import constants as const

pixel_pin = board.D18

pixels = neopixel.NeoPixel(
    pixel_pin, const.num_pixels, brightness=0.3
)

def pixels_off():
    pixels.fill(const.off)

def fill_pixels(color):
    pixels_off()
    pixels[0] = color
    time.sleep(1)
    pixels[1] = color
    time.sleep(1)
    pixels[2] = color
    pixels[3] = color
    time.sleep(2)
    pixels_off()
    pixels[1] = const.blue

def pixel_signals(sport_mode):
    if sport_mode is True:
        fill_pixels(const.red)
    else:
        fill_pixels(const.green)

