# loggin import file
from .logging import Logging
from .filesystem import FileSystem
import re

class User:
    def __init__(self, firstname, lastname):
        self.log = Logging()
        self.firstname = firstname
        self.lastname = lastname
    
    def validate(self):
        if not self.firstname.isdigit() & self.lastname.isdigit():
            reg = re.compile('[^a-zA-Z ]')
            firstname = reg.sub("", self.firstname).strip().replace(" ", "")
            lastname = reg.sub("", self.lastname).strip().replace(" ", "")
            if len(firstname) < 50 and len(lastname) < 50:
                return firstname, lastname
            else:
                # logging
                self.log.DEBUG(f"{firstname} and {lastname} length much 50 symbols")
        else:
            self.log.CRITICAL(f"In input's have numbers: {self.firstname} or {self.lastname}")

    def name_length(self):
        try:
            length = [len(item) for item in self.validate()]
            print("*" * 100)
            print(f"Length new input first word: {length[0]} and length second word: {length[1]}")
            print("_" * 100)
        except TypeError as te:
            self.log.CRITICAL(te)
    
    def past_name(self, file):
        # print("*" * 100)
        print(f"Last input: {file}")
        print("*" * 100)