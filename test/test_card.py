import unittest

from card import Card, CLUBS, HEARTS, DIAMONDS, SPADES, new_deck

class TestCard(unittest.TestCase):
    
    def setUp(self):
        self.card = Card(1, CLUBS)
        
    def testShouldHaveASuit(self):
        self.assertEqual(self.card.suit, CLUBS)

    def testShouldHaveASymbol(self):
        self.assertEqual(self.card.symbol, 1)

    def testNewValidDeck(self):
        deck = new_deck()
        self.assertEqual(len(deck), 52)


if __name__ == '__main__':
    unittest.main()
