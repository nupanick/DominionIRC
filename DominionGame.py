# This is the central model. It gets called by some sort of view.

import random # for shuffling

def listCommands():
    commands = "play <card>, buy <card>, end [turn]"

def newGame():
    return DominionGame()
    
def log(

class DominionGame:
    """ An object representing a single game of Dominion. """
    
    def __init__(self):
        """ Set up the game. """
        
        # since this is just a test, assume there's only one player.
        players = []
        players.append(Player(0))
        
        # deal the starting decks.
        for i in range(7):
            players[0].gain("Copper")
        for i in range(3):
            players[0].gain("Estate")
        for i in range(5):
            players[0].draw()
        print("Initial deck = " + str(players[0].deck))
        print("Initial hand = " + str(players[0].hand))
        
class Player:
    """ An object representing a player. """
    
    def __init__(self, playerId):
        """ Create a player object. """
        self.playerId = playerId
        self.deck = []
        self.hand = []
        self.discard = []
        self.actionsLeft = 0
        self.buysLeft = 0
        self.moneyLeft = 0
        
    def draw(self):
        """ Causes this Player to draw a card from their deck. """
        
        # Shuffle before drawing, if necessary.
        if len(self.deck) == 0:
            self.deck, self.discard = self.discard, self.deck
            random.shuffle(self.deck)
            
        # Now you can draw the card.
        self.hand.append(self.deck.pop())

    def gain(self, card):
        """ Causes this Player to gain the passed card. """
        self.discard.append(card)
        
