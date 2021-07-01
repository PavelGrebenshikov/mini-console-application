import os
from .logging import Logging

class DataBase:
    def __init__(self):
        self.log = Logging()
        self.flags = self.directory()

    def directory(self):
        for directory in os.listdir():
            if directory in "data":
                return True
        return False

    def check_directory(self):
        if self.flags:
             os.chdir("data")
        else:
            os.makedirs("data")
            os.chdir("data")
        