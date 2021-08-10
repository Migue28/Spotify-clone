import spotipy
import os
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv

load_dotenv()

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id= os.environ.get('CLIENT_ID'),
    client_secret= os.environ.get('CLIENT_SECRET'),
    redirect_uri = os.environ.get('SPOTIPY_REDIRECT_URI'),
    scope= os.environ.get('SCOPE'),
))

results = sp.current_user_saved_tracks()
for idx, item in enumerate(results['items']):
    track = item['track']
    print(idx, track['artists'][0]['name'], " – ", track['name'])