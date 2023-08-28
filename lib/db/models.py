from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from datetime import datetime

engine = create_engine('sqlite://workout_data')

Base = declarative_base()

class Workout(Base):
    __tablename__ = 'exercises'

    id = Column(Integer, primary_key=True)
    workout_name = Column(String)
    difficulty = Column(String)
    started_at = Column(DateTime)
    completed_at = Column(DateTime, default=datetime.now())

    def __repr__(self):
        return f'Exercise(id={self.id}, ' + \
            f'name={self.workout_name}, ' + \
            f'difficulty={self.difficulty})'
    
class User(Base):
    __tablename__ = 'users'

    