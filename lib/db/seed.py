from models import Workout, User
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///workout_data.db')
Session = sessionmaker(bind=engine)
session = Session()

def create_workouts():
    workouts = [Workout() for i in range(25)]
    session.add_all(workouts)
    session.commit()
    return workouts

def create_users():
    users = [User()]