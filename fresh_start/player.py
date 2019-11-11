import card
import location

# Player Class
class player:

    # Init
    def __init__(self, name, color, team):
        self.name = name
        self.color = color
        self.team = team
        self.hand = []
        self.baseLocs = []
        for i in range(4):
            self.baseLocs.append(location.location(True))
        self.playLocs = []
        for i in range(18):
            self.playLocs.append(location.location(False))
        self.homeLocs = []
        for i in range(4):
            self.homeLocs.append(location.location(False))

    # Setters
    def setName(self, name):
        self.name = name

    # Getters
    def getName(self):
        return self.name
    def getTeam(self):
        return self.team
    def getColor(self):
        return self.color
    def getHandLen(self):
        return len(self.hand)

    # Card Methods
    def addCard(self,newCard):
        self.hand.append(newCard)
    def printHand(self):
        for myCard in self.hand:
            print(str(self.hand.index(myCard)) + ": " + myCard.getValue() + " of " + myCard.getSuit())
    def getCard(self,cardIdx):
        return self.hand.pop(cardIdx)
    def clearHand(self):
        self.hand = []
