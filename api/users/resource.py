from .model import returnall, Users, userrepr
from flask_restful import Resource
from flask import jsonify

class User(Resource):
    def get(self):
        users = returnall()
        return {'Users': [userrepr(users)]}