from fastapi import APIRouter, HTTPException
import pandas as pd
import plotly.express as px
router = APIRouter()

FILENAME = "./app/api/BW_Spotify_Final.joblib"
csv_url = "./app/api/BW_Spotify_Final.csv"







@router.get('/viz/{Radar Chart}')
async def viz(track_id: str):
    """
    Visualize state unemployment rate from [Federal Reserve Economic Data](https://fred.stlouisfed.org/) 📈
    
    ### Path Parameter
    `statecode`: The [USPS 2 letter abbreviation](https://en.wikipedia.org/wiki/List_of_U.S._state_and_territory_abbreviations#Table) 
    (case insensitive) for any of the 50 states or the District of Columbia.

    ### Response
    JSON string to render with [react-plotly.js](https://plotly.com/javascript/react/)
    """
def feature_average(track_id):
    '''
    This function returns the sum of the features for the ten recommended songs.
    '''
    similar_tracks = predict(track_id)
    # Return a dataframe with only the ten most similar tracks
    similar_tracks = new_df[new_df["id"].isin(similar_tracks)]
    similar_tracks = similar_tracks[['acousticness', 'danceability',
                                     'energy', 'instrumentalness',
                                     'liveness',
                                     'speechiness', 'valence']]
    # Average features of ten tracks
    acousticness = round(similar_tracks['acousticness'].mean(), 2)
    danceability = round(similar_tracks['danceability'].mean(), 2)
    energy = round(similar_tracks['energy'].mean(), 2)
    instrumentalness = round(similar_tracks['instrumentalness'].mean(), 2)
    liveness = round(similar_tracks['liveness'].mean(), 2)
    #mode = round(similar_tracks['mode'].mean(), 2)
    speechiness = round(similar_tracks['speechiness'].mean(), 2)
    valence = round(similar_tracks['valence'].mean(), 2)
    # Store all to "features" variable
    features = []
    attributes = [
        acousticness,
        danceability,
        energy,
        instrumentalness,
        liveness,
        speechiness,
        valence]
    # features.append(acousticness)
    for attribute in attributes:
        features.append(attribute)
    return features
    r = feature_average(track_id)
    attributes = [
        'acousticness',
        'danceability',
        'energy',
        'instrumentalness',
        'liveness',
        'speechiness',
        'valence']



      # Make Plotly figure
    fig = px.line_polar(r=r, theta=attributes, line_close=True)
    fig.update_traces(fill='toself')
    fig.show()
    # Return Plotly figure as JSON string
    return fig.to_json()
