from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from config import Development

app = Flask(__name__)
app.config.from_object(Development)


db = SQLAlchemy(app)
migrate = Migrate(app, db)

from views import *
from mod_admin import admin
from mod_users import users
from mod_blog import blog

app.register_blueprint(admin)
app.register_blueprint(users)
app.register_blueprint(blog)
