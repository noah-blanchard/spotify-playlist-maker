from spotipy.oauth2 import SpotifyOAuth
import spotipy


class SpotifyConnection:
    def __init__(self, client_id, client_secret, redirect_uri, scope):
        try:
            self.client_id = client_id
            self.client_secret = client_secret
            self.redirect_uri = redirect_uri
            self.scope = scope
            self.sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
                client_id=self.client_id,
                client_secret=self.client_secret,
                redirect_uri=self.redirect_uri,
                scope=self.scope
            ))
            self.playlist = None
        except Exception as e:
            raise ValueError(f"Failed to initialize SpotifyConnection: {e}")

    def getUserId(self):
        try:
            return self.sp.current_user()['id']
        except Exception as e:
            print(f"Error getting user id: {e}")
            return None

    def createPlaylist(self):
        try:
            user_id = self.getUserId()
            print("Enter the name of the playlist: ")
            playlist_name = input()
            print("Enter the description of the playlist: ")
            playlist_description = input()
            print("Creating playlist...")
            self.playlist = self.sp.user_playlist_create(
                user=user_id, name=playlist_name, public=True, description=playlist_description)
            return self.playlist
        except Exception as e:
            print(f"Error creating playlist: {e}")
            return None

    def addSongToPlaylist(self, track_uris):
        try:
            return self.sp.playlist_add_items(self.playlist['id'], track_uris)
        except Exception as e:
            print(f"Error adding songs to playlist: {e}")
            return None

    def searchUniqueSong(self, artist, song_name):
        try:
            query = f""
            if artist != '' or None:
                query = query + f"artist:{artist} "
            if song_name != '' or None:
                query = query + f"track:{song_name}"
            result = self.sp.search(query, limit=1, type='track')
            uri = result['tracks']['items'][0]['uri']
            return uri
        except IndexError:
            print(
                f"{song_name} by {artist} not found. Would you like to search for more results? (y/n)")
            search_more = input()
            if search_more == 'y':
                return self.searchMultipleSongs(artist, song_name)
            return None
        except Exception as e:
            print(f"Error searching for song: {e}")
            return None

    def searchMultipleSongs(self, artist, song_name, limit=30):
        try:
            song_number = -1
            query = f"track:{song_name}"
            result = self.sp.search(query, limit, type='track')
            for i in range(len(result['tracks']['items'])):
                print(
                    f"{i+1}. {result['tracks']['items'][i]['name']} by {result['tracks']['items'][i]['artists'][0]['name']}")
            if (len(result['tracks']['items']) == 0):
                print("No results found.")

            else:
                print(
                    "Enter the number of the song you would like to add (-1 for none): ")
                song_number = int(input())
            if song_number == -1:
                print("Would you like to make a custom search? (y/n)")
                custom_search = input()
                if custom_search == 'y':
                    return self.customSearch()
                else:
                    return None
            uri = result['tracks']['items'][song_number-1]['uri']
            return uri
        except Exception as e:
            print(f"Error searching for song: {e}")
            return None

    def customSearch(self):
        try:
            print("Enter the name of the song (leave blank if needed) : ")
            song_name = input()
            print("Enter the name of the artist (leave blank if needed) : ")
            artist = input()
            print("How many results would you like to see? (max 50) : ")
            limit = int(input())
            return self.searchMultipleSongs(artist, song_name, limit)
        except Exception as e:
            print(f"Error searching for song: {e}")
            return None
