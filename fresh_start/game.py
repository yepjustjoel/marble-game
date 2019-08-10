import player
import deck
import section
import marble
import board

# Game Class
class game:

    # Init
    def __init__(self, playersDict):
        self.playerList = []
        self.turn = 0
        self.deck = deck.deck()
        # Set up the players in an ordered list every other by team
        unSortedPlayerList = []
        for name,attr in playersDict.items():
            unSortedPlayerList.append(player.player(name,attr[0],attr[1]))
        t1Idx=0;
        t2Idx=1;
        sortedPlayerList = []
        for i in range(len(unSortedPlayerList)):
            sortedPlayerList.append(None)
        for aPlayer in unSortedPlayerList:
            if (aPlayer.getTeam() == 1):
                sortedPlayerList[t1Idx] = aPlayer
                t1Idx += 2
            elif (aPlayer.getTeam() == 2):
                sortedPlayerList[t2Idx] = aPlayer
                t2Idx += 2
        self.playerList = sortedPlayerList
        self.board = board.board(self.playerList)
        self.board.printBoard()
        # Prepare the game board
        self.playLocs = []
        self.baseLocs = {}
        self.homeLocs = {}
        for eachPlayer in self.playerList:
            name = eachPlayer.getName()
            self.baseLocs[name] = []
            for i in range(4):
                self.baseLocs[name].append(marble.marble(True,eachPlayer,i))
            self.homeLocs[name] = []
            for i in range(4):
                self.homeLocs[name].append(marble.marble(False))
            for i in range(18):
                self.playLocs.append(marble.marble(False))


    # Setters
    def nextTurn(self):
        self.turn = self.turn+1 if self.turn<len(self.playerList)-1 else 0


    # Getters
    def getAllPlayerNames(self):
        nameList = []
        for player in self.playerList:
            nameList.append(player.getName())
        return nameList
    def getPlayers(self):
        return self.playerList
    def getCurrentPlayer(self):
        return self.playerList[self.turn]
    def getDeck(self):
        return self.deck
    def getBoard(self):
        return self.board

    # Printers
    def printCurrentPlayer(self):
        print ("Current player is: "+self.getCurrentPlayer().getName())

    # Card Methods
    def dealHands(self):
        for player in self.playerList:
            for i in range(5):
                player.addCard(self.deck.popCard())
    def printHands(self):
        for player in self.playerList:
            print(player.getName()+"'s hand is:")
            player.printHand()

    # Marble Methods
    def getMarbleLocation(self, player, idx):
        for loc in self.playLocs:
            if (loc.getMarbId()==idx) & (loc.getPlayerName()==player.getName()):
                return 0
    # def moveMarble(self, loc1, loc2):
        
    # Board Display Methods
    def printBoard(self):
        print("Play Board")
        boardText=""
        for loc in self.playLocs:
            boardText+=loc.getDispChar()
        print(boardText)
        for player in self.playerList:
            name = player.getName()
            baseStr = ""
            homeStr = ""
            for loc in self.baseLocs[name]:
                baseStr+=loc.getDispChar()
            for loc in self.homeLocs[name]:
                homeStr+=loc.getDispChar()
            print(name + "'s home: " + homeStr)
            print(name + "'s base: " + baseStr)

            
