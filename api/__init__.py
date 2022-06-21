from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from config import CONN_STR

## app config
app = Flask(__name__)
api = Api(app)


## database config
app.config['SQLALCHEMY_DATABASE_URI'] = CONN_STR
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


## adding routes with resources
from .users.resource import GetAllUsers, GetUserInfoByID
api.add_resource(GetAllUsers, '/users') 
api.add_resource(GetUserInfoByID, '/user/<iduser>')
