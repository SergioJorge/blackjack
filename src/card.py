CLUBS = u"\u2663"
HEARTS = u"\u2665"
DIAMONDS = u"\u2666"
SPADES = u"\u2660"

suits = [CLUBS, HEARTS, DIAMONDS, SPADES]


class Card(object):

    def __init__(self, symbol, suit):
        self.symbol = symbol
        self.suit = suit


def new_deck():
    deck = []
    
    symbols = [str(value) for value in range(2,11)] + ['J', 'Q', 'K', 'A']

    for symbol in symbols:
        for suit in suits:
            deck.append(Card(symbol, suit))

    return deck
