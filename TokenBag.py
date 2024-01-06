import random

from Token import Token
Qties = [9, 9, 8, 8, 7, 8, 6, 6, 4, 4, 3, 3, 2, 2, 1, 1]
maxDrawQty = 3

get_indexes = lambda x, xs: [i for (y, i) in zip(xs, range(len(xs))) if x == y.value]
    
class TokenBag:
    _tokens = []
    def  __init__(self):
        value = 0
        for qty in Qties:
            value += 1
            thisToken = Token(value-1)
            for i in range(qty):
                self._tokens.append(thisToken)

        thisToken = Token('x')
        self._tokens.append(thisToken)
        self._tokens.append(thisToken)
        random.shuffle(self._tokens)
        #self.print()

    def draw(self, qty):
        if(qty > maxDrawQty):
            return print("Error you tried to draw " + str(qty) + " from the bag when " + str(maxDrawQty) + " is the maximum tokens you can take.")
        if(qty == 0):
            return print("Error, you cannot draw 0 tokens.")
        drawnTokens = self._tokens[:qty]
        self._tokens = self._tokens[qty:]
        return drawnTokens
    
    def print(self):
        print("Qty: " + str(len(self._tokens)) + " tokens.")
        print("[", end='')
        i = 0
        while i < len(self._tokens):
            print(self._tokens[i].value, end='')
            i += 1
            if(i<len(self._tokens)):
                print("", end=', ')
        print("]")
        return
        
    def countTokens(self, *args):
        if len(args) == 0:
            return len(self._tokens)
        value = 0
        for ar in args:
            value = ar
        return len(get_indexes(value, self._tokens))
            