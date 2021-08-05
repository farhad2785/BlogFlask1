from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Development
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Development)

db = SQLAlchemy(app)
migrate = Migrate(app,db)

from mod_admin import admin
from mod_users import user
import views

app.register_blueprint(admin)
app.register_blueprint(user)

app.run()