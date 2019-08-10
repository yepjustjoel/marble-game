import player
import marble

from colorama import Fore
from colorama import Style

# Board Class
class board:

    # Init
    def __init__(self, playerList):
        # Prepare the game board
        self.board = {"PLAY":{},"BASE":{},"HOME":{}}
        playDict = {}
        baseDict = {}
        homeDict = {}
        for eachPlayer in playerList:
            name = eachPlayer.getName()
            color = eachPlayer.getColor()
            emptyChar = '\u25cb'
            emptyColorChar = self.getDispChar(color, emptyChar)
            fullChar = '\u25cf'
            fullColorChar = self.getDispChar(color, fullChar)
            baseDict[name] = []
            homeDict[name] = []
            playDict[name] = []
            for i in range(4):
                baseDict[name].append({"name":name,"ID":i,"dispChar":fullColorChar,"defaultDispChar":emptyColorChar})
                homeDict[name].append({"name":0,"ID":0,"dispChar":0,"defaultDispChar":emptyColorChar})
            for i in range(18):
                playChar = emptyChar if i else emptyColorChar
                playDict[name].append({"name":0,"ID":0,"dispChar":0,"defaultDispChar":playChar})
        self.board["PLAY"] = playDict
        self.board["BASE"] = baseDict
        self.board["HOME"] = homeDict

    def getDispChar(self,color, char):
        switcher = {
            'black' : f'{Fore.BLACK}{char}{Style.RESET_ALL}',
            'blue' : f'{Fore.BLUE}{char}{Style.RESET_ALL}',
            'cyan' : f'{Fore.CYAN}{char}{Style.RESET_ALL}',
            'green' : f'{Fore.GREEN}{char}{Style.RESET_ALL}',
            'magenta' : f'{Fore.MAGENTA}{char}{Style.RESET_ALL}',
            'red' : f'{Fore.RED}{char}{Style.RESET_ALL}',
            'white' : f'{Fore.WHITE}{char}{Style.RESET_ALL}',
            'yellow' : f'{Fore.YELLOW}{char}{Style.RESET_ALL}'
        }
        return switcher.get(color,f'{char}')

    # Board Display Methods
    def printBoard(self):
        for type,player in self.board.items():
            print(type+":")
            for name,locArray in player.items():
                dispString = name+": "
                for loc in locArray:
                    dispString += loc["dispChar"] if loc["name"] else loc["defaultDispChar"]
                print (dispString)

    # Marble Movers
    def moveMarb(self,type1,name1,idx1,type2,name2,idx2):
        self.board[type2][name2][idx2]["name"] = self.board[type1][name1][idx1]["name"]
        self.board[type2][name2][idx2]["ID"] = self.board[type1][name1][idx1]["ID"]
        self.board[type2][name2][idx2]["dispChar"] = self.board[type1][name1][idx1]["dispChar"]
        self.board[type1][name1][idx1]["name"] = 0
        self.board[type1][name1][idx1]["ID"] = 0
        self.board[type1][name1][idx1]["dispChar"] = 0

    # Get Marb Location
    def getMarb(self,name,id):
        for type,player in self.board.items():
            for sectionName,locArray in player.items():
                i = 0
                for loc in locArray:
                    if (loc["name"]==name) & (loc["ID"]==id):
                        print (type+" "+sectionName+" "+str(i))
                        # return [type,sectionName,locArray.index[loc]]
                    i+=1


