from array import *
from Token import Token

class TokenStand:
    _tokens = []
    
    def __init__(self, tokens):
        self._tokens = tokens
    
    def print(self):
        for token in self._tokens:
            print('_', end='')
            print(token.value, end='')
        print('_')