# import logging
from fastapi import APIRouter
from .fedata import *
import joblib


FILENAME = "./app/api/Heroku_test.joblib"
csv_url = "./app/api/Heroku_test.csv"

log = logging.getLogger(__name__)
router = APIRouter()


@router.post('/predict')
async def predict(id):
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


    knn = joblib.load(FILENAME)
    df = pd.read_csv(csv_url)

    def predict_model(track_id, new_df):
        obs = new_df.index[new_df['id'] == track_id]
        series = new_df.iloc[obs, 5:].to_numpy()

        neighbors = knn.kneighbors(series)
        new_obs = neighbors[1][0][6:20]
        return list(new_df.loc[new_obs, 'id'])

    # id1 = '4KuFgXbahxEILwg8qu1kKG'
    # id1 = [-1,'73LY41HCJzlQwoNBmWM7Md']
    # id1 = id1.reshape(1,-1)


    tracks = predict_model(track_id= id, new_df=df)
    return {
         'Suggested track IDs': tracks
         }
