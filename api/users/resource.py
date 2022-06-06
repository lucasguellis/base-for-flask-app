from .model import Users
from flask_restful import Resource
from flask import jsonify

class GetAllUsers(Resource):
    def get(self):
        users = Users.returnall()
        print(type(repr(users[0])))
        return jsonify({'Users': [repr(user) for user in users]})
