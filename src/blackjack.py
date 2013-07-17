# -*- coding: utf-8 -*-


class Card(object):

    def symbol(self):
        pass

    def suit(self):
        pass

    def value(self):
        pass

    def is_visible(self):
        pass
    
class Human(Player):
    pass


class Dealer(Player):
    pass


class Game(object):

    def __init__(self, players):
        pass
