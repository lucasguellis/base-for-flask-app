from importlib.resources import Resource


from flask_restful import Resource

class User(Resource):
    def get(self):
        return 