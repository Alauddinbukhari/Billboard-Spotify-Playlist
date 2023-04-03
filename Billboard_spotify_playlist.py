import requests # You need to import the requests module to make HTTP requests

from bs4 import BeautifulSoup
import spotipy # You are using this module to communicate with the Spotify server

# Your Spotify credentials
SPOTIFY_CLIENT_ID = "your spotify client id"
SPOTIFY_CLIENT_SECRET = "your spotify client secret"
REDIRECT_URL = "http://example.com"

# Prompting user for input
date = input("which year do you want to travel to? Type the date in this format YYYY-MM-DD:")
year = date.split("-")[0]

# Making an HTTP GET request to Billboard's Hot 100 page
response = requests.get("https://www.billboard.com/charts/hot-100/{}/".format(date))
content = response.text

# Parsing the HTML content using BeautifulSoup
soup = BeautifulSoup(content, "html.parser")

# Extracting the song names from the HTML using BeautifulSoup
songs = soup.find_all(name="h3", class_="u-max-width-230@tablet-only", id="title-of-a-story")
songs_list = [song.getText() for song in songs]
print(songs_list)

# Cleaning up the song names
cleaned_songs_list = []
for song in songs_list:
    cleaned_song = song.replace('\n', '').replace("\t","")
    cleaned_songs_list.append(cleaned_song)
print(cleaned_songs_list)

# Spotify part
# Authorization comes first
spo = spotipy.oauth2.SpotifyOAuth(client_id=SPOTIFY_CLIENT_ID, client_secret=SPOTIFY_CLIENT_SECRET, redirect_uri=REDIRECT_URL, scope="playlist-modify-private")

# Getting a specific access token
ACCESS_TOKEN = spo.get_access_token()["access_token"]

# Creating a Spotify web API object to communicate with the Spotify servers
sp = spotipy.client.Spotify(auth=ACCESS_TOKEN, oauth_manager=spo, requests_timeout=150)

# Getting the user ID of the current user
user_id = sp.current_user()["id"]

# Creating a list of song URIs
songs_uri = []
i = 1
for song in cleaned_songs_list:
    # Searching for the song on Spotify
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    try:
        # Getting the URI of the first search result
        uri = result["tracks"]["items"][0]["uri"]
        songs_uri.append(uri)
    except IndexError:
        # Handling the case when the song is not available on Spotify
        print("Sorry, it is not available")
        print(i)
    i += 1

# Creating a new playlist with the date as its name
new_playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False, description=f"This playlist contains {year} songs")
playlist_id = new_playlist["id"]

# Adding the songs to the playlist
sp.playlist_add_items(playlist_id=playlist_id, items=songs_uri)
print("Successfully done")
