from .. import db

class UserModel(db.Model):
    __tablename__ = 'users'
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
                'created': self.created.strftime('%d/%m/%Y, %H:%M:%S'),
                'modified': self.modified,
                'allows': self.allows})

    def returnall():
        try:
            r = db.session.query(UserModel).all()
        except:
            return None
        return r

    def returnuserinfo(iduser):
        try:
            r = db.session.query(UserModel).filter(UserModel.iduser == iduser).first()
        except:
            return None
        return r
