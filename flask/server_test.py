from flask import Flask, request, Response
from flask_restful import Resource, Api
from flask import jsonify


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
    {'id' : 36, 'value' : False,  'name': 'Principal'},
    {'id' : 13, 'value' : True,  'name': 'Patio'},
    {'id' : 12, 'value' : False,  'name': 'Sala'},
    {'id' : 16, 'value' : True,  'name': 'Comedor'},
]

class Main(Resource):
    def get(self):
        if(request.headers.get('password') != password):
            resp = jsonify([])
        else:
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
            resp = jsonify( lights)
        resp.headers['Access-Control-Allow-Origin'] = '*'
        return resp

class Doors (Resource):
    def get (self):
        if(request.headers.get('password') != password):
            resp = jsonify([])
        else:
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
        return 'Aquí se envía la foto'
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
     app.run(host='0.0.0.0', port = 5555, debug=True)
