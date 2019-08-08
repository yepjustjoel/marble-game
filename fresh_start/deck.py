import random
import card

# Deck Class
class deck:

    # Init
    def __init__(self):
        suits = ["hearts","clubs","spades","diamonds"]
        cardValues = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
        self.cardDeck = []
        for suit in suits:
            for val in cardValues:
                self.cardDeck.append(card.card(suit,val))
        self.shuffleDeck()

    # Methods
    def getNumRemainingCards(self):
        return len(self.cardDeck)
    def popCard(self):
        return self.cardDeck.pop()
    def shuffleDeck(self):
        random.shuffle(self.cardDeck)