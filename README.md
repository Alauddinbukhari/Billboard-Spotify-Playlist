# Billboard-Spotify-Playlist

# README
Introduction
This Python code scrapes the top 100 songs from the Billboard chart of a given date and creates a Spotify playlist with those songs. The user is prompted to enter the desired date in the YYYY-MM-DD format, and the program automatically extracts the year from the input date. The code makes use of the requests library and BeautifulSoup for web scraping, spotipy to communicate with the Spotify servers, and OAuth for authorization.

Installation
To run this code, you will need to install the following dependencies:

requests
beautifulsoup4
spotipy
You can install these dependencies by running the following command:

Copy code
pip install requests beautifulsoup4 spotipy
Usage
To run the code, open a terminal or command prompt and navigate to the directory containing the code.
Run the following command:
css
Copy code
python main.py
Enter the desired date in the format YYYY-MM-DD when prompted.
The code will extract the year from the input date and scrape the top 100 songs from the Billboard chart of that date.
The code will then create a private Spotify playlist named "{date} Billboard 100" and add the top 100 songs to that playlist.
The code will print "successfully done" once the playlist has been created and populated with the songs.
API keys
The following Spotify API keys have been hidden for security purposes:

SPOTIFY_CLIENT_ID
SPOTIFY_CLIENT_SECRET
REDIRECT_URL
You will need to obtain your own Spotify API keys and replace the above variables in the code with your own keys. You can obtain your own Spotify API keys by following the instructions on the Spotify Developer Dashboard.

Credits
This code was written by [insert your name here]. The web scraping portion of the code was inspired by the tutorial on this website. The Spotify portion of the code was inspired by the documentation on the Spotipy GitHub page.
