"""
defines a class type for sqlalchemy, and loads the database based on a csv file
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy import Column, Integer, String
from sqlalchemy.types import Float
import csv
# import psycopg2
from .settings import DATABASE_URL

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
Base.metadata.create_all(bind=engine)


class Songdb(Base):
    __tablename__ = "Song_table"
    """Song_db data model based on sqlalchemy 
    used by elephant postgres database """

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
    """
    reset the database and re-create it
    """
    try:
        Base.metadata.drop_all(bind=engine)
    finally:
        Base.metadata.create_all(bind=engine)
    return


def get_db():
    """
    Open a db session
    """
    try:
        db.close()
    finally:
        db = SessionLocal()
        return db


def load_csv(db: Session, file_name: str):
    """
    Load a csv file into the db session
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



