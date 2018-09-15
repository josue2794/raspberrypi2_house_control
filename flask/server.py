from flask import Flask, request
from flask_restful import Resource, Api
from flask import jsonify
from ctypes import cdll

gpio_lib = cdll.LoadLibrary("/home/taller7/lib/libGpioLib.so")
initPin = gpio_lib.GPIOExport
freePin = gpio_lib.GPIOUnexport
pinMode = gpio_lib.pinMode
blink = gpio_lib.blink
digitalRead = gpio_lib.digitalRead
digitalWrite = gpio_lib.digitalWrite
picture = gpio_lib.picture


app = Flask(__name__)
api = Api(app)

lights = {
    4 : 0,
    14 : 0,
    15 : 0,
    18 : 0,
    17 : 0
}

doors = {
    26 : 0,
    13 : 0,
    12 : 0,
    16 : 0
}

def enablePins():
    for light in lights:
        initPin(light)
        pinMode(light,1)
    for door in doors:
        initPin(door)
        pinMode(door,0)

def disablePins():
    for light in lights:
        pinMode(light,1)
    for door in doors:
        pinMode(door,0)


class Main(Resource):
    def get(self):
        return jsonify(lights, doors)

class Lights (Resource):
    def post (self):
        json_data = request.get_json()
        light_id = json_data['id']
        light_state = json_data['state']
        lights[light_id] = light_state
        digitalWrite(light_id,light_state)
        return 200

    def get (self):
        resp = jsonify(lights)
        resp.headers['Access-Control-Allow-Origin'] = '*'
        return resp

class Doors (Resource):
    def get (self):
        resp = jsonify(doors)
        resp.headers['Access-Control-Allow-Origin'] = '*'
        return resp

class Photo(Resource):
    def get(self):
        return 'Aquí se envía la foto'

api.add_resource(Main, '/')
api.add_resource(Lights, '/lights')
api.add_resource(Doors, '/doors')
api.add_resource(Photo, '/img')


if __name__ == '__main__':
     enablePins()
     app.run(host='0.0.0.0', port = 5555, debug=True)
     disablePins()
