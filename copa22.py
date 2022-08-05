from array import array
from flask import Flask, jsonify, request
from flask_restx import Api, Resource,fields
from sorteio_copa import copamundo

app  = Flask(__name__)
app_infos = dict(version='1.0', title='Copa do Mundo 2022',
        description='Sorteio automático dos 8 grupos da Copa do Mundo 2022')
rest_app = Api(app, **app_infos)

endpoint = rest_app.namespace('Grupos da Copa do Mundo 2022')
@endpoint.route("")
class Sorteio_Copa(Resource):
    @rest_app.expect()
    def get(self):
        copa22 = copamundo().sorteio_copa()
        return copa22, 200

if __name__ == "__main__":
    debug = True
    app.run(host = '0.0.0.0', port = 5005, debug = debug)