import random
import sys

class Game(object):

    def __init__(self):
        self.cards = [[self.getCard()], [self.getCard(), self.getCard()]]

    def getCard(self):
        random.seed()
        return random.choice(range(2,11))

    def hit(self):
        self.cards[1].append(self.getCard())

    def stand(self):
        player_points = sum(self.cards[1])

        while(player_points >= sum(self.cards[0])):
            self.cards[0].append(self.getCard())

        if (self.lost(self.cards[0])):
            print "Player wins"
        else:
            print "House wins"
        self.printStatus()
        sys.exit(0)
                
    def printStatus(self):
        print "Dealer: ", self.cards[0], sum(self.cards[0])
        print "Player: ", self.cards[1], sum(self.cards[1])

    def lost(self, hands):
        return sum(hands) > 21        

    def getAction(self):
        action = raw_input("Stand [S], Hit [H]? ")
        if action == "S":
            self.stand()
        elif action == "H":
            self.hit()
            if self.lost(self.cards[1]):
                print "House wins"
                self.printStatus()
                sys.exit(0)
        

game = Game()

while(True):
    game.printStatus()
    game.getAction()
