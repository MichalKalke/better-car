import json
from types import SimpleNamespace


class Constants:
    def __init__(self):
        f = open('constants.json')
        j = json.loads(f.read(), object_hook=lambda d: SimpleNamespace(**d))
        f.close()
        self.colors = j.colors
        self.resolution = j.resolution
        self.gears = j.gearChanging
