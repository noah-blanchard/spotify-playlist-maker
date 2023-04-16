import os
import SpotifyConnection
import FolderParser
from dotenv import dotenv_values

sp = SpotifyConnection.SpotifyConnection(
    client_id=dotenv_values(".env")['client_id'],
    client_secret=dotenv_values(".env")['client_secret'],
    redirect_uri=dotenv_values(".env")['redirect_uri'],
    scope=dotenv_values(".env")['scope']
)

fp = FolderParser.FolderParser()

print("Would you like to export the song list to a JSON file? (y/n)")
export_json = input()

if export_json == 'y':
    print("Enter the path to the folder where the JSON file will be exported (leave blank for current folder): ")
    path = input()
    if path == '':
        path = os.getcwd()
    print("Enter the name of the JSON file (leave blank for songs.json): ")
    file_name = input()
    if file_name == '':
        file_name = 'songs.json'
    fp.exportJsonToFile(path, file_name)

print("Would you like to create a playlist on Spotify? (y/n)")
create_playlist = input()

if create_playlist == 'y':
    if sp.createPlaylist() is not None:
        print("Playlist created successfully!")
        print("Ready to add all the songs to the playlist ? (y/n)")
        add_songs = input()
        if add_songs == 'y':
            # iterate over fp.json
            # for each song, search for the song on Spotify
            # add the song to the playlist
            uris = []
            for i in range(len(fp.json)):
                artist = fp.json[i]['artist']
                song_name = fp.json[i]['song_name']
                uri = sp.searchUniqueSong(artist, song_name)
                if uri is not None:
                    print(f"Adding {song_name} by {artist} to playlist...")
                    print(f"URI: {uri}")
                    uris.append(uri)

            if sp.addSongToPlaylist(uris) is not None:
                print("Songs added successfully!")

print("Done!")
print("Thank you for using this program!")
print("Press any key to exit...")
input()

# sp.addSongToPlaylist(sp.playlist['id'], [uri])

# print("Enter folder path containing mp3 files: ")
# path = input()

# def extract_data_from_file_name(file_name):
#     data = file_name.split(" - ")
#     artist = data[0]
#     song_name = os.path.splitext(data[1])[0]
#     return {'artist': artist, 'song_name': song_name}

# # Set up Spotify OAuth client
# sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
#     client_id=client_id,
#     client_secret=client_secret,
#     redirect_uri=redirect_uri,
#     scope=scope
# ))

# print("Enter folder path containing mp3 files: ")
# path = input()

# # Generate JSON with an array of objects with two keys: artist and song name
# # The structure of the mp3 file name should be: artist - song name.mp3
# # Read content of the folder in the path
# # For each file in the folder, get the artist and song name
# # Add the artist and song name to the JSON array
# # Write the JSON array to a file
# # Create empty list to store artist and song names
# songs = []
# # Iterate over files in folder and extract artist and song name from file names
# for file_name in os.listdir(path):
#     if file_name.endswith(".mp3"):
#         data = extract_data_from_file_name(file_name)
#         songs.append(data)
# # Create JSON object with list of songs
# data = {'songs': songs}
# # Write JSON object to file
# with open('songs.json', 'w') as f:
#     json.dump(data, f)

# # Print confirmation message
# print(f"Successfully created songs.json file with {len(songs)} songs.")

# # Prompt for playlist name
# print("Enter playlist name: ")
# playlist_name = input()

# # Prompt for playlist description
# print("Enter playlist description: ")
# playlist_description = input()

# # Search for songs in Spotify from the JSON file
# # Create a playlist with the songs
# # Add the songs to the playlist
# with open('songs.json', 'r') as f:
#     data = json.load(f)

# track_uris = []

# for song in data['songs']:
#     artist = song['artist']
#     song_name = song['song_name']
#     query = f"artist:{artist} track:{song_name}"
#     result = sp.search(query, limit=1, type='track')
#     try:
#         uri = result['tracks']['items'][0]['uri']
#         track_uris.append(uri)
#     except IndexError:
#         print(f"{song_name} doesn't exist in Spotify. Skipped.")

# user_id = sp.current_user()['id']
# playlist = sp.user_playlist_create(
#     user=user_id, name=playlist_name, public=True, description=playlist_description)
# sp.playlist_add_items(playlist_id=playlist['id'], items=track_uris)

# # Print confirmation message
# print(
#     f"Successfully created {playlist_name} playlist with {len(track_uris)} songs.")
# # print link to playlist
# print(f"Link to playlist: {playlist['external_urls']['spotify']}")
