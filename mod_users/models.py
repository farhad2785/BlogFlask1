from sqlalchemy import Integer, String, Column
from werkzeug.security import generate_password_hash, check_password_hash

from app import db


class User(db.Model):
    __tablename__ = 'users'  # --->changing table name
    id = Column(Integer(), primary_key=True)
    email = Column(String(256), nullable=False, unique=True)
    password = Column(String(128), nullable=False, unique=False)
    role = Column(Integer(), nullable=False, default=0)
    full_name = Column(String(256), nullable=True, unique=False)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self,password):
        return check_password_hash(self.password,password)
    
    def is_admin(self):
        return self.role == 1