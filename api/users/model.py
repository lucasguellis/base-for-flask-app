from flask import jsonify
from .. import db

class Users(db.Model):
    iduser = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(45))
    password = db.Column(db.String(45))
    name = db.Column(db.String(45))
    email = db.Column(db.String(45))
    created = db.Column(db.DateTime)
    modified = db.Column(db.DateTime)
    allows = db.Column(db.String(45))

    def __repr__(self):
        return repr({'iduser': self.iduser,
                'username': self.username,
                'password': self.password,
                'name': self.name,
                'email': self.email,
                'created': self.created,
                'modified': self.modified,
                'allows': self.allows})

    def returnall():
        r = db.session.query(Users).all()
        return r
