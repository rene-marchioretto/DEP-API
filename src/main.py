#import all the modules from flask to create a restfull api
from flask import Flask, jsonify
from flask_restful import Resource, Api
from data import *

#create the instance in flask for the app and api
app = Flask(__name__)
api = Api(app)

#create a class that consume de the json_url() function and return to the api
class json(Resource):
    def get(self):
        data = json_url()
        return jsonify(data)

# add this class a resource for the api use
api.add_resource(json, '/')


if __name__ == '__main__':
    app.run(debug= True)

