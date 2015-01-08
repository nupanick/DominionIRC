# python 2, because Twisted and stuff I guess.
# for now: just respond to basic input from the console!

import random # for shuffling
import DominionGame

def customOutput(message, player=None):
    if player == None:
        print "PUBLIC: " + message
    else:
        print player + ": " + message

game = DominionGame.newGame()
game.output = customOutput
game.start()


"""
player = "player"
deck = ["Copper", "Copper", "Copper", "Copper", "Copper", 
        "Copper", "Copper", "Estate", "Estate", "Estate", ]
discard = []
hand = []
    
random.shuffle(deck)
    
while True:
    
    for i in range(5):
        if len(deck) == 0:
            deck, discard = discard, deck
            random.shuffle(deck)
        hand.append(deck.pop())
    
    print "Your hand: " + str(hand)
    print "Cards in deck: " + len(deck)
    print "Cards in discard:" + len(discard)
    
    msg = raw_input(player + ": ")
    
    if msg == "quit":
        break
    else:
        if msg == "!buy Estate":
            discard.append("Estate")
        elif msg == "!buy Copper":
            discard.append("Copper")
    
    while len(hand) > 0:
        discard.append(hand.pop())
"""

    
