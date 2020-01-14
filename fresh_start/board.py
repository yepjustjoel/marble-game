import player
import deck
import collections

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
        self.wallLocations = [Location(player.name if not i else None,None) for player in playerList for i in range(18)]

    # Given a player, card, and location - either move a marble or return false
    def moveMarb(self, card, location, basic=True, location2=None):
        # Prepare an individualized game board from the perspective of
        # the current player to make math easier
        playerIdx = self.wallLocations.index(Location(location.marbOwner,None))
        myBoard = self.playLocations[playerIdx:] + self.playLocations[:playerIdx] + self.homeLocations[location.marbOwner]
        # Note here that myWalls includes marbles that are at home, as the same rules apply to those marbles
        myWalls = self.wallLocations[playerIdx:] + self.wallLocations[:playerIdx] + self.homeLocations[location.marbOwner]
        # If it's a "basic" movement, calculate the new position and evaluate
        # whether or not it can be played
        if basic:
            orderedRanks = list('KA')+ [str(n) for n in range(2,11)] + list('Q')
            orderedMoveVals = [-1,1] + [n for n in range(2,11)] + [12]
            moveValDict = dict(zip(orderedRanks,orderedMoveVals))
            moveValDict['4'] = -4 # replace 4 with -4
            # If the requested marble is not currently on the player's board, return false
            try:
                startIdx = myBoard.index(location)
            except ValueError:
                #  raise NotInPlay('Requested marble is not in play')
                return False
            # The marble is on the board, calculate end index and see if there
            # are any problems moving the marble there
            endIdx = startIdx + moveValDict[card.rank]
            print(moveValDict)
            print(endIdx)
            # Test if out of range
            if endIdx >= len(myBoard):
                #  raise OffBoard('Not enough spaces left in the board to play this marble')
                return False
            # Do some special stuff if moving backwards
            if endIdx < startIdx:
                if (startIdx >= len(myBoard)-4): # You can't go backwards from home
                    #  raise NoBackwd('Cannot go backwards from home')
                    return False
                myBoard = myBoard[:-4] # Remove the home locations from the board
            """ Test if there's a wall in between
            Range should not include current marb location (startIdx), but
            must include final marb location (thus endIdx+1), also needs to 
            work for going backwards, hence min/max """
            rangeMin = min(startIdx+1,endIdx)
            rangeMax = max(endIdx+1,startIdx)
            for i in range(rangeMin,rangeMax):
                if myBoard[i].marbOwner and (myBoard[i].marbOwner == myWalls[i].marbOwner):
                    # raise WallOrHome('Wall in the way, or cannot jump over marbles in home')
                    return False
            # Actually move the marbles, sending home if necessary
            endLocation = myBoard[endIdx]
            if (endLocation.marbOwner):
                homeLocations[endLocation.marbOwner][endLocation.marbIdx] = endLocation
                myBoard[endIdx] = Location(None,None)
            myBoard[endIdx],myBoard[startIdx] = myBoard[startIdx],myBoard[endIdx]

            if len(myBoard) > len(self.playLocations):
                self.homeLocations[location.marbOwner]= myBoard[-4:]
            self.playLocations = myBoard[-playerIdx:len(self.playLocations)] + myBoard[:-playerIdx]
            return True
        else :
            if card.rank in 'KA':
                # If the marble is in the base locations, bring it into play
                # and remove any marble that was there
                try:
                    locIdx = self.baseLocations[location.marbOwner].index(location)
                except ValueError:
                    return False
                self.baseLocations[location.marbOwner][locIdx] = Location(None, None)
                playerIdx = self.wallLocations.index(Location(location.marbOwner,None))
                sendToBaseLoc = self.playLocations[playerIdx]
                if (sendToBaseLoc.marbOwner):
                    self.homeLocations[sendToBaseLoc.marbOwner][sendToBaseLoc.marbIdx] = sendToBaseLoc
                self.playLocations[playerIdx] = location
                return True
            elif card.rank in '7':
                return False
            elif card.rank in 'J':
                return False
            else:
                return False

        #  if card.rank in 'KA':
        #      # Secondary usage: bring into play
        #  elif card.rank in '7':
        #      # Secondary usage: moving two marbles in a way that adds to 7
        #  elif card.rank in 'J':
        #      # Primary usage: swapping locations with a marble that's not a wall
        #      # Need to know which marble it will be switching with
    # Board Display Methods
    def printBoard(self):
        emptyChar = '\u25cb'
        fullChar  = '\u25cf'
        # Print base locations
        for player in self.playerList:
            dispString = player.name+": "
            emptyDispChar = self.getDispChar(player.color, emptyChar)
            fullDispChar  = self.getDispChar(player.color, fullChar)
            for loc in self.baseLocations[player.name]:
                dispString += fullDispChar if loc.marbOwner else emptyDispChar
            print(dispString)
        # Print the play board
        charList=[emptyChar for _ in self.playLocations]
        for player in self.playerList:
            for locIdx in range(len(self.playLocations)):
                if self.wallLocations[locIdx].marbOwner == player.name:
                    charList[locIdx] = self.getDispChar(player.color, emptyChar)
                if self.playLocations[locIdx].marbOwner == player.name:
                    charList[locIdx] = self.getDispChar(player.color, fullChar)
        print("".join(charList))
        # Print home locations
        for player in self.playerList:
            dispString = player.name+": "
            emptyDispChar = self.getDispChar(player.color, emptyChar)
            fullDispChar  = self.getDispChar(player.color, fullChar)
            for loc in self.homeLocations[player.name]:
                dispString += fullDispChar if loc.marbOwner else emptyDispChar
            print(dispString)

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
