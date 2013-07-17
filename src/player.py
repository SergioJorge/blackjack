# -*- coding: utf-8 -*-


class Player(object):

    def __init__(self, hand):
        self._hand = hand

    def in_hand(self):
        return self._hand

    def stand(self):
        pass

    def hit(self):
        pass
