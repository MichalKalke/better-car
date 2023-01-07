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
    pixel_pin, num_pixels, brightness=0.05
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
            if(car_data.rpm > 1500):
                self.pixel_signals(const.sport_mode)

    def pixels_off(self):
        pixels.fill(const.off)
        

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
        if car_data.rpm > 6450:
            self.blink(2)
       

    def gear_down(self, color):
        pixels[0] = color
        pixels[1] =  color
        time.sleep(1)
        self.pixels_off()


    def gear_up(self, color):
        pixels[2] = color
        pixels[3] =  color
        time.sleep(1)
        self.pixels_off()


    def normal(self):
        if(car_data.rpm > 3500):
            self.gear_up(const.purple)
        if(car_data.rpm < 2000):
            self.gear_down(const.blue)


    def calculate_gear(self):
        global gear
        tmp = (car_data.speed / car_data.rpm) * 100
        print(tmp)
        if tmp > (const.gear.g1 - 0.2) and tmp < (const.gear.g1 + 0.2):
            gear = 1
        elif tmp > (const.gear.g2 - 0.2) and tmp < (const.gear.g2 + 0.2):
            gear = 2
        elif tmp > (const.gear.g3 - 0.2) and tmp < (const.gear.g3 + 0.2):
            gear = 3
        elif tmp > (const.gear.g4 - 0.2) and tmp < (const.gear.g4 + 0.2):
            gear = 4
        elif tmp > (const.gear.g5 - 0.2) and tmp < (const.gear.g5 + 0.2):
            gear = 5
        elif tmp > (const.gear.g6 - 0.2) and tmp < (const.gear.g6 + 0.2):
            gear = 6
        else: 
            gear = 0


    def sport(self):
        global gear
        self.calculate_gear()
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


    def eco(self):
        global gear
        self.calculate_gear()
        if gear == 1:
            if car_data.rpm > const.gears_eco.g1:
                self.gear_up(const.green)
            elif car_data.rpm < const.gears_eco.down:
                self.gear_down(const.yellow)

        if gear == 2:
            if car_data.rpm > const.gears_eco.g2:
                self.gear_up(const.green)
            elif car_data.rpm < const.gears_eco.down:
                self.gear_down(const.yellow)


        if gear == 3:
            if car_data.rpm > const.gears_eco.g3:
                self.gear_up(const.green)
            elif car_data.rpm < const.gears_eco.down:
                self.gear_down(const.yellow)


        if gear == 4:
            if car_data.rpm > const.gears_eco.g4:
                self.gear_up(const.green)
            elif car_data.rpm < const.gears_eco.down:
                self.gear_down(const.yellow)


        if gear == 5:
            if car_data.rpm > const.gears_eco.g5:
                self.gear_up(const.green)
            elif car_data.rpm < const.gears_eco.down:
                self.gear_down(const.yellow)


        if gear == 6:
            if car_data.rpm < const.gears_eco.down:
                self.gear_down(const.yellow)


    def sport_controller(self):
        if (car_data.rpm > 3000 and car_data.oil_temp < 40) or (car_data.rpm > 4500 and car_data.oil_temp < 80):
            self.blink(2)
        else:
             if car_data.throttle >= 60:
                self.sport()
             else:
                self.normal()

    def eco_controller(self):
        if car_data.throttle <= 30:
            self.eco()
        else:
            self.normal()
                
    def pixel_signals(self, sport_mode):
        if sport_mode is True:
            self.sport_controller()
        else:
            self.eco_controller()


class obdThread(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.start()
    
    def run(self):
        global car_data
        global const

        car_data.connection = obd.Async("/dev/ttyUSB0")

        car_data.connection.watch(obd.commands.ENGINE_LOAD, callback=car_data.new_engine_load)
        car_data.connection.watch(obd.commands.THROTTLE_POS, callback=car_data.new_throttle)
        car_data.connection.watch(obd.commands.OIL_TEMP, callback=car_data.new_oil_temp)
        car_data.connection.watch(obd.commands.RPM, callback=car_data.new_rpm)
        car_data.connection.watch(obd.commands.SPEED, callback=car_data.new_speed)

        car_data.connection.start()

        

    
        
