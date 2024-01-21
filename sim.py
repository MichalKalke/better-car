import json
import time
from threading import Thread
import random

class CarSimulator:
    def __init__(self, data_file):
        self.data_file = data_file
        self.car_data = None

    def load_car_data(self):
        with open(self.data_file, 'r') as file:
            self.car_data = json.load(file)

    def simulate_data_change(self):
        # Symuluj losową zmianę danych samochodu
        self.car_data['engine_load'] += random.uniform(-5, 5)
        self.car_data['throttle'] += random.uniform(-2, 2)
        self.car_data['oil_temp'] += random.uniform(-0.5, 0.5)
        self.car_data['rpm'] += random.randint(-100, 100)
        self.car_data['speed'] += random.uniform(-5, 5)

        # Ogranicz wartości do pewnego zakresu (opcjonalnie)
        self.car_data['engine_load'] = max(0, min(100, self.car_data['engine_load']))
        self.car_data['throttle'] = max(0, min(100, self.car_data['throttle']))
        self.car_data['oil_temp'] = max(0, min(100, self.car_data['oil_temp']))


    def get_engine_load(self):
        return self.car_data['engine_load']

    def get_throttle(self):
        return self.car_data['throttle']

    def get_oil_temp(self):
        return self.car_data['oil_temp']

    def get_rpm(self):
        return self.car_data['rpm']

    def get_speed(self):
        return self.car_data['speed']

# Przykład użycia


# Symulacja zmiany danych co sekundę przez 5 sekund
class simThread(Thread):
    def __init__(self):
        self.simulator = CarSimulator('simulated_data.json')
        self.simulator.load_car_data()
        Thread.__init__(self)
        self.running = True
        self.start()
    
    def stop(self):
        self.running = False

    def run(self):
        while self.running:
            self.simulator.simulate_data_change()
            print("Engine Load:", int(self.simulator.get_engine_load()), "%")
            print("Throttle:", int(self.simulator.get_throttle()), "%")
            print("Oil Temperature:", int(self.simulator.get_oil_temp()), "°C")
            print("RPM:", int(self.simulator.get_rpm()))
            print("Speed:", int(self.simulator.get_speed()), "km/h")
            print("-----------------------")
            time.sleep(0.5)