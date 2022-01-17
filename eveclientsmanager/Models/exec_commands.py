# Author : Sébastien Duruz
# Date : 03.01.2022

import os


class ExecCommands:
    """
    Class ExecCommands : Execute Linux commands
    """   
    
    @staticmethod
    def get_clients():
        """
        Get the opened Eve Clients
        """
        
        clients = os.popen('wmctrl -l | grep "EVE - "').read().splitlines()
        eve_clients = []
        
        # Extract the required information
        for i in range(len(clients)):
            eve_clients.append(clients[i][clients[i].find('EVE'):])
            
        return eve_clients
    
    @staticmethod
    def switch_focus(window):
        """
        Switch the focused windows
        """
        
        # Switch the focus of current window
        os.popen('wmctrl -a "' + window + '"')
