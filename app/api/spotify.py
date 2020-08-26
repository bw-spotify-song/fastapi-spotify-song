import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import os
from os import getenv


client_credentials_manager = SpotifyClientCredentials(
                                                client_id='86f9148edcfe4ec5b654fae8b523611e',
                                                client_secret='453ce91aebe449708fd35455caeff76e'
                                                )
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)


def audio_feat(id):
    """
    search_id[0]['insert_feature_here']
    id="4nb8OcZG8lpnHi5DmkEnY2" #Sample ID

    :param id:
    :return:
    """
    return sp.audio_features(tracks=id)

print(audio_feat("4nb8OcZG8lpnHi5DmkEnY2"))