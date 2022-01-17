# Author : Sébastien Duruz
# Date : 04.01.2022

import os


class TextManipulation:
    """
    Class TextManipulation : Access, read, write to TEXT file
    """
    
    def __init__(self, file_path):
        """
        Class Constructor
        """
        
        self.filePath = os.path.dirname(os.path.abspath(__file__)) + file_path
        
    def read_text(self):
        """
        Read the content of the config file
        """
        
        file_content = []
        file = open(self.filePath, 'r')
        for line in file:
            file_content.append(line.rstrip())
        file.close()
        return file_content
    
    def delete_line(self, to_remove):
        """
        Delete a specific line from a text file
        """
        
        with open(self.filePath, "r+") as f:
            file_content = f.readlines()
            f.seek(0)
            for i in file_content:
                if not i.__contains__(to_remove):
                    f.write(i)
            f.truncate()
            
    def add_line(self, to_add):
        """
        Add a specific line to text file if not already exists
        """
        
        with open(self.filePath, "r+") as f:
            for line in f:
                if to_add in line:
                    return False
            else:
                f.write(to_add + '\n')
                return True
