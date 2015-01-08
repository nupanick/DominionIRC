# python 2, because Twisted and stuff I guess.
# for now: just respond to basic input from the console!

import random # for shuffling
import DominionGame

def customOutput(message, player=None):
    if player == None:
        print message
    else:
        print player + ": " + message

game = DominionGame.newGame()
game.output = customOutput
game.start()
while True:
    msg = raw_input("> ")
    if msg == "quit":
        break
    if msg.startswith("!"):
        game.parseInput(msg[1:], "Player")
