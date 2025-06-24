from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import requests
from dotenv import load_dotenv
import os

load_dotenv()

CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")

date = input("Which year would you like to travel to? Type the date in this format YYYY-MM-DD: ")

URL = f"https://www.billboard.com/charts/hot-100/{date}"
response = requests.get(URL)
website_html = response.text

scope = "playlist-read-private, " \
        "user-read-currently-playing, " \
        "user-read-currently-playing, " \
        "user-follow-read, playlist-modify-private"

soup = BeautifulSoup(website_html, "html.parser")
top = soup.select("li ul li h3")
top_songs = [song.getText().strip() for song in top]

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="https://open.spotify.com/",
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt",
        username="sunaina ☀",
    )
)
user_id = sp.current_user()["id"]
print(user_id)

song_uris = []
year = date.split("-")[0]
for song in top_songs:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        pass
description = "Top 100 songs on Billboard charts for the specified year."


playlist = sp.user_playlist_create(user=user_id,
                                   name=f"{date} Billboard 100",
                                   description=description,
                                   public=False)
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
