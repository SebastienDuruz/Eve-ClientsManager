# Autor : Sébastien Duruz
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
        eveClients = []
        
        # Extract the required informations
        for i in range(len(clients)):
            eveClients.append(clients[i][clients[i].find('EVE'):])
            
        return eveClients
    
    @staticmethod
    def switch_focus(window):
        """
        Switch the focused windows
        """
        
        # Switch the focus of current window
        os.popen('wmctrl -a "' + window + '"')