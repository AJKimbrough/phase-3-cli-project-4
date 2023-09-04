import click
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import User, Workout

url = 'sqlite:///workout_data.db'

engine = create_engine(url)
Session = sessionmaker(bind=engine)
session = Session()

@click.group()
def cli():
    """Workout Tracker"""
    pass

@cli.command()
def delete_user():
    """Delete User"""

    user_name = click.prompt("User Name")

    user_to_delete = session.query(User).filter_by(user_name = user_name).first()

    if user_to_delete:
        session.query(Workout).filter_by(user = user_to_delete).delete()
        session.delete(user_to_delete)
        session.commit()
        print(f'User {user_name} deleted')
    else:
        print(f'{user_name} not found.')

if __name__ == '__main__':
    cli()
