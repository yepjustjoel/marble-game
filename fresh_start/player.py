from recordclass import recordclass, RecordClass
import deck

class Player(RecordClass):
    name : str
    color : str
    team : int
    hand : deck.Deck
