
from Constants import *
from Token import Token
from TokenBag import TokenBag
from Board import Board
from Player import Player

class Game:
    tokenBag = TokenBag()
    players = []
    board = Board()

    def __init__(self, playersQty):
        self.playersQty = playersQty
        for i in range(playersQty):
            self.players.append(Player(randomNames[i]))
    
    def initialise(self):
        print("Bienvenue pour une nouvelle partie de Triolets.")
        print("Ce jeu est configuré pour " + str(self.playersQty) + " joueurs, " + self.players[0].name + " et " + self.players[1].name + ".")
        self.players[0].drawTokensFromTokenBag(self.tokenBag, 3)
        self.players[1].drawTokensFromTokenBag(self.tokenBag, 3)
        self.tokenBag.print()
        self.board.printBoard()

    def start(self):

        return


game = Game(2)
game.initialise()
game.start()
