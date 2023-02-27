import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base
from database import engine

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.Text)
    email = sa.Column(sa.Text, unique=True)
    username = sa.Column(sa.Text, unique=True)
    password_hash = sa.Column(sa.Text)


class Contract(Base):
    __tablename__ = 'contracts'
    id = sa.Column(sa.Integer, primary_key=True)
    project = sa.Column(sa.String)
    dogovor_npo = sa.Column(sa.String)
    kontract_mzkt = sa.Column(sa.String)


class Location(Base):
    __tablename__ = 'locations'
    id = sa.Column(sa.Integer, primary_key=True)
    vch_no = sa.Column(sa.Integer)
    location = sa.Column(sa.String)
