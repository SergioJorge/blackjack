import unittest

from game import Game

class GameTestCase(unittest.TestCase):

    def setUp(self):
        self.game = Game()

    def testShouldStarte(self):
        self.assertEqual(len(self.game.cards[0]), 1)
        self.assertEqual(len(self.game.cards[1]), 2)

    def testShouldReceiveCard(self):
        card = self.game.getCard()
        self.assertTrue(card >= 2 and card <= 10)
    
    def testHit(self):
        self.game.hit()
        self.assertEqual(len(self.game.cards[1]), 3)
 
    def testStand(self):
        self.game.stand()
        self.assertTrue(sum(self.game.cards[0]) > sum(self.game.cards[1]))
    
    def testShouldPrintGameStatus(self):
        self.game.getStatus()

    def test_lost(self):
        self.assertFalse(lost([2,10])

if __name__ == '__main__':
    unittest.main()
