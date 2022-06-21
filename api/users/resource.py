from .model import UserModel
from flask_restful import Resource

class GetAllUsers(Resource):
    def get(self):
        users = UserModel.returnall()
        return {'Users': [repr(user) for user in users]}

class GetUserInfoByID(Resource):
    def get(self, iduser):
        user = UserModel.returnuserinfo(iduser)
        return {'User': repr(user)}