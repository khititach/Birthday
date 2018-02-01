from flask import Flask , request
from flask_restful import Resource , Api, reqparse
import json , time

app = Flask (_name_)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('info')
parser.add_argument('age')

class birthday(Resource):
	def post(self):
		args = parser.parse_args()
		day = args['info']
		age = args['age']	
		return {"birthdate":day,"Age":age}

api.add_resource(birthday,'/birthday')

if _name_  == '_main_':
	app.run(host='0.0.0.0',port=5500)