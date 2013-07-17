# -*- coding: utf-8 -*-

import unittest
from player import Player


class TestPlayer(unittest.TestCase):

    def test_should_have_a_instance_of_player(self):
        player = Player()
        self.assertTrue(player)
    

if __name__ == "__main__":
    unittest.main()
