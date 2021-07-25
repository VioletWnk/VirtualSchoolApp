import os
import pathlib
from pathlib import Path


class FileHandler:
    def get_file_path(self, file_name):
        dir_path = pathlib.Path.cwd()
        new_path = Path(dir_path, file_name)
        return new_path

    def write(self, path, data):
        file = open(path, 'w')
        file.writelines(data)
        file.close()

    def read(self, path):
        file = open(path, 'r')
        file_read = file.read()
        file.close()
        return file_read

    def path_is_valid(self, path):
        return os.path.exists(path)