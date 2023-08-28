from models import Workout, User
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from random import choice as rc
from faker import Faker
import random

engine = create_engine('sqlite:///workout_data.db')
Session = sessionmaker(bind=engine)
session = Session()

fake = Faker()

exercise_types = ['Cardio', 'Weight Lifting', 'CrossFit', 'Boxing', 'Yoga', 'Swimming']
sport_types = ['Football', 'Rugby', 'Basketball', 'Soccer', 'Lacrosse', 'Hockey']

def create_workouts():
    workouts = [
        Workout(
            exercise=random.choice(exercise_types),
        ) 
    for i in range(25)]
    session.add_all(workouts)
    session.commit()
    return workouts

def create_users():
    users = [
        User(
            user_name = fake.name(),
            age = random.randint(1,99),
            sport = random.choice(sport_types)
    ) 
    for i in range(50)]
    session.add_all(users)
    session.commit()
    return users

def delete_records():
    session.query(Workout).delete()
    session.query(User).delete()
    session.commit()

def one_to_many(workouts, users):
    for workout in workouts:
        workout.user = rc(users)
    
    session.add_all(workouts)
    session.commit()

    return workouts, users

if __name__ == '__main__':
    delete_records()
    workouts = create_workouts()
    users = create_users()
    workouts, users = one_to_many(workouts, users)