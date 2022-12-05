import json
from types import SimpleNamespace


class Constants:
    def __init__(self):
        f = open('constants.json')
        j = json.loads(f.read(), object_hook=lambda d: SimpleNamespace(**d))
        f.close()
        self.resolution = j.resolution
        self.gears = j.gearDown
        self.gears_eco = j.gearUp
        print(self.gears_eco.g2)
        self.white = (255,255,255)
        self.blue = (3, 173, 252)
        self.red = (237, 28, 36)
        self.green = (3, 155, 0)
        self.yellow = (255, 255, 0)
        self.purple = (104, 51, 168)
        self.off = (0,0,0)
        self.sport_mode = False
        self.thread_kill = False

class Car_data:
    def __init__(self):
        self.engine_load = 0
        self.throttle = 0
        self.oil_temp = 0
        self.rpm = 0
        self.speed = 0
        self.connection = None

    def new_engine_load(self, r):
        self.engine_load = int(r.value.magnitude)

    def new_throttle(self, r):
        self.throttle = int(r.value.magnitude)

    def new_oil_temp(self, r):
        self.oil_temp = int(r.value.magnitude)

    def new_rpm(self, r):
        self.rpm = int(r.value.magnitude)

    def new_speed(self, r):
        self.speed = int(r.value.magnitude)

    def new_speed2(self, r):
        self.speed = r

    def new_throttle2(self, r):
        self.throttle = r
    def new_rpm2(self, r):
        self.rpm = r

    def new_oil_temp2(self, r):
        self.oil_temp = r
