import board 
import neopixel
import time
import constants as cnst
from threading import Thread
import obd

const = None
car_data = None

pixel_pin = board.D10
num_pixels = 60

def set_const(obj):
    global const
    const = obj

def set_car_data(obj):
    global car_data
    car_data = obj

pixels = neopixel.NeoPixel(
    pixel_pin, num_pixels, brightness=0.3
)

class ledThread(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.daemon = True
        self.start()

    def run(self):
        global car_data
        global const
        while True:
            if const.thread_kill is True:
                break
            if(car_data.rpm > 2000):
                self.pixel_signals(const.sport_mode)

    def pixels_off(self):
        pixels.fill(const.off)

    def fill_pixels(self, color):
        self.pixels_off()
        pixels[0] = color
        time.sleep(1)
        pixels[1] = color
        time.sleep(1)
        pixels[2] = color
        pixels[3] = color
        time.sleep(2)
        self.pixels_off()

    def pixel_signals(self, sport_mode):
        if sport_mode is True:
            self.fill_pixels(const.red)
        else:
            self.fill_pixels(const.green)

  




class obdThread(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.daemon = True
        self.start()
    
    def run(self):
        global car_data
        global const

        #time.sleep(5)
        #car_data.new_rm(100)
        #obd.logger.setLevel(obd.logging.DEBUG)

        car_data.connection = obd.Async("/dev/ttyUSB0")

        #car_data.connection.watch(obd.commands.ENGINE_LOAD, callback=car_data.new_engine_load)
        car_data.connection.watch(obd.commands.INTAKE_PRESSURE, callback=car_data.new_engine_load)
        car_data.connection.watch(obd.commands.THROTTLE_POS, callback=car_data.new_throttle)
        car_data.connection.watch(obd.commands.OIL_TEMP, callback=car_data.new_oil_temp)
        car_data.connection.watch(obd.commands.RPM, callback=car_data.new_rpm)

        car_data.connection.start()

        const.set_obd_ready(True)
        

    
        