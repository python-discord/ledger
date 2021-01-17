from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime


Base = declarative_base()


class User(Base):
    id = Column(Integer, primary_key=True)


class IssueMixin:
    opened = Column(DateTime)
    closed = Column(DateTime)
    author = Column()


class Repository(Base):
    __tablename__ = "repository"
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
