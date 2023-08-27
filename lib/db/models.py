from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, String, Integer, DateTime, ForeignKey

Base = declarative_base()

class exercise(Base):
    __tablename__ = 'exercises'
