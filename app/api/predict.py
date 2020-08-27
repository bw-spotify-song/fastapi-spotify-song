# import logging
from fastapi import APIRouter
from .fedata import *
import joblib


FILENAME = "./app/api/Heroku_test.joblib"
csv_url = "./app/api/Heroku_test.csv"

log = logging.getLogger(__name__)
router = APIRouter()


@router.get('/predict/{id}')
async def predict(id: str):
    """
    Takes a trackID string as input and returns a list
    of similar trackIDs
    ### Request Body
    - `Track ID`: String
    example: id = 5gM5byB8AWZrbadQfK45jf , 1Larmgh5TJN5PQQBhtN65P

    ### Response
    - `Suggested track IDs`: a list of trackIDs that are similar to the user's trackID
    """

    # Import the prediction model
    knn = joblib.load(FILENAME)
    df = pd.read_csv(csv_url)

    # Comes from the colab file containing the prediction model
    def predict_model(track_id, new_df, knn):
        obs = new_df.index[new_df['id'] == track_id]
        series = new_df.iloc[obs, 5:].to_numpy()

        neighbors = knn.kneighbors(series)
        new_obs = neighbors[1][0][6:20]
        return list(new_df.loc[new_obs, 'id'])

    tracks = predict_model(track_id= id, new_df=df, knn=knn)

    return {
         'Suggested track IDs': tracks
         }
