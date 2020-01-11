import player
import deck
import board
import random

# Game Class
class Game:

    # Init
    def __init__(self, playerList):
        # Take player list input and order it so team members are spaced every-other
        sortedPlayers = sorted(playerList, key=lambda player: player.team) # Sort by team e.g. 1,1,1,2,2,2
        numPlayers = len(playerList)
        everyOtherSlices = [slice(i,None,numPlayers//2) for i in range(numPlayers//2)] # Each slice has a player from both teams
        self.playerList = [player for pairSlice in everyOtherSlices
                                  for player in sortedPlayers[pairSlice]] # Combine all slices to make ordered list
        self.turn = 0
        self.deck = deck.Deck()
        random.shuffle(self.deck)
        self.board = board.Board(self.playerList)
        # self.board.printBoard()

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
    def printHand(self,player):
        print(player.getName()+"'s hand is:")
        player.printHand()

    # Gameplay functions
    def playGame(self):
        while (True):
            self.dealHands()
            # while (True):
            for i in range(len(self.playerList)*self.getCurrentPlayer().getHandLen()):
                self.printCurrentPlayer()
                currentPlayer = self.getCurrentPlayer()
                self.printHand(currentPlayer)
                # Prompt for card to play
                canPlay = True if (input("Can you play? (y/n) ")=="y") else False
                if (canPlay):
                    cardIdx = int(input("Enter card index: "))
                    marbIdx = int(input("Enter marb index: "))
                    # Play card
                    self.board.playCard(currentPlayer.getName(),marbIdx,currentPlayer.getCard(cardIdx).getValue())
                else:
                    currentPlayer.clearHand()
                # Show board
                self.board.printBoard()
                # Next player
                self.nextTurn()


