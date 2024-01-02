from Constants import *
from enum import Enum

rowsNumber = 15
columnsNumber = 15
class SquareValues(Enum):
    NORMAL = 1
    REPLAY = 2
    x2 = 3
    x3 = 4

class Coordinates:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Square:
    coordinates: Coordinates
    value: SquareValues

    def __init__(self, coordinates, *args):
        self.coordinates = coordinates
        value = 0
        for ar in args:
            value = ar
        if(value):
            self.value = value
        else:
            self.value = specialSquares.getValue(coordinates)
    
    def textValue(self):
        match self.value:
            case SquareValues.REPLAY:
                return 'R'
            case SquareValues.x2:
                return '2'
            case SquareValues.x3:
                return '3'
            case _:
                return '.'

class SquareSet:
    set = []

    def __init__(self, set):
        for i in range(len(set)):
            self.set.append(set[i])

    def getValue(self, coordinates):
        for i in range(len(self.set)):
            if ((self.set[i].coordinates.x == coordinates.x) & (self.set[i].coordinates.y == coordinates.y)):
                return self.set[i].value
        return SquareValues.NORMAL
    
specialSquares = SquareSet([
    Square(Coordinates(7, 0), SquareValues.REPLAY),
    Square(Coordinates(1, 1), SquareValues.REPLAY),
    Square(Coordinates(4, 1), SquareValues.x3),
    Square(Coordinates(10, 1), SquareValues.x3),
    Square(Coordinates(13, 1), SquareValues.REPLAY),
    Square(Coordinates(7, 3), SquareValues.x2),
    Square(Coordinates(1, 4), SquareValues.x3),
    Square(Coordinates(4, 4), SquareValues.x2),
    Square(Coordinates(10, 4), SquareValues.x2),
    Square(Coordinates(13, 4), SquareValues.x3),
    Square(Coordinates(0, 7), SquareValues.REPLAY),
    Square(Coordinates(3, 7), SquareValues.x2),
    Square(Coordinates(7, 7), SquareValues.x2),
    Square(Coordinates(11, 7), SquareValues.x2),
    Square(Coordinates(14, 7), SquareValues.REPLAY),
    Square(Coordinates(1, 10), SquareValues.x3),
    Square(Coordinates(4, 10), SquareValues.x2),
    Square(Coordinates(10, 10), SquareValues.x2),
    Square(Coordinates(13, 10), SquareValues.x3),
    Square(Coordinates(7, 11), SquareValues.x2),
    Square(Coordinates(1, 13), SquareValues.REPLAY),
    Square(Coordinates(4, 13), SquareValues.x3),
    Square(Coordinates(10, 13), SquareValues.x3),
    Square(Coordinates(13, 13), SquareValues.REPLAY),
    Square(Coordinates(7, 14), SquareValues.REPLAY),
])

class Board:
    board = []
    specialSquares = specialSquares

    def __init__(self):
        for i in range(rowsNumber):
            for j in range(columnsNumber):
                coordinates = Coordinates(j, i)
                square = Square(coordinates)
                self.board.append(square)

    def printBoard(self):
        for y in range(rowsNumber):
            print()
            for x in range(rowsNumber):
                print(self.board[((x * rowsNumber) + y)].textValue(), end = " ")
        
        print()

        