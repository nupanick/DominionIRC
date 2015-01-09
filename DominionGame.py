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
        self.output = defaultOutput     # Output method hook.
        self.players = {}       # Players, indexed by name.
        self.turns = []         # Players, sorted by turn order.
        self.turn = 0           # Increments each turn.
        self.isRunning = False  # Flag indicating if game is started.
        
        # since this is just a test, assume there's only one player.
        #self.players.append(Player("Player"))
    
    def start(self):
        """ Begin the game. """
        # We're not running yet, right? That would be silly.
        if self.isRunning:
            self.output("Error: Game already started.")
            return
        
        # deal starting decks
        for p in self.turns:
            for i in range(7):
                p.gain("Copper")
            for i in range(3):
                p.gain("Estate")
            for i in range(5):
                p.draw()  # This will automatically
                                        # shuffle the deck anyway.
        
        # announce hands
        for p in self.turns:
            self.output(str(p.hand), p.name)
            
        # and we're rolling!
        self.isRunning = True
        
    def join(self, playerName):
        """ Request to join the game. Note that a new player cannot
            join a game in progress. """
            
        if self.isRunning:
            self.output("Error: You cannot join a game in progress!")
        elif playerName.lower() in self.players.keys():
            self.output("Error: You are already in this game!")
        else:
            p = Player(playerName)
            self.players[playerName.lower()] = p
            self.turns.append(p)
            self.output(playerName + " joined the game.")
                
    def parseInput(self, message, playerName, private=False):
        """ Respond to input from the calling program. """
        
        # Accept a string-delimited argument list.
        args = message.split()
        
        # Pick out the main command.
        command = args[0].lower()
        args = args[1:]
        
        # If it's a new player, try to add them and then quit early.
        if command == "join":
            self.join(playerName)
            return
 
        # Otherwise, identify the existing player.
        player = None
        for p in self.players.keys():
            if p.lower() == playerName.lower():
                # Found the player object!
                player = self.players[p]
        if player == None:
            self.output("Error: You are not currently in the game.", 
                    playerName)
            return
 
        # We've found the player and they're not new. What are they
        # trying to do?
        command = command.lower()
        if command == "start":
            self.start()
        else:
            # We've tried everything and nothing worked. Just complain.
            self.output("I don't know how to " + message, playerName)
        
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
