import datetime
from flask_login import UserMixin
from app.extensions import bcrypt
from ..database import db, CRUDMixin
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import relationship
from sqlalchemy.schema import Column, ForeignKey, Table
from sqlalchemy.types import Boolean, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

class User(CRUDMixin, UserMixin, db.Model,Base):
    __tablename__ = 'User'
    id = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False, unique=True)
    email = Column(String(128), nullable=False, unique=True)
    password = Column(String(128), nullable=False, unique=False)
    def __init__(self, password, **kwargs):
        super(User, self).__init__(**kwargs)
        self.set_password(password)
    def __repr__(self):
        return '<User #%s:%r>' % (self.id, self.name)
    def set_password(self, password):
        hash_ = bcrypt.generate_password_hash(password, 10).decode('utf-8')
        self.pw_hash = hash_
    def check_password(self, password):
        return bcrypt.check_password_hash(self.pw_hash, password)
    UnS = relationship("Skupina", secondary="UnS")
    UnS = relationship("Firma", secondary="UnS")


class Firma(CRUDMixin, db.Model):
    __tablename__ = 'Firma'
    id = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False, unique=True)
    ICO = Column(String(128), nullable=False, unique=True)
    users = relationship("User", secondary="UnS")

class Skupina(CRUDMixin, db.Model,Base):
    __tablename__ = 'Skupina'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    users = relationship("User", secondary="UnS")


class UnS(CRUDMixin, db.Model, Base):
    __tablename__ = 'UnS'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('User.id'))
    skupina_id = Column(Integer, ForeignKey('Skupina.id'))
    firma_id = Column(Integer, ForeignKey('Firma.id'))
