import logging

from fastapi import APIRouter
import pandas as pd
from pydantic import BaseModel, Field, validator
# from uuid import UUID


# pydantic Schema for Fastapi front end
class Song(BaseModel):
    """Front end data model"""
    acousticness: float = Field(..., example=0.029400)
    energy: float = Field(..., example=0.579)
    album: str
    track_number: int
    id: str
    name: str
    danceability: float
    instrumentalness: float
    loudness: float
    liveness: float
    speechiness: float
    tempo: float
    valence: float
    popularity: int
    uri: str

    class Config:
        orm_mode = True


def to_df(self):
    """Convert pydantic object to pandas dataframe with 1 row."""
    return pd.DataFrame([dict(self)])


