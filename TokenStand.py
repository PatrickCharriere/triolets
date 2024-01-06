from array import *

class TokenStand:
    _tokens = []
    
    def __init__(self, tokens):
        self._tokens = tokens
    
    def print(self):
        for token in self._tokens:
            print(' ', end='')
            print(token.value, end='')
        print('')