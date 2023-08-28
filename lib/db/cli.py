import click
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Workout, User

url = 'sqlite:///workout_data.db'

engine = create_engine(url)
Session = sessionmaker(bind=engine)
Session()