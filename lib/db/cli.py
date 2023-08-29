import click
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Workout, User

url = 'sqlite:///workout_data.db'

engine = create_engine(url)
Session = sessionmaker(bind=engine)

@click.group()
def cli():
    """Workout Tracker"""
    pass

@cli.command()
@click.argument('date')
@click.argument('user', nargs=1)
def add_user(date, user):
    """Add new user"""
    session = Session()

    users_data = [{'user_name': user_name, 'age': age, 'sport': sport} for user_name, age, sport in (w.split(':') for w in workout)]
    workout = Workout(date = date, workouts = [])

    for workout_data in workouts_data:
        workout = Workout()
