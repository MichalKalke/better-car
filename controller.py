import board 
import neopixel
import time

pixel_pin = board.D18

num_pixels = 60

blue = (3, 173, 252)
red = (237, 28, 36)
green = (3, 155, 0)
off = (0,0,0)

pixels = neopixel.NeoPixel(
    pixel_pin, num_pixels, brightness=0.3
)

def pixels_off():
    pixels.fill(off)

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
    pixels[1] = blue

def pixel_signals(sport_mode):
    if sport_mode is True:
        fill_pixels(red)
    else:
        fill_pixels(green)

