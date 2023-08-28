import click
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Workout, User

url = 'sqlite:///workout_data.db'

engine = create_engine(url)
Session = sessionmaker(bind=engine)


def cli():
    """Workout Tracker"""
    pass

@cli.command()
@click.argument('date')
@click.argument('workout', nargs=1)
def add_workout(date, workout):
    """Add new workout"""
    session = Session()