# This is the central model. It gets called by some sort of view.

import random # for shuffling

def listCommands():
    commands = "play <card>, buy <card>, end [turn]"

def newGame():
    return DominionGame()
    
def defaultOutput(message, player=None):
    print player, message

class DominionGame:
    """ An object representing a single game of Dominion. """
    
    def __init__(self):
        """ Set up the game. """
        self.players = []
        self.output = defaultOutput
        
        # since this is just a test, assume there's only one player.
        self.players.append(Player("Player"))
    
    def start(self):
        # deal the starting decks.
        for i in range(7):
            self.players[0].gain("Copper")
        for i in range(3):
            self.players[0].gain("Estate")
        for i in range(5):
            self.players[0].draw()
        self.output("Initial deck = " + str(self.players[0].deck))
        self.output("Initial hand = " + str(self.players[0].hand),
                self.players[0].name)
        
class Player:
    """ An object representing a player. """
    
    def __init__(self, name):
        """ Create a player object. """
        self.name = name
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
        
