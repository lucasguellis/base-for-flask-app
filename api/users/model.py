from ...api import db

class users(db.Model):
    iduser = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(45))
    password = db.Column(db.String(45))
    name = db.Column(db.String(45))
    email = db.Column(db.String(45))
    created = db.Column(db.Datetime)
    modified = db.Column(db.Datetime)
    isadmin = db.Column(db.String(45))

    def __repr__(self):
        return {'iduser': self.iduser,
                'username': self.username,
                'password': self.password,
                'name': self.name,
                'email': self.email,
                'created': self.created,
                'modified': self.modified,
                'isadmin': self.isadmin}

