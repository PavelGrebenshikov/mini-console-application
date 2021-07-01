from .logging import Logging
from os import getcwd

class FileSystem:
    def __init__(self, filename):
        self.filename = filename
        self.log = Logging()
        self.isFile = self.isFile()

    def isFile(self):
        for files in __file__:
            if files in self.filename:
                return True
        return False
    
    def check_file(self):
        if self.isFile:
            return True
        return False

    def create_file(self, data=None):
        try:
            if self.check_file:
                with open(getcwd() + "/" + self.filename, "w", encoding="utf-8") as file:
                    if isinstance(data, str):
                        file.writelines(data + "\n")
                    else:
                        file.writelines(data[0] + " " + data[1])

        except FileExistsError as fee:
            self.log.ERROR(fee)

    def read_file(self):
        try:
            if self.check_file:
                with open(getcwd() + "/" + self.filename, "r", encoding="utf-8") as rfile:
                    return rfile.read()
            else:
                self.log.DEBUG("Wrong not read files")
        except FileNotFoundError as fee:
            self.log.INFO(fee)
            return "The last input was not found"