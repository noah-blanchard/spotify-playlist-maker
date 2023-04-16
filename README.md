# Readme

This program allows you to export a list of songs stored in a folder in JSON format and create a Spotify playlist with these songs. It can be very useful if you have a big folder with a lot of songs / musics, and you want to quickly convert it to a spotify playlist for your account !

## Configuration

To use this program, you need to have a Spotify account and valid client ID and client secret. You can obtain this information by creating an application on the Spotify Developer Dashboard.

## Installation

You need to install the following dependencies before running the program:

- spotipy
- python-dotenv

You can install them using pip:

```
pip install spotipy
pip install python-dotenv
```

## Usage

To use this program, you need to run the main.py file. The program will ask you several questions to find out what you want to do.
You need to specify your spotify API credentials in a `.env` file as shown :

```py
client_id = 'your_client_id'
client_secret = 'your_client_secret'
redirect_uri = 'your_redirect_uri'
scope = 'playlist-modify-public' # don't change this line
```

### Export the song list to a JSON file

The program will ask you if you want to export the song list to a JSON file. If you answer "y", the program will ask you for the path where the JSON file should be exported and the name of the file.

### Create a Spotify playlist

The program will ask you if you want to create a Spotify playlist with the exported songs. If you answer "y", the program will create a playlist and ask you if you want to add all the songs to the playlist.

### Add the songs to the Spotify playlist

The program will iterate over the exported song list and search for each song on Spotify. If the song is found, the program will add the song to the playlist.

### Finish the program

Once the program has finished executing the commands you have chosen, it will end and you can press any key to quit.

## Conclusion
There you have it! You now know how to use this program to export a song list and add it to a Spotify playlist. Feel free to adapt and improve it according to your needs!
