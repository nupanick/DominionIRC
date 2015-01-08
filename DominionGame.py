# This is the central model. It gets called by some sort of controller.

import random # for shuffling

def listCommands():
    """ List the commands the game can parse. """
    commands = "play <card>, buy <card>, end [turn]"

def newGame():
    """ An alias of the constructor. """
    return DominionGame()
    
def defaultOutput(message, player=None):
    """ An example output function. Can be overridden by the caller. """
    if player == None:
        print message
    else:
        print player + ": " + message

class DominionGame:
    """ An object representing a single game of Dominion. """
    
    def __init__(self):
        """ Set up the game. """
        self.players = []
        self.output = defaultOutput
        self.turn = None
        
        # since this is just a test, assume there's only one player.
        self.players.append(Player("Player"))
    
    def start(self):
        """ Begin the game. """
        
        # deal starting decks
        for i in range(7):
            self.players[0].gain("Copper")
        for i in range(3):
            self.players[0].gain("Estate")
        for i in range(5):
            self.players[0].draw()
        
        # announce hands
        self.output(str(self.players[0].hand), self.players[0].name)
                
    def parseInput(self, message, playerName, private=False):
        """ Respond to input from the calling program. """
 
        # Identify the issuing player.
        # TODO: consider moving the players into a dictionary instead,
        #       to save a step here.
        player = None
        for p in self.players:
            if p.name.lower() == playerName.lower():
                # Found the player object!
                player = p
        if player == None:
            # Error: Command issued by player not in the game.
            self.output("Error: You are not currently in the game.", 
                    playerName)
            return
 
        # Accept a string-delimited argument list.
        args = message.split()
        
        # Pick off the main command.
        command = args[0]
        args = args[1:]
        
        self.output("I don't know how to " + command +
                " ".join(args), playerName)
        
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
