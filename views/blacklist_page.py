# Autor : Sébastien Duruz
# Date : 30.12.2021

import os
from models.exec_commands import ExecCommands
from models.json_manipulation import JsonManipulation
from tkinter import *
from tkinter import ttk

class BlacklistPage:
    """
    Main Page of the Application
    """
    
    title = "Eve Clients Manager - Blacklist"
    
    active = False
    
    @staticmethod
    def __init__():
        """
        Class Constructor
        """
        
        pass
    
    @staticmethod
    def build():
        """
        Build the page layout
        """
        if BlacklistPage.active == False:
            # Intanciation of the required objects
            BlacklistPage.settings = JsonManipulation('config.json').read_json()
        
            # Build the apge
            BlacklistPage.app = Tk()
            BlacklistPage.app.title(BlacklistPage.title)
            BlacklistPage.app.resizable(False, False)
            BlacklistPage.frm = ttk.Frame(BlacklistPage.app)
            BlacklistPage.frm.grid()
            
            ttk.Label(BlacklistPage.frm, text="Work in progress", padding=100).grid(column=0, row=0)

            BlacklistPage.active = True
            
            # Enter loop        
            BlacklistPage.frm.mainloop() 
        
    def close():
        """
        Close the window if signal send
        """
        
        BlacklistPage.app.destroy()
    
    



    
