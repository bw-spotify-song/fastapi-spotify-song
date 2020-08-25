from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
# from fastapi import Depends

import uvicorn
from typing import List, Optional

from .api.predict import Song
from .api.ormdb import *
from .api.fedata import *
from app.api import predict, viz

app = FastAPI(
    title='Spotify song API',
    description='Fast-API interface for Spotify application',
    version='0.1',
    docs_url='/',
)


@app.get("/")
def root():
    return


app.include_router(predict.router)
app.include_router(viz.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)


@app.get("/Database")
def db_reload():
    """
    Reload the database from spotify_music.csv file
    """
    reset_db(engine)
    db = get_db()
    file_name = "./app/api/spotify_music.csv"
    load_csv(db, file_name)
    db.close()
    return "Data Base Reloaded!"


@app.get("/songs/", response_model=List[Song])
def songs_list():
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
