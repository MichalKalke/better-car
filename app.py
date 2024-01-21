from flask import Flask, jsonify
from threading import Thread

app = Flask(__name__)
car_data = None

def set_car_data(obj):
    global car_data
    car_data = obj

@app.route('/realtime_data', methods=['GET'])
def get_realtime_data():
    return jsonify({
        'engine_load': car_data.engine_load,
        'throttle': car_data.throttle,
        'oil_temp': car_data.oil_temp,
        'rpm': car_data.rpm,
        'speed': car_data.speed,
        'gear': car_data.gear
    })

def run_flask():
    app.run(debug=False)

class FlaskThread(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.start()

flask_thread = Thread(target=run_flask)
flask_thread.start()