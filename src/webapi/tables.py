import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base
from database import engine

Base = declarative_base()

class Contract(Base):
    __tablename__ = 'contracts'
    id = sa.Column(sa.Integer, primary_key=True)
    project = sa.Column(sa.String)
    dogovor_npo = sa.Column(sa.String)
    kontract_mzkt = sa.Column(sa.String)