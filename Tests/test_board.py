
from unittest import TestCase
from Board import Board, Coordinates

class Test(TestCase):
    def test_special_cases(self):
        print(self._testMethodName)
        board = Board()
        coordinates = Coordinates(7, 0)
        self.assertEqual(board.getSquareValue(coordinates), 'R')
        coordinates = Coordinates(7, 14)
        self.assertEqual(board.getSquareValue(coordinates), 'R')
        coordinates = Coordinates(7, 7)
        self.assertEqual(board.getSquareValue(coordinates), '2')
        coordinates = Coordinates(10, 13)
        self.assertEqual(board.getSquareValue(coordinates), '3')
        
        
    def test_normal_cases(self):
        print(self._testMethodName)
        board = Board()
        coordinates = Coordinates(0, 0)
        self.assertEqual(board.getSquareValue(coordinates), '.')
        coordinates = Coordinates(14, 0)
        self.assertEqual(board.getSquareValue(coordinates), '.')
        coordinates = Coordinates(0, 14)
        self.assertEqual(board.getSquareValue(coordinates), '.')
        coordinates = Coordinates(14, 14)
        self.assertEqual(board.getSquareValue(coordinates), '.')