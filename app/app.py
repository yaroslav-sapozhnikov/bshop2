from flask import Flask
from config import Configuration
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_admin import AdminIndexView
from flask_admin.contrib.sqla import ModelView
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from flask_security import SQLAlchemySessionUserDatastore
from flask_security import Security
from flask_security import current_user

from flask import redirect, url_for, request
from form import ExtendedRegisterForm
from flask_mail import Mail

app = Flask(__name__)
app.config.from_object(Configuration)
db = SQLAlchemy(app)

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

mail = Mail(app)

from models import Post, User, Role, Record


class AdminMixin:
    def is_accessible(self):
        return current_user.has_role('admin')

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('security.login', next=request.url))


class AdminView(AdminMixin, ModelView):
    pass


class HomeAdminView(AdminMixin, AdminIndexView):
    pass


admin = Admin(app, 'SiteApp', url='/', index_view=HomeAdminView(name='Home'))
admin.add_view(AdminView(Post, db.session()))


user_datastore = SQLAlchemySessionUserDatastore(db.session, User, Role)
security = Security(app, user_datastore, register_form=ExtendedRegisterForm)

admin.add_view(AdminView(User, db.session()))
admin.add_view(AdminView(Record, db.session()))
