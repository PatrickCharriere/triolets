class Player:
    tokens = []
    points = 0
    def __init__(self, name):
        self.name = name

    def drawTokensFromTokenBag(self, tokenBag, qty):
        tokens = tokenBag.draw(qty)
        print(self.name + ": " + str(tokens))