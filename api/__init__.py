from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_ckeditor import CKEditor
from flask_ckeditor import CKEditorField

from .connection.secrets import conn_str


# app config
app = Flask(__name__)
api = Api(app)

# set optional bootswatch theme
app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'

admin = Admin(app, name='microblog', template_mode='bootstrap3')

# database config
app.config['SQLALCHEMY_DATABASE_URI'] = conn_str
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

ckeditor = CKEditor(app)
app.config['CKEDITOR_PKG_TYPE'] = 'basic'

# adding routes with resources
from .users.resource import User  # noqa: E402
api.add_resource(User, '/user')


class UserAdmin(ModelView):
    form_overrides = dict(text=CKEditorField)
    create_template = 'edit.html'
    edit_template = 'edit.html'


from .users.model import Users as UserModel  # noqa: E402
admin.add_view(UserAdmin(UserModel, db.session))
