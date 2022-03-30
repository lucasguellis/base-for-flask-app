from importlib.resources import Resource
from .. import db

from flask_restful import Resource

class User(Resource):
    def get(self):
        users = db.session.query(User).all
        print(users)
        return {'message': users}