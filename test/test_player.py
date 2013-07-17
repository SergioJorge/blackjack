import unittest

from card import Card
from player import Player


class PlayerTestCase(unittest.TestCase):

    def test_in_hand(self):
        hand = [Card(), Card()]
        p = Player(hand)
        self.assertEqual(hand, p.in_hand())
