from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from datetime import datetime
from sqlalchemy.orm import relationship, backref

engine = create_engine('sqlite://workout_data')

Base = declarative_base()

class Workout(Base):
    __tablename__ = 'workout'

    id = Column(Integer, primary_key=True)
    exercise = Column(String)
    completed_at = Column(DateTime, default=datetime.now())

    user_id = Column(Integer, ForeignKey('user.id'))

    def __repr__(self):
        return f'workout(id={self.id}, ' + \
            f'exercise={self.exercise}, ' + \
            f'completed_at={self.completed_at})'
    
class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    user_name = Column(String)
    age = Column(Integer)
    sport = Column(String)

    workouts = relationship("Workout", backref=backref('the_user'))

    def __repr__(self):
        return f'User(id={self.id}, ' + \
            f'name={self.user_name}, ' + \
            f'age={self.age}), ' + \
            f'sport={self.sport}'

