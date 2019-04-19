import os
import tempfile

def create_temp_file():
    return tempfile.NamedTemporaryFile().name

def delete_temp_files(*args):
    for file in args:
         os.remove(file)

def write_to_file(data, file_path):
    with(open(file_path, "w")) as file:
        file.write(data)
