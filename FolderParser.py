import os
import json


class FolderParser:
    def __init__(self, accepted_file_extensions=[".mp3"]):
        try:
            print("Enter folder path containing the audio files: ")
            self.folder = input()
            self.files = os.listdir(self.folder)
            self.files.sort()
            print(
                f"Successfully found {len(self.files)} files in folder the specified folder.")
            self.accepted_file_extensions = accepted_file_extensions
            self.json = self.getJson()
        except Exception as e:
            raise ValueError(
                f"Failed to initialize FolderParser with folder {self.folder}: {e}")

    def getJson(self):
        try:
            songs = []
            for file_name in self.files:
                if self.isAcceptedFileExtension(file_name):
                    data = self.extractDataFromFileName(file_name)
                    songs.append(data)
            return songs
        except Exception as e:
            raise ValueError(
                f"Failed to generate JSON from folder {self.folder}: {e}")

    def isAcceptedFileExtension(self, file_name):
        try:
            file_extension = os.path.splitext(file_name)[1]
            return file_extension in self.accepted_file_extensions
        except Exception as e:
            raise ValueError(
                f"Failed to check if file {file_name} has an accepted file extension: {e}")

    def extractDataFromFileName(self, file_name):
        try:
            data = file_name.split(" - ")
            artist = data[0]
            song_name = os.path.splitext(data[1])[0]
            return {'artist': artist, 'song_name': song_name}
        except Exception as e:
            raise ValueError(
                f"Failed to extract data from file name {file_name}: {e}")

    def exportJsonToFile(self, path, file_name):
        try:
            with open(os.path.join(path, file_name), 'w') as f:
                f.write(json.dumps(self.json, indent=4))
        except Exception as e:
            print(f"Failed to export JSON to file {file_name}: {e}")
