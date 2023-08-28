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
    users = [User() for i in range(50)]
    session.add_all(users)
    session.commit()
    return users

def delete_records():
    session.query(Workout).delete()
    session.query(User).delete()
    session.commit()

if __name__ == '__main__':
    workouts = create_workouts()
    users = create_users()