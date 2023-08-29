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

    users_data = [
        {
            'user_name': user_name, 
            'age': age, 
            'sport': sport
        } 
        for user_name, age, sport in user
        ]
    
    workout = Workout(date = date, users = [])

    for user_data in users_data:
        user = User(
            name = user_data['user_name'],
            age = user_data['age'],
            sport = user_data['sport']
        )
        workout.user.append(user)

    session.add(workout)
    session.commit()

    if __name__ == '__main__':
        cli()
