import logging
import random

from fastapi import APIRouter
import pandas as pd
from pydantic import BaseModel, Field, validator
# from uuid import UUID


log = logging.getLogger(__name__)
router = APIRouter()


class Song(BaseModel):
    """Use this data model to parse the request body JSON."""
    # song_id: UUID,
    x1: float = Field(..., example=3.14)
    # artist_name: str = Field(..., example='Chris Cooq')
    # track_name: str = Field(..., example='Lactose')
    # acousticness: float = Field(..., example=0.029400)
    # energy: float = Field(..., example=0.579)

    # def to_df(self):
    #     """Convert pydantic object to pandas dataframe with 1 row."""
    #     return pd.DataFrame([dict(self)])
    #
    # @validator('x1')
    # def x1_must_be_positive(cls, value):
    #     """Validate that x1 is a positive number."""
    #     assert value > 0, f'x1 == {value}, must be > 0'
    #     return value

    # @validator('track_name')
    # def check_string(cls, value):
    #     """Validate that track_name is a string."""
    #     # assert value > 0, f'x1 == {value}, must be > 0'
    #     assert isinstance(value, str), f'track_name == {value}, must be string'
    #     return value


@router.post('/predict')
async def predict(song: Song):
    """
    Make random baseline predictions for classification problem 🔮

    ### Request Body
    - `x1`: positive float
    - `artist_name`: String
    - `track_name`: string
    - `acousticness`: Float
    - `energy`: Float



    ### Response
    - `prediction`: Genre
    - `predict_proba`: float between 0.5 and 1.0, 
    representing the predicted class's probability

    Replace the placeholder docstring and fake predictions with your own model.
    """

    X_new = song.to_df()
    log.info(X_new)
    y_pred = random.choice([True, False])
    y_pred_proba = random.random() / 2 + 0.5
    return {
        'prediction': y_pred,
        'probability': y_pred_proba
    }
