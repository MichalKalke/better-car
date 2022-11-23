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


class Car_data:
    def __init__(self):
        self.engine_load = 0
        self.accelerator = 0
        self.turbocharger_temp = 0
        self.rpm = 0
        self.connection = None

    def new_engine_load(self, r):
        self.engine_load = int(r.value.magnitude)

    def new_accelerator(self, r):
        self.accelerator = int(r.value.magnitude)

    def new_rpm(self, r):
        self.rpm = int(r.value.magnitude)
