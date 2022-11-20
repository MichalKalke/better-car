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
        self.sport_mode = True
