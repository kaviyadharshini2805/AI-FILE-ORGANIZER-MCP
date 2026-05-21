import os
import shutil

def list_files(path):
    return os.listdir(path)

def create_folder(path):
    os.makedirs(path, exist_ok=True)
    return f"Folder created: {path}"

def move_file(source, destination):
    shutil.move(source, destination)
    return f"Moved {source} to {destination}"