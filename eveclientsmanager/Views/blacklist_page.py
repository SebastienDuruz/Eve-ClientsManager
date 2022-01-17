# Author : Sébastien Duruz
# Date : 30.12.2021

from Models.exec_commands import ExecCommands
from Models.text_manipulation import TextManipulation
import tkinter as tk


class BlacklistPage:
    """
    Main Page of the Application
    """

    active = False

    def __init__(self):
        """
        Class Constructor
        """

        self.title = "Eve Clients Manager - Blacklist"
        self.blacklistRelativeFilePath = '/../blacklist.txt'

        self.app = None
        self.frm = None
        self.clientsList = None
        self.blacklist = None
    
    def build(self):
        """
        Build the page layout
        """
        
        if not BlacklistPage.active:
            
            # Force only one page open
            BlacklistPage.active = True
        
            # Build the page
            self.app = tk.Tk()
            self.app.title(self.title)
            self.app.resizable(False, False)
            self.app.attributes('-topmost', True)
            self.app.protocol('WM_DELETE_WINDOW', self.on_close)
            self.frm = tk.Frame(self.app)
            self.frm.grid()
            tk.Label(self.frm, text="Whitelist").grid(column=0, row=0)
            tk.Label(self.frm, text="Blacklist").grid(column=2, row=0)
            tk.Button(self.frm, text="Add / Remove", command=self.add_remove_blacklist_item).grid(column=1, row=1)
            self.build_lists()
                
            # Enter loop        
            self.frm.mainloop()

    def build_lists(self):
        """
        Build the listbox required for using blacklist functionality
        """
        
        # Get the clients
        eve_clients = ExecCommands().get_clients()
        blacklist_clients = TextManipulation(self.blacklistRelativeFilePath).read_text()
        
        # Build the list boxes
        self.clientsList = tk.Listbox(self.frm, width=50, height=10)
        self.clientsList.grid(column=0, row=1)
        self.blacklist = tk.Listbox(self.frm, width=50, height=10)
        self.blacklist.grid(column=2, row=1)
        
        # Populate the lists
        for x in eve_clients:
            if any(x in str for str in blacklist_clients):
                pass
            else:
                self.clientsList.insert(tk.END, x)
        for x in blacklist_clients:
            self.blacklist.insert(tk.END, x)

    def add_remove_blacklist_item(self):
        """
        Apply the modifications to selected blacklist items (add or remove, depend of the selection)
        """
        
        for i in self.clientsList.curselection():
            TextManipulation(self.blacklistRelativeFilePath).add_line(self.clientsList.get(i))
                
        for i in self.blacklist.curselection():
            TextManipulation(self.blacklistRelativeFilePath).delete_line(self.blacklist.get(i))
        
        self.build_lists()
                
    def on_close(self):
        """
        Change the state of the active before closing the page
        """
        
        BlacklistPage.active = False
        self.app.destroy()
    
    



    
