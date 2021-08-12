import spotipy
import os
from spotipy.oauth2 import SpotifyOAuth
from fastapi import APIRouter, HTTPException
from dotenv import load_dotenv
import json

load_dotenv()

router = APIRouter()

@router.post("/login")
async def login(): 
    try:
        spauth = SpotifyOAuth(
            client_id= os.environ.get('SPOTIPY_CLIENT_ID'),
            client_secret= os.environ.get('SPOTIPY_CLIENT_SECRET'),
            redirect_uri = os.environ.get('SPOTIPY_REDIRECT_URI'),
            scope= os.environ.get('SPOTIPY_SCOPE'),
        )
        spotipy.Spotify(auth_manager=spauth)
        cached_token = spauth.get_cached_token()
        res = {
            "cached_token": cached_token,
            "refresh_token": cached_token["refresh_token"], 
            "expires_at": cached_token["expires_at"],
        }
    except HTTPException:
        raise HTTPException(status_code=404)
    return json.dumps(res)

@router.post("/refresh")
async def refresh():
    try:
        spauth = SpotifyOAuth(
            client_id= os.environ.get('SPOTIPY_CLIENT_ID'),
            client_secret= os.environ.get('SPOTIPY_CLIENT_SECRET'),
            redirect_uri = os.environ.get('SPOTIPY_REDIRECT_URI'),
            scope= os.environ.get('SPOTIPY_SCOPE'),
        )
        cached_token = spauth.get_cached_token()
        spauth.refresh_access_token(cached_token["refresh_token"])
        cached_token = spauth.get_cached_token()
        spotipy.Spotify(auth_manager=spauth)
        res = {
            "cached_token": cached_token,
            "refresh_token": cached_token["refresh_token"], 
            "expires_at": cached_token["expires_at"],
        }
    except HTTPException:
        raise HTTPException(status_code=404)
    return json.dumps(res)