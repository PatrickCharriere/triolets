import random

from Token import Token
Qties = [9, 9, 8, 8, 7, 8, 6, 6, 4, 4, 3, 3, 2, 2, 1, 1]
maxDrawQty = 3

class TokenBag:
    tokens = []
    def  __init__(self):
        value = 0
        for qty in Qties:
            value += 1
            for i in range(qty):
                self.tokens.append(value-1)

        self.tokens.append('x')
        self.tokens.append('x')
        random.shuffle(self.tokens)
        print(self.tokens)

    def draw(self, qty):
        if(qty > maxDrawQty):
            return print("Error you tried to draw " + str(qty) + " from the bag when " + str(maxDrawQty) + " is the maximum tokens you can take.")
        if(qty == 0):
            return print("Error, you cannot draw 0 tokens.")
        drawnTokens = self.tokens[:qty]
        self.tokens = self.tokens[qty:]
        return drawnTokens
    
    def print(self):
        print("Qty: " + str(len(self.tokens)) + " " + str(self.tokens))