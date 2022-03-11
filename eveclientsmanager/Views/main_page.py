# Author : Sébastien Duruz
# Date : 30.12.2021

from Models.json_manipulation import JsonManipulation
from Models.text_manipulation import TextManipulation
from Models.exec_commands import ExecCommands
from Views.blacklist_page import BlacklistPage
import time
import threading
import tkinter as tk
import os


class MainPage:
    """
    Main Page of the Application
    """
    
    blacklist_relative_file_path = '/../blacklist.txt'
    config_relative_file_path = '/../config.json'
    logo_relative_file_path = '/../Resources/logo.png'
    
    def __init__(self):
        """
        Class Constructor
        """

        self.app = None
        self.frm = None
        self.auto_reload_thread = None
        self.settings = JsonManipulation(self.config_relative_file_path).read_json()
        self.blacklistPage = BlacklistPage()
        self.openedClients = list()

        self.build()
    
    def build(self):
        """
        Build the page layout
        """
        
        # Build the page
        self.app = tk.Tk()
        self.app.title("Eve Clients Manager")
        self.app.tk.call('wm', 'iconphoto', self.app._w, tk.PhotoImage(file=os.path.dirname(
            os.path.abspath(__file__)) + self.logo_relative_file_path))
        self.app.resizable(False, False)
        self.app.configure(background="black")
        self.app.attributes('-topmost', True)
        self.app.protocol('WM_DELETE_WINDOW', self.on_close)
        self.frm = tk.Frame(self.app)
        self.frm.grid()

        # Build the menu
        menubar = tk.Menu(self.app)
        client_menu = tk.Menu(menubar)
        client_menu.add_command(label="Reload", command=lambda : self.reload_on_click())
        client_menu.add_command(label="Black list", command=lambda : self.blacklistPage.build())
        menubar.add_cascade(label="Clients", menu=client_menu)
        self.app.config(menu=menubar)

        # Get the clients
        self.build_clients_buttons()

        self.auto_reload_thread = threading.Thread(target=self.auto_reload)
        self.auto_reload_thread.daemon = True
        self.auto_reload_thread.start()
        
        # Enter loop        
        self.frm.mainloop()
    
    def client_on_click(self, client):
        """
        A client as been clicked
        """
        
        ExecCommands.switch_focus(client)

    def build_clients_buttons(self):
        """
        Build the interface buttons with fetched clients
        """
    
        current_col = 0
        current_row = 0
        clients_nb = 0

        self.openedClients = list()

        # Get the clients
        eve_clients = ExecCommands.get_clients()
        blacklist_clients = TextManipulation(self.blacklist_relative_file_path).read_text()
        
        # Build the actions buttons (one foreach opened client)
        for i in range(len(eve_clients)):
            # Check if the clients is currently on blacklist
            if any(eve_clients[i] in str for str in blacklist_clients):
                pass
            else:
                # Build the command and the button
                tk.Button(self.frm, text=eve_clients[i], width=self.settings['card']['width'],
                          height=self.settings['card']['height'],
                          command=lambda i=i: self.client_on_click(eve_clients[i])).grid(
                    column=current_col, row=current_row)
            
                # Make the required agencements determined by the current max clients per row
                current_col += 1
                if current_col > self.settings['row']['max']:
                    current_col = 0
                    current_row += 1
                
                # A button as been built
                clients_nb += 1

                # Add client to openedClientsList (don't recreate buttons if it's not necessary)
                self.openedClients.append(eve_clients[i])
        
        # No clients founded
        if clients_nb < 1:
            tk.Label(self.frm, text="No Eve clients detected, please try again.").grid(
                column=current_col, row=current_row)

    def reload_on_click(self):
        """
        Reload the clients by fetching them again
        """
        
        # Destroy every item before reload
        for child in self.frm.winfo_children():
            child.destroy()
        # Reload the buttons
        self.build_clients_buttons()

    def auto_reload(self):
        """
        Auto reload the client list each X seconds
        """

        while True:
            # Only if a change as been detected
            if self.clients_list_changes():
                # Destroy every item before reload
                for child in self.frm.winfo_children():
                    child.destroy()
                # Reload the buttons
                self.build_clients_buttons()

            # Sleep for desired sec
            time.sleep(10)

    def clients_list_changes(self):
        """
        Check if any change as been made to clients list
        True -> Changes , False -> no changes
        """

        # Get the clients
        eve_clients = ExecCommands.get_clients()
        blacklist_clients = TextManipulation(self.blacklist_relative_file_path).read_text()

        # Check if client is on blacklist, if true remove it from list
        for i in range(len(eve_clients)):
            # Check if the clients is currently on blacklist
            if any(eve_clients[i] in str for str in blacklist_clients):
                continue
            # Check if the client is currently on the Clients Buttons
            if not any(eve_clients[i] in str for str in self.openedClients):
                return True

        # Every client checked, if same number of elements, no changes !
        if len(eve_clients) == len(self.openedClients):
            return False

        # At least one change as been made
        return True


    def on_close(self):
        """
        Clean the others windows on close of the main page
        """
        
        if BlacklistPage.active:
            BlacklistPage.app.destroy()
        
        self.app.destroy()
