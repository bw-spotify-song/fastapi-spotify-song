import logging
import random
from fastapi import APIRouter
from pydantic import BaseModel, Field, validator
from .fedata import *


log = logging.getLogger(__name__)
router = APIRouter()


# @validator('x1')
# def x1_must_be_positive(cls, value):
#     """Validate that x1 is a positive number."""
#     assert value > 0, f'x1 == {value}, must be > 0'
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

    X_new = to_df(song)
    log.info(X_new)
    y_pred = random.choice([True, False])
    y_pred_proba = random.random() / 2 + 0.5
    return {
        'prediction': y_pred,
        'probability': y_pred_proba
    }
