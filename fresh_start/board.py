import player
import deck
import collections
from recordclass import recordclass

from colorama import Fore
from colorama import Style

Location = collections.namedtuple('Location', 'marbOwner marbIdx')

# Board Class
# Needs to do 3 things:
#  - Be a record of current and past states of the gameboard
#  - Be able to display itself
#  - Take a card, player, and marble ID either play the card or reject it as an invalid play
class Board:

    # Init
    def __init__(self, playerList):
        # Prepare the game board
        self.playerList = playerList
        self.playLocations = [Location(None,None) for player in playerList for i in range(18)]
        self.baseLocations = {player.name : [Location(player.name,i) for i in range(4)] for player in playerList}
        self.homeLocations = {player.name : [Location(None,None) for i in range(4)] for player in playerList}
        self.wallLocations = [Location(player if not i else None,None) for player in playerList for i in range[18]]

    # Given a player, card, and location - either move a marble or return false
    def moveMarb(self, card, location, basic=True, location2=None):
        # Prepare an individualized game board from the perspective of
        # the current player to make math easier
        playerIdx = self.playLocations.index(location.marbOwner)
        myBoard = self.playLocations[playerIdx:] + self.playLocations[0:playerIdx] + self.homeLocations[location.marbOwner]
        # Note here that myWalls includes marbles that are at home, as the same rules apply to those marbles
        myWalls = self.wallLocations[playerIdx:] + self.wallLocations[0:playerIdx] + self.homeLocations[location.marbOwner]
        # If it's a "basic" movement, calculate the new position and evaluate
        # whether or not it can be played
        if basic:
            orderedRanks = ['KA'] + [str(n) for n in range(2,11)] + list('Q')
            orderedMoveVals = [-1,1] + [n for n in range(2,11)] + [12]
            moveValDict = dict(zip(orderedRanks,orderedMoveVals))
            moveValDict['4'] = -4 # replace 4 with -4
            # If the requested marble is not currently on the player's board, return false
            try:
                startIdx = myBoard.index(location)
            except ValueError:
                return False
            # The marble is on the board, calculate end index and see if there
            # are any problems moving the marble there
            endIdx = startIdx + moveValDict[card.rank]
            endIdx = endIdx - 4 if endIdx<0 else endIdx
            # Test if out of range
            if endIdx >= len(myBoard):
                return false
            # Test if there's a wall in between
            # Range should not include current marb location (startIdx), but
            # must include final marb location (thus endIdx+1)
            for i in range(startIdx+1,endIdx+1):
                if myBoard[i].marbOwner == myWalls[i].marbOwner:
                    return false
            endLocation = myBoard[endIdx]
            elif myBoard[endIdx]
            try:
                myBoard[endIdx] = myBoard[startIdx]
            if location not in myBoard:
                return false

        #  if card.rank in 'KA':
        #      # Primary usage: bring into play
        #      # Secondary usage: move backwards or forwards
        #  elif card.rank in '23568910Q':
        #      # Primary usage: moving a marble by a value
        #  elif card.rank in '7':
        #      # Primary usage: moving a marble by 7
        #      # Secondary usage: moving two marbles in a way that adds to 7
        #  elif card.rank in 'J':
        #      # Primary usage: swapping locations with a marble that's not a wall
        #      # Need to know which marble it will be switching with
        #  elif card.rank in '4':
        #      # Primary usage: moving a marble back by 4
        #  return true
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
                        return [type,sectionName,i]
                    i+=1

    # Playing a card
    def sendToBase(self,sectionName,idx):
        marbOwner = self.board["PLAY"][sectionName][idx]["name"]
        marbID = self.board["PLAY"][sectionName][idx]["ID"]
        if (marbOwner):
            self.moveMarb("PLAY",sectionName,idx,"BASE",marbOwner,marbID)
    def bringIntoPlay(self,name):
        self.sendToBase(name,0)
        for i in range(4):
            locInfo = self.board["BASE"][name][i]
            if locInfo["name"]:
                break
        self.moveMarb("BASE",name,i,"PLAY",name,0)
    def calcNewLoc(self,name,id,value):
        [type,sectionName,idx] = self.getMarb(name,id)
        endIdx = idx+value
        if (endIdx>17)|(endIdx<0):
            sectionsAdded = endIdx//18
            endIdx = endIdx%18
            sectionIdx = self.playerOrder.index(sectionName)
            sectionIdx = (sectionIdx+sectionsAdded)%len(self.playerOrder)
            sectionName = self.playerOrder[sectionIdx]
            if (sectionName == name)&(value>0):
                type = "HOME"
        return [type,sectionName,endIdx]
    def moveMarbByValue(self,name,id,value):
        [type,sectionName,idx] = self.getMarb(name,id)
        [endType,endSectionName,endIdx] = self.calcNewLoc(name,id,value)
        self.sendToBase(endSectionName,endIdx)
        self.moveMarb(type,sectionName,idx,endType,endSectionName,endIdx)
    def playCard(self,name,id,card):
        if card in ["2","3","5","6","8","9","10"]:
            self.moveMarbByValue(name,id,int(card))
        elif card in ["Q"]:
            self.moveMarbByValue(name,id,12)
        elif card in ["4"]:
            self.moveMarbByValue(name,id,-4)
        elif card in ["A","K"]:
            self.bringIntoPlay(name)

        #  emptyChar = '\u25cb'
        #  emptyColorChar = self.getDispChar(color, emptyChar)
        #  fullChar = '\u25cf'
        #  fullColorChar = self.getDispChar(color, fullChar)

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

# To play a card:
#  - 
