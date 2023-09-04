import click
import random
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Workout, User
from seed import exercise_types, sport_types
from faker import Faker


url = 'sqlite:///workout_data.db'

engine = create_engine(url)
Session = sessionmaker(bind=engine)
session = Session()

fake = Faker()

@click.group()
def cli():
    """Workout Tracker"""
    pass

@cli.command()
def add_user():
    """Add new user"""

    user_name = click.prompt('User Name')
    age = click.prompt('Age', type=int)
    sport = click.prompt('Sport')
    exercise = click.prompt('Exercise')

    new_user = User(
        user_name = user_name,
        age = age,
        sport = sport

    )
    
    new_workout = Workout(
        exercise= exercise, 
        user = new_user
    )
    
    session.add(new_user)
    session.add(new_workout)
    session.commit()
    print(f'Workout added for user: {user_name}')


if __name__ == '__main__':
    cli()
