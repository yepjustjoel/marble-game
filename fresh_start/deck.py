import collections

# Set up the card named tuple
Card = collections.namedtuple('Card',['rank','suit'])

# Deck Class
class Deck:
    ranks = [str(n) for n in range(2,11)]+list('JQKA')
    suits = 'hearts clubs spades diamonds'.split()

    # Init
    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                                        for rank in self.ranks]

    def __len__(self):
        return len(self._cards)
    def __getitem__(self, position):
        return self._cards[position]
    def __setitem__(self, position, card):
        self._cards[position] = card
