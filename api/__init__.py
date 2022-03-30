from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from .connection.connection import conn_str, conn

## app config
app = Flask(__name__)
api = Api(app)

## database config
app.config['SQLALCHEMY_DATABASE_URI'] = conn_str
db = SQLAlchemy(app)
conn = conn()


## adding resources
from .users.resource import User
api.add_resource(User, '/user') 

