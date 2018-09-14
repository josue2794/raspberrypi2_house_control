from flask import Flask, request
from flask_restful import Resource, Api
from flask import jsonify

app = Flask(__name__)
api = Api(app)

lights = {
    0 : 0,
    1 : 0,
    2 : 0,
    3 : 0,
    4 : 0
}

doors = {
    0 : 0,
    1 : 0,
    2 : 0,
    3 : 0
}

class Main(Resource):
    def get(self):
        return jsonify(lights, doors)

class Lights (Resource):
    def post (self):
        json_data = request.get_json()
        light_id = json_data['id']
        light_state = json_data['state']
        lights[light_id] = light_state
        return 200

class Photo(Resource):
    def get(self):
        if (num == 1):
            return 'Aquí se envía la foto'

api.add_resource(Main, '/')
api.add_resource(Lights, '/lights')
api.add_resource(Photo, '/img')


if __name__ == '__main__':
     app.run(host='0.0.0.0', port = 5555, debug=True)
