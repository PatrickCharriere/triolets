
from TokenBag import TokenBag
from Board import Board, Coordinates
from Player import Player
from Constants import *
from random import *
import time
import os

class Game:
    currentPlayer = 0
    tokenBag = TokenBag()
    players = []
    board = Board()

    def __init__(self, playersQty):
        self.playersQty = playersQty
        for i in range(playersQty):
            self.players.append(Player(randomNames[i]))
    
    def initialise(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        #print("Bienvenue pour une nouvelle partie de Triolets.")
        #print("Ce jeu est configuré pour " + str(self.playersQty) + " joueurs, " + self.players[0].name + " et " + self.players[1].name + ".")
        #self.tokenBag.print()
        self.players[0].drawTokensFromTokenBag(self.tokenBag, 3)
        self.players[1].drawTokensFromTokenBag(self.tokenBag, 3)
        #self.board.print()

    def start(self):
        #print('Selection aléatoire du premier joueur...')
        self.currentPlayer = self.selectRandomPlayerToStart()
        print('Joueur ' + self.players[self.currentPlayer].name + ' commence.')
        self.turn()
        return
    
    def selectRandomPlayerToStart(self):
        return randrange(0, self.playersQty)
    
    def turn(self):
        self.players[self.currentPlayer].tokenStand.print()
        while True:
            try:
                selection = int(input(self.players[self.currentPlayer].name + ' choisissez un pion a jouer parmi votre chevalet (1, 2 ou 3):'))
                break
            except:
                print("Cette option n'est pas valide")

        if selection != 1 & selection != 2 & selection != 3:
            print("Cette option n'est pas valide")
            
        
        currentSelection = Coordinates(7, 7)
        while True:
            #print("Selectionnez où positioner votre jeton sur le plateau")
            #self.board.print(currentSelection)
            #time.sleep(.5)
            #os.system('cls' if os.name == 'nt' else 'clear')
            #print("Selectionnez où positioner votre jeton sur le plateau")
            #self.board.print()
            #time.sleep(.5)
            #os.system('cls' if os.name == 'nt' else 'clear')
            1
