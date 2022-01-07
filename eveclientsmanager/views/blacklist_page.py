# Autor : Sébastien Duruz
# Date : 30.12.2021

from models.exec_commands import ExecCommands
from models.text_manipulation import TextManipulation
import os
import tkinter as tk

class BlacklistPage:
    """
    Main Page of the Application
    """
    
    title = "Eve Clients Manager - Blacklist"
    
    active = False
    
    blacklistRelativeFilePath = '/../blacklist.txt'
    
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
            
            # Force only one page open
            BlacklistPage.active = True
        
            # Build the page
            BlacklistPage.app = tk.Tk()
            BlacklistPage.app.title(BlacklistPage.title)
            BlacklistPage.app.resizable(False, False)
            BlacklistPage.app.attributes('-topmost', True)
            BlacklistPage.app.protocol('WM_DELETE_WINDOW', BlacklistPage.on_close)
            BlacklistPage.frm = tk.Frame(BlacklistPage.app)
            BlacklistPage.frm.grid()
            tk.Label(BlacklistPage.frm, text="Whitelist").grid(column=0, row=0)
            tk.Label(BlacklistPage.frm, text="Blacklist").grid(column=2, row=0)
            tk.Button(BlacklistPage.frm, text="Add / Remove", command=BlacklistPage.add_remove_blacklist_item).grid(column=1, row=1)
            BlacklistPage.build_lists()
                
            # Enter loop        
            BlacklistPage.frm.mainloop() 
            
    def build_lists():
        """
        Build the listboxes required for using blacklist functionality
        """
        
        # Get the clients
        BlacklistPage.eveClients = ExecCommands().get_clients()
        BlacklistPage.blacklistClients = TextManipulation(BlacklistPage.blacklistRelativeFilePath).read_text()
        
        # Build the list boxes
        BlacklistPage.clientsList = tk.Listbox(BlacklistPage.frm, width=50, height=10)
        BlacklistPage.clientsList.grid(column=0, row=1)
        BlacklistPage.blacklist = tk.Listbox(BlacklistPage.frm, width=50, height=10)
        BlacklistPage.blacklist.grid(column=2, row=1)
        
        # Populate the lists
        for x in BlacklistPage.eveClients:
            if any(x in str for str in BlacklistPage.blacklistClients):
                pass
            else:
                BlacklistPage.clientsList.insert(tk.END, x)
        for x in BlacklistPage.blacklistClients:
            BlacklistPage.blacklist.insert(tk.END, x)
            
    def add_remove_blacklist_item():
        """
        Apply the modifications to selected blacklist items (add or remove, depends of the selection)
        """
        
        for i in BlacklistPage.clientsList.curselection():
                TextManipulation(BlacklistPage.blacklistRelativeFilePath).add_line(BlacklistPage.clientsList.get(i))
                
        for i in BlacklistPage.blacklist.curselection():
                TextManipulation(BlacklistPage.blacklistRelativeFilePath).delete_line(BlacklistPage.blacklist.get(i)) 
        
        BlacklistPage.build_lists()
                
    def on_close():
        """
        Change the state of the active before closing the page
        """
        
        BlacklistPage.active = False
        BlacklistPage.app.destroy()
    
    



    
