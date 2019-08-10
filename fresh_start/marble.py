import player

from colorama import Fore
from colorama import Style

# Marble Class
class marble:

    # Init
    def __init__(self, isPlayerMarb, marbOwner=None, marbId=0):
        self.isPlayerMarb = isPlayerMarb
        self.marbId = marbId
        if (self.isPlayerMarb):
            self.player = marbOwner

    # Setters
    # def setLocation(self, newSection, newLocation, newType):
    #     self.currSection = newSection
    #     self.currLocation = newLocation
    #     self.currType = newType

    # Getters
    def getPlayerName(self):
        return self.player.getName() if (self.isPlayerMarb) else 0
    def getTeam(self):
        return self.player.getTeam() if (self.isPlayerMarb) else 0
    def getColor(self):
        return self.player.getColor() if (self.isPlayerMarb) else 0
    def getMarbId(self):
        return self.marbId
    def getDispChar(self):
        color = self.getColor()
        empty = '\u25cb'
        full = '\u25cf'
        switcher = {
            'black' : f'{Fore.BLACK}{full}{Style.RESET_ALL}',
            'blue' : f'{Fore.BLUE}{full}{Style.RESET_ALL}',
            'cyan' : f'{Fore.CYAN}{full}{Style.RESET_ALL}',
            'green' : f'{Fore.GREEN}{full}{Style.RESET_ALL}',
            'magenta' : f'{Fore.MAGENTA}{full}{Style.RESET_ALL}',
            'red' : f'{Fore.RED}{full}{Style.RESET_ALL}',
            'white' : f'{Fore.WHITE}{full}{Style.RESET_ALL}',
            'yellow' : f'{Fore.YELLOW}{full}{Style.RESET_ALL}'
        }
        return switcher.get(color,f'{empty}')

