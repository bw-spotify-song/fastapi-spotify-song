from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy import Column, Integer, String
from sqlalchemy.types import Date, Float
import csv
import datetime
import psycopg2
from os import getenv
import os
# from ..main import db_url
# from dotenv import load_dotenv
# from os.path import join, dirname


# dotenv_path = join(dirname(__file__), '.env')
# load_dotenv(dotenv_path)
# SECRET_KEY = os.environ.get("SECRET_KEY")
# print(dotenv_path)

# database file
DATABASE_URL = "postgres://rrjsotrn:bcLxGv5Ukb0PKwPQjFxA7J99eHvImioH@lallah.db.elephantsql.com:5432/rrjsotrn"
# engine = create_engine(getenv('DATABASE_URL'))
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
Base.metadata.create_all(bind=engine)


class Songdb(Base):
    __tablename__ = "Song_table"
    """Song_db data model based on sqlalchemy"""
    index = Column(Integer, primary_key=True, index=True)
    track_number = Column(String)
    album = Column(String)
    acousticness = Column(Float)
    danceability = Column(Float)
    energy = Column(Float)
    instrumentalness = Column(Float)
    speechiness = Column(Float)
    tempo = Column(Float)
    popularity = Column(Integer)
    liveness = Column(Float)
    loudness = Column(Float)
    valence = Column(Float)
    uri = Column(String(255), index=True)
    name = Column(String(255), index=True)
    id = Column(String(255), index=True)


def reset_db(engine):
    try:
        Base.metadata.drop_all(bind=engine)
    finally:
        Base.metadata.create_all(bind=engine)
    return

def get_db():
    try:
        db.close()
    finally:
        db = SessionLocal()
        return db


def load_csv(db: Session, file_name: str):
    """
    commit the csv file into the db session
    """

    with open(file_name, "r") as f:
        csv_reader = csv.DictReader(f)

        for row in csv_reader:
            db_record = Songdb(
                track_number=row["track_number"],
                album=row["album"],
                acousticness=row["acousticness"],
                danceability=row["danceability"],
                energy=row["energy"],
                instrumentalness=row["instrumentalness"],
                speechiness=row["speechiness"],
                tempo=row["tempo"],
                popularity=row["popularity"],
                liveness=row["liveness"],
                loudness=row["loudness"],
                valence=row["valence"],
                uri=row["uri"],
                name=row["name"],
                id=row["id"]
            )
            db.add(db_record)
        db.commit()
    return



