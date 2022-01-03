# Autor : Sébastien Duruz
# Date : 03.01.2022

import json

class JsonManipulation:
    """
    Class JsonManipulation : Access, read, write to JSON file
    """
    
    def __init__(self, filePath):
        """
        Class Constructor
        """
        
        self.filePath = filePath
        
    def read_json(self):
        """
        Read the content of the config file
        """
        
        with open(self.filePath, "r") as jsonContent:
            return json.load(jsonContent)    