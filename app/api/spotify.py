import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from .settings import CLIENT_ID, CLIENT_SECRET
from fastapi import APIRouter
from  sqlalchemy.sql.expression import func, select
from .ormdb import *


client_cred = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager=client_cred)


router = APIRouter()


def audio_feat(id):
    """
    search_id[0]['insert_feature_here']
    id="4nb8OcZG8lpnHi5DmkEnY2" #Sample ID
    audio_feat("4nb8OcZG8lpnHi5DmkEnY2")

    :param id:
    :return:
    """
    return sp.audio_features(tracks=id)


@router.post('/spotify')
async def spotify():
    """
    a random api call to spotify
    :return:
    """
    db = get_db()
    songs = db.query(Songdb).order_by(func.random()).limit(1).all()
    db.close()
    song_id=[]
    for song in songs:
        song_id.append(song.id)
    return audio_feat(song_id[0])