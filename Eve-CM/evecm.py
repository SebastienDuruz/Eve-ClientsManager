# Autor : Sébastien Duruz
# Date : 30.12.2021

import os
import json
from tkinter import *
from tkinter import ttk



##
# Config File
##

def read_json(configFilePath):

    # Read the content of the config, return the content
    with open(configFilePath, "r") as jsonContent:
        return json.load(jsonContent)


# read the settings from the json config file
settings = read_json('resources/config.json')


##
# Main Page functions
##

def client_on_click(counter, clients):
    
    # Switch the current focused client
    os.popen('wmctrl -a "' + clients[counter] + '"')
    

def load_clients():

    # Find the eve clients windows
    clients = os.popen('wmctrl -l | grep "EVE - "').read().splitlines()

    # Extract the required informations
    for i in range(len(clients)):
        clients[i] = clients[i][clients[i].find('EVE'):]
        
    return clients


def build_clients_buttons():
 
    currentCol = 0
    currentRow = 0
    
    # Get the clients
    eveClients = load_clients()

    # Build the actions buttons (one foreach opened client)
    for i in range(len(eveClients)):
        
        # Build the command and the button
        ttk.Button(frm, text=eveClients[i], padding=settings['card']['padding'], width=settings['card']['width'], command=lambda i=i: client_on_click(i, eveClients)).grid(column=currentCol, row=currentRow)
        
        # Make the required agencements (MAX 3 buttons on a row)
        currentCol += 1
        if currentCol > 2:
            currentCol = 0
            currentRow += 1

    # No clients as been found
    if len(eveClients) < 1:
        ttk.Label(frm, text="No Eve clients detected, please try again.", padding=settings['card']['padding']).grid(column=currentCol, row=currentRow)
    

def reload_on_click(frm):
    
    # Destroy every item before reload
    for child in frm.winfo_children():
        child.destroy()
        
    # Reload the buttons
    build_clients_buttons()



##
# Start Logic
##
    
# app window (Main Window)
app = Tk()
app.title("Eve Clients Manager")
app.tk.call('wm', 'iconphoto', app._w, PhotoImage(file='resources/logo.png'))
app.resizable(False, False)
app.attributes('-topmost', True)

# Main Frame
frm = ttk.Frame(app)
frm.grid()

# Main Menu
menubar = Menu(app)
clientMenu = Menu(menubar)
clientMenu.add_command(label="Reload", command=lambda : reload_on_click(frm))
menubar.add_cascade(label="Clients", menu=clientMenu)
app.config(menu=menubar)

# Build the initial clients buttons
build_clients_buttons()


# App main loop
frm.mainloop()  

