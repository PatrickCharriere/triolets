
from unittest import TestCase
from Board import Board, Coordinates

class Test(TestCase):
    def test(self):
        board = Board()
        coordinates = Coordinates(0, 0)
        self.assertEqual(board.getSquareValue(coordinates), '.')
        coordinates = Coordinates(7, 0)
        self.assertEqual(board.getSquareValue(coordinates), 'R')
        #self.assertEqual(board.getSquare(7 ,0), 'R')