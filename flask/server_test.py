#!/usr/bin/env python3
from flask import Flask, request, Response
from flask_restful import Resource, Api
from flask import jsonify
from flask import send_file
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

password = "password"

lights = [
    {'id' : 4, 'value' : True,  'name': 'Sala'},
    {'id' : 14, 'value' : False,  'name': 'Cocina'},
    {'id' : 15, 'value' : True,  'name': 'Comedor'},
    {'id' : 18, 'value' : False,  'name': 'Cuarto Principal'},
    {'id' : 17, 'value' : True,  'name': 'Cuarto Pilas'}
]
    

doors = [
    {'id' : 26, 'value' : False,  'name': 'Principal'},
    {'id' : 13, 'value' : True,  'name': 'Patio'},
    {'id' : 12, 'value' : False,  'name': 'Sala'},
    {'id' : 16, 'value' : True,  'name': 'Comedor'},
]

def enablePins():
    for light in lights:
        initPin(light['id'])
        pinMode(light['id'],1)
    for door in doors:
        initPin(door['id'])
        pinMode(door['id'],0)

def disablePins():
    for light in lights:
        freePin(light['id'])
    for door in doors:
        freePin(door['id'])
        
def setValue(array,id,value):
    for ele in array:
                if (ele['id'] == id):
                    ele['value'] = value
    return array                

def readInputs():
    for light in lights:
        ledValue=digitalRead(light['id'])
        light['value']=ledValue
    for door in doors:
        doorValue=digitalRead(door['id'])
        door['value']=doorValue

class Main(Resource):
    def get(self):
        if(request.headers.get('password') != password):
            resp = jsonify([])
        else:
            readInputs()
            resp = jsonify({'lights': lights, 'doors': doors})
        resp.headers['Access-Control-Allow-Origin'] = '*'
        return resp

class Lights (Resource):
    def post (self):
        resp = Response("")
        json_data = request.get_json()
        if(password != request.headers.get('password')):
            resp.status_code = 403
        else:
            resp.status_code = 200
            light_id = json_data['id']
            light_value = json_data['value']
            for light in lights:
                if (light['id'] == light_id):
                    light['value'] = light_value
                    digitalWrite(light_id,light_value)
            resp.headers['Access-Control-Allow-Origin'] = '*'
        
        return resp
    def options (self):
        resp = Response("")
        resp.headers['Access-Control-Allow-Origin'] = '*'
        resp.headers["Access-Control-Allow-Methods"] = "GET,POST,PUT,DELETE,OPTIONS"
        resp.headers["Access-Control-Allow-Headers"] = "Content-Type, Access-Control-Allow-Headers, Authorization, X-Requested-With, password"

        return resp

    def get (self):
        if (request.headers.get('password') != password):
            resp = jsonify([])
        else:
            readInputs()
            resp = jsonify( lights)
        resp.headers['Access-Control-Allow-Origin'] = '*'
        return resp

class Doors (Resource):
    def get (self):
        if(request.headers.get('password') != password):
            resp = jsonify([])
        else:
            readInputs()
            resp = jsonify(doors)
        resp.headers['Access-Control-Allow-Origin'] = '*'
        return resp
    def options (self):
        resp = Response("")
        resp.headers['Access-Control-Allow-Origin'] = '*'
        resp.headers["Access-Control-Allow-Methods"] = "GET,POST,PUT,DELETE,OPTIONS"
        resp.headers["Access-Control-Allow-Headers"] = "Content-Type, Access-Control-Allow-Headers, Authorization, X-Requested-With, password"

        return resp

class Photo(Resource):
    def get(self):
        picture()
        return send_file('image.jpg', mimetype='image/gif')
    def options (self):
        resp = Response("")
        resp.headers['Access-Control-Allow-Origin'] = '*'
        resp.headers["Access-Control-Allow-Methods"] = "GET,POST,PUT,DELETE,OPTIONS"
        resp.headers["Access-Control-Allow-Headers"] = "Content-Type, Access-Control-Allow-Headers, Authorization, X-Requested-With, password"

        return resp

class Auth(Resource):
    def post (self):
        resp = Response("")
        resp.headers['Access-Control-Allow-Origin'] = '*'
        password_temp = request.headers.get('password')
        if(password == password_temp):
            resp.status_code = 200
        else:
            resp.status_code = 403
        return resp
    def options (self):
        resp = Response("")
        resp.headers['Access-Control-Allow-Origin'] = '*'
        resp.headers["Access-Control-Allow-Methods"] = "GET,POST,PUT,DELETE,OPTIONS"
        resp.headers["Access-Control-Allow-Headers"] = "Content-Type, Access-Control-Allow-Headers, Authorization, X-Requested-With, password"

        return resp

api.add_resource(Main, '/')
api.add_resource(Auth, '/auth')
api.add_resource(Lights, '/lights')
api.add_resource(Doors, '/doors')
api.add_resource(Photo, '/img')


if __name__ == '__main__':
     enablePins()
     readInputs()    
     app.run(host='0.0.0.0', port = 5555)
     disablePins()