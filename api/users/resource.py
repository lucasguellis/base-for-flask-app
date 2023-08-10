from .model import returnall, userrepr
from flask_restful import Resource


class User(Resource):
    def get(self):
        users = returnall()
        return {'Users': [userrepr(users)]}
