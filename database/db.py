import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from entity.video import Base

DATABASE_URL = os.environ.get('DATABASE_URL', 'sqlite:///videos.db')

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)

def init_db():
    Base.metadata.create_all(engine)