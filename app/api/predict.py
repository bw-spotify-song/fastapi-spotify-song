import logging
import random
from fastapi import APIRouter
from pydantic import BaseModel, Field, validator
from .fedata import *
# import joblib
FILENAME = 'model-v1.sav'


log = logging.getLogger(__name__)
router = APIRouter()


@router.post('/predict')
async def predict(id: int):
    """
    takes song id from front end and returns a list
    of song ids that are closer to the one
    ### Request Body
    - `artist_name`: String
    - `track_name`: string
    - `acousticness`: Float
    - `energy`: Float

    ### Response
    - `suggestion`: a list of song ids that are similar to the user's
    """

    X_new = to_df(song)
    log.info(X_new)
    y_pred = random.choice([True, False])
    y_pred_proba = random.random() / 2 + 0.5
    return {
        'prediction': y_pred,
        'probability': y_pred_proba
    }
