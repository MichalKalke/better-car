import json
from types import SimpleNamespace

class Constants():
    def __init__(self):
        f = open('constants.json')
        #j = json.dumps(f)
        #j = json.load(f)
        j = json.loads(f.read(), object_hook=lambda d: SimpleNamespace(**d))
        f.close()
        print(j.colors.white)
        #self.colors = j['colors']
        #print(self.colors)
        # self.width = 800
        # self.height = 480
