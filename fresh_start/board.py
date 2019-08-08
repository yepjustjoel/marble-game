import player
import deck
import section

# Board Class
class board:

    # Init
    def __init__(self, playersDict):
        self.playerList = []
        self.turn = 0
        self.deck = deck.deck()
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
