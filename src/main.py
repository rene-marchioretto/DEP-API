from flask import Flask
from flask_restful import Resource, Api
from data import *

app = Flask(__name__)
api = Api(app)

class json(Resource):
    def get(self):
        data = json_url()
        return data


api.add_resource(json, '/')


if __name__ == '__main__':
    app.run(debug= True)

