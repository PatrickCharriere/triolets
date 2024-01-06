from TokenStand import TokenStand
from TokenBag import TokenBag
from array import *

class Player:
    tokenStand: TokenStand
    points = 0
    def __init__(self, name):
        self.name = name

    def drawTokensFromTokenBag(self, tokenBag: TokenBag, qty):
        self.tokenStand = TokenStand(tokenBag.draw(qty))
        #self.tokenStand.print()