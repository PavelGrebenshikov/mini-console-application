import logging
import os

class Logging:
    def __init__(self):
        self.path = os.getcwd() + "/logs.txt"

    def WARNING(self, error):
        logging.basicConfig(filename=self.path, level=logging.WARNING)
        logging.warning(f"{error}")

    def INFO(self, error_info):
        logging.basicConfig(filename=self.path, level=logging.INFO)
        logging.info(f"{error_info}")
    
    def DEBUG(self, debug):
        logging.basicConfig(filename=self.path, level=logging.DEBUG)
        logging.debug(f"{debug}")
    
    def CRITICAL(self, critical):
        self.log = logging.basicConfig(filename=self.path, level=logging.CRITICAL)
        logging.critical(f"{critical}")
    
    def ERROR(self, error):
        logging.basicConfig(filename=self.path, level=logging.ERROR)
        logging.error(f"{error}")