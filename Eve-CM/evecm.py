# Autor : Sébastien Duruz
# Date : 30.12.2021

import os
from tkinter import *
from tkinter import ttk
from typing import Counter

def clientOnClick(i):
    os.popen('wmctrl -a "' + eveClients[i] + '"')

# Find the eve clients windows
eveClients = os.popen('wmctrl -l | grep -wv "- Brave\|- Mozilla Firefox"  "EVE - "').read().splitlines()

# Extract the required informations
for i in range(len(eveClients)):
    eveClients[i] = eveClients[i][eveClients[i].find('EVE'):]
    
# Root window (Main Window)
root = Tk()
root.title("Eve Clients Manager")
root.resizable(False, False)
root.attributes('-topmost', True)

# Main Frame
frm = ttk.Frame(root)
frm.grid()

currentCol = 0
currentRow = 0

# Build the actions buttons (one foreach opened client)
for i in range(len(eveClients)):
    # Build the command and the button
    ttk.Button(frm, text=eveClients[i], padding=50, command=lambda i=i: clientOnClick(i)).grid(column=currentCol, row=currentRow)
    # Make the required agencements (MAX 3 buttons on a row)
    currentCol += 1
    if currentCol > 2:
        currentCol = 0
        currentRow += 1

if len(eveClients) < 1:
    ttk.Label(frm, text="No Eve clients detected, please try again.", padding=50).grid(column=currentCol, row=currentRow)

# App main loop
frm.mainloop()

