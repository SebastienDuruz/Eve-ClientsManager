# Autor : Sébastien Duruz
# Date : 30.12.2021

import os
from tkinter import *
from tkinter import ttk


def clientOnClick(counter, clients):
    
    # Switch the current focused client
    os.popen('wmctrl -a "' + clients[counter] + '"')
    

def loadClients():

    # Find the eve clients windows
    clients = os.popen('wmctrl -l | grep "EVE - "').read().splitlines()

    # Extract the required informations
    for i in range(len(clients)):
        clients[i] = clients[i][clients[i].find('EVE'):]
        
    return clients


def buildClientsButtons():
 
    currentCol = 0
    currentRow = 0
    
    # Get the clients
    eveClients = loadClients()

    # Build the actions buttons (one foreach opened client)
    for i in range(len(eveClients)):
        
        # Build the command and the button
        ttk.Button(frm, text=eveClients[i], padding=50, command=lambda i=i: clientOnClick(i, eveClients)).grid(column=currentCol, row=currentRow)
        
        # Make the required agencements (MAX 3 buttons on a row)
        currentCol += 1
        if currentCol > 2:
            currentCol = 0
            currentRow += 1

    # No clients as been found
    if len(eveClients) < 1:
        ttk.Label(frm, text="No Eve clients detected, please try again.", padding=50).grid(column=currentCol, row=currentRow)
    

def reloadOnClick(frm):
    
    # Destroy every item before reload
    for child in frm.winfo_children():
        child.destroy()
        
    # Reload the buttons
    buildClientsButtons()
    
    
# app window (Main Window)
app = Tk()
app.title("Eve Clients Manager")
app.tk.call('wm', 'iconphoto', app._w, PhotoImage(file='resources/logo.png'))
app.resizable(False, False)
app.attributes('-topmost', True)
app.lift()

# Main Frame
frm = ttk.Frame(app)
frm.grid()

# Main Menu
menubar = Menu(app)
clientMenu = Menu(menubar)
clientMenu.add_command(label="Reload", command=lambda : reloadOnClick(frm))
menubar.add_cascade(label="Clients", menu=clientMenu)
app.config(menu=menubar)


# Build the initial clients buttons
buildClientsButtons()

# App main loop
frm.mainloop()  

