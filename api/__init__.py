from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from .connection.secrets import conn_str

## app config
app = Flask(__name__)
api = Api(app)


## database config
app.config['SQLALCHEMY_DATABASE_URI'] = conn_str
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


## adding routes with resources
from .users.resource import User
api.add_resource(User, '/user') 
