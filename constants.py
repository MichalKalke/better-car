import json
from types import SimpleNamespace


class Constants:
    def __init__(self):
        f = open('constants.json')
        j = json.loads(f.read(), object_hook=lambda d: SimpleNamespace(**d))
        f.close()
        self.resolution = j.resolution
        self.gears = j.gearChanging
        self.white = (255,255,255)
        self.blue = (3, 173, 252)
        self.red = (237, 28, 36)
        self.green = (3, 155, 0)
        self.off = (0,0,0)
        self.obd_ready = False
        self.sport_mode = True
        self.thread_kill = False
    
    def set_obd_ready(self,r):
        self.obd_ready = r


class Car_data:
    def __init__(self):
        self.engine_load = 0
        self.throttle = 0
        self.oil_temp = 0
        self.rpm = 0
        self.connection = None

    def new_engine_load(self, r):
        #print(r.value)
        self.engine_load = int(r.value.magnitude)

    def new_throttle(self, r):
        self.throttle = int(r.value.magnitude)

    def new_oil_temp(self, r):
        self.oil_temp = int(r.value.magnitude)

    def new_rpm(self, r):
        self.rpm = int(r.value.magnitude)

    def new_rpm2(self, r):
        self.rpm = r

    def new_oil_temp2(self, r):
        self.oil_temp = r
