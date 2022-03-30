from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from .connection.connection import conn_str, conn

app = Flask(__name__)
api = Api(app)

app.config['SQLALCHEMY_DATABASE_URI'] = conn_str
db = SQLAlchemy(app)

conn = conn()

from .users.resource import User
api.add_resource(User, '/user') #http://127.0.0.1:5000/student/Lucas

if __name__ == '__main__':
    app.run(debug=True, port=5000)