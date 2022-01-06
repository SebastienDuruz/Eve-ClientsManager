# Autor : Sébastien Duruz
# Date : 04.01.2022

from pathlib import Path
from typing import Text


class TextManipulation:
    """
    Class TextManipulation : Access, read, write to TEXT file
    """
    
    from pathlib import Path
    
    def __init__(self, filePath):
        """
        Class Constructor
        """
        
        self.filePath = filePath
        
    def read_text(self):
        """
        Read the content of the config file
        """
        
        fileContent = []
        file = open('blacklist.txt', 'r')
        for l in file:
            fileContent.append(l.rstrip())
        file.close()
        return fileContent
    
    def delete_line(self, toRemove):
        """
        Delete a specific line from a text file
        """
        
        with open(self.filePath, "r+") as f:
            fileContent = f.readlines()
            f.seek(0)
            for i in fileContent:
                if i.__contains__(toRemove) == False:
                    f.write(i)
            f.truncate()
            
    def add_line(self, toAdd):
        """
        Add a specific line to text file if not already exists
        """
        
        with open(self.filePath, "r+") as f:
            for line in f:
                if toAdd in line:
                    return False
            else:
                f.write(toAdd + '\n')
                return True
