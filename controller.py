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
gear = 0

def set_const(obj):
    global const
    const = obj

def set_car_data(obj):
    global car_data
    car_data = obj

pixels = neopixel.NeoPixel(
    pixel_pin, num_pixels, brightness=0.2
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

    def blink(self, how_many):
        i = 0
        while i < how_many:
            pixels.fill(const.red)
            time.sleep(0.1)
            self.pixels_off()
            time.sleep(0.1)
            i= i+1
     

    def gear_up_sport(self):
        if car_data.rpm > 5000:
            pixels[0] = const.green
        if car_data.rpm > 5500:
            pixels[1] = const.yellow
        if car_data.rpm > 5900:
            pixels[2] = const.purple
        if car_data.rpm > 6300:    
            pixels[3] = const.red
        if car_data.rpm < 6450:
            self.blink(2)
        

    def gear_down(self, color):
        pixels[0] = color
        pixels[1] =  color

    def normal(self):
        if(car_data.rpm < 3500):
            self.gear_up_sport()

    
    def calculate_gear(self):
        global gear
        tmp = (car_data.speed / car_data.rpm) * 100
        if tmp > 0.5 and tmp < 0.9:
            gear = 1
        elif tmp > 1.1 and tmp < 1.6:
            gear = 2
        elif tmp > 1.6 and tmp < 2.5:
            gear = 3
        elif tmp > 2.5 and tmp < 3.1:
            gear = 4
        elif tmp > 3.1 and tmp < 3.7:
            gear = 5
        elif tmp > 3.7 and tmp < 5:
            gear = 6
        else: 
            gear = 0



    def sport(self):
        global gear
        if gear == 1:
                self.gear_up_sport()

        if gear == 2:
            if car_data.rpm < const.gears.g2:
                self.gear_down(const.red)
            else:
                self.gear_up_sport()

        if gear == 3:
            if car_data.rpm < const.gears.g3:
                self.gear_down(const.red)
            else:
                self.gear_up_sport()

        if gear == 4:
            if car_data.rpm < const.gears.g4:
                self.gear_down(const.red)
            else:
                self.gear_up_sport()

        if gear == 5:
            if car_data.rpm < const.gears.g5:
                self.gear_down(const.red)
            else:
                self.gear_up_sport()

        if gear == 6:
            if car_data.rpm < const.gears.g6:
                self.gear_down(const.red)
            else:
                self.gear_up_sport()




    def sport_controller(self):
        if (car_data.rpm > 3000 and car_data.oil_temp < 40) or (car_data.rpm > 4500 and car_data.oil_temp < 80):
            self.blink(2)
        else:
             if car_data.throttle >= 60:
                self.sport()
             else:
                self.normal()

                


    def pixel_signals(self, sport_mode):
        if sport_mode is True:
            self.sport_controller()
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

        time.sleep(2)
        car_data.new_rpm2(4000)
        time.sleep(2)
        car_data.new_rpm2(2000)
        time.sleep(5)
        car_data.new_oil_temp2(45)
        car_data.new_rpm2(4000)
        time.sleep(2)
        car_data.new_rpm2(4700)
        time.sleep(2)
        car_data.new_oil_temp2(85)
        time.sleep(7)
        car_data.new_rpm2(6700)
        #obd.logger.setLevel(obd.logging.DEBUG)

        # car_data.connection = obd.Async("/dev/ttyUSB0")

        # #car_data.connection.watch(obd.commands.ENGINE_LOAD, callback=car_data.new_engine_load)
        # car_data.connection.watch(obd.commands.SPEED, callback=car_data.new_engine_load)
        # #car_data.connection.watch(obd.commands.INTAKE_PRESSURE, callback=car_data.new_engine_load)
        # car_data.connection.watch(obd.commands.THROTTLE_POS, callback=car_data.new_throttle)
        # car_data.connection.watch(obd.commands.OIL_TEMP, callback=car_data.new_oil_temp)
        # car_data.connection.watch(obd.commands.RPM, callback=car_data.new_rpm)
        # car_data.connection.watch(obd.commands.SPEED, callback=car_data.new_speed)

        # car_data.connection.start()

        

    
        