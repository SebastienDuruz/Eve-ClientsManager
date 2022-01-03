# Autor : Sébastien Duruz
# Date : 30.12.2021

import os
from models.json_manipulation import JsonManipulation
from models.exec_commands import ExecCommands
from tkinter import *
from tkinter import ttk

from views.blacklist_page import BlacklistPage


class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class MainPage(metaclass=Singleton):
    """
    Main Page of the Application
    """
    
    def __init__(self):
        """
        Class Constructor
        """
        
        MainPage.build()
        
    def build():
        """
        Build the page layout
        """
        
        # Intanciation of the required objects
        MainPage.settings = JsonManipulation('config.json').read_json()
        MainPage.blacklistPage = BlacklistPage()
    
        # Build the page
        MainPage.app = Tk()
        MainPage.app.title("Eve Clients Manager")
        MainPage.app.tk.call('wm', 'iconphoto', MainPage.app._w, PhotoImage(file='resources/logo.png'))
        MainPage.app.resizable(False, False)
        MainPage.app.attributes('-topmost', True)
        MainPage.frm = ttk.Frame(MainPage.app)
        MainPage.frm.grid()

        # Build the menu
        menubar = Menu(MainPage.app)
        clientMenu = Menu(menubar)
        clientMenu.add_command(label="Reload", command=lambda : MainPage.reload_on_click())
        clientMenu.add_command(label="Black list", command=lambda : MainPage.blacklistPage.build())
        menubar.add_cascade(label="Clients", menu=clientMenu)
        MainPage.app.config(menu=menubar)

        # Get the clients
        MainPage.build_clients_buttons()
        
        # Enter loop        
        MainPage.frm.mainloop() 
    
    def client_on_click(client):
        """
        A client as been clicked
        """
        
        ExecCommands.switch_focus(client)

    def build_clients_buttons():
        """
        Build the interface buttons with fetched clients
        """
    
        currentCol = 0
        currentRow = 0
        
        # Get the clients
        eveClients = ExecCommands.get_clients()
        
        # Build the actions buttons (one foreach opened client)
        for i in range(len(eveClients)):
        
            # Build the command and the button
            ttk.Button(MainPage.frm, text=eveClients[i], padding=MainPage.settings['card']['padding'], width=MainPage.settings['card']['width'], command=lambda i=i: MainPage.client_on_click(eveClients[i])).grid(column=currentCol, row=currentRow)
        
            # Make the required agencements determined by the current max clients per row
            currentCol += 1
            if currentCol > MainPage.settings['row']['max']:
                currentCol = 0
                currentRow += 1
        
        # No clients founded
        if len(eveClients) < 1:
            ttk.Label(MainPage.frm, text="No Eve clients detected, please try again.", padding=MainPage.settings['card']['padding']).grid(column=currentCol, row=currentRow)

    def reload_on_click():
        """
        Reload the clients by fetching them again
        """
        
        # Destroy every item before reload
        for child in MainPage.frm.winfo_children():
            child.destroy()
        # Reload the buttons
        MainPage.build_clients_buttons()
