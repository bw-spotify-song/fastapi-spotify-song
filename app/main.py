"""
Spotify app based on fastapi
routs: root, database, songs, reset
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from typing import List, Optional
from .api.ormdb import *
from .api.fedata import Song
from .api import predict, viz, spotify

# to launch the local web server: uvicorn app.main:app --reload

app = FastAPI(
    title='Spotify Web App',
    description='Fast-API interface for Spotify application',
    version='0.1',
    docs_url='/',
)


app.include_router(predict.router)
app.include_router(viz.router)
app.include_router(spotify.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

@app.get("/")
def root():
    """
    Lists all the routs
    """
    return


@app.get("/Database")
def db_reload():
    """
    Reset and reload the database from spotify_music.csv file
    """
    reset_db(engine)
    db = get_db()
    file_name = "./app/api/spotify_music.csv"
    load_csv(db, file_name)
    db.close()
    return "Data Base Reloaded!"


@app.get("/songs/", response_model=List[Song])
def songs_list():
    """
    Get all the audio features of the songs
    that exist in the database.
    """
    db = get_db()
    songs = db.query(Songdb).all()
    db.close()
    return songs


@app.post("/Reset")
def reset():
    """
    Flush the database
    """
    reset_db(engine)
    return "Database reset!"


if __name__ == '__main__':
    uvicorn.run(app)
