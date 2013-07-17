class Card(object):

    def symbol(self):
        pass

    def suit(self):
        pass

    def value(self):
        pass

    def is_visible(self):
        pass


class Player(object):

    def in_hand(self):
        pass

    def stand(self):
        pass

    def hit(self):
        pass


class Human(Player):
    pass


class Dealer(Player):
    pass


class Game(object):

    def __init__(self, players):
        pass
