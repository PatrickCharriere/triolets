from Game import Game
from Board import *
import pygame
fonts = pygame.font.get_fonts()
print(len(fonts))
for f in fonts:
    print(f)

#font = pygame.font.SysFont(fonts[0], 24)

WIDTH, HEIGHT = 1000, 1000
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARK_BLUE = (0,72,125)
BLUE = (1,97,172)
PURPLE = (108,71,150)
GREEN = (60,155,138)
LIGHT_BLUE = (46,64,221)
ORANGE = (248,175,0)
SILVER = (105,152,202)


block_width, block_height = 50, 50

def draw_block(color, position):
    pygame.draw.rect(surface, color, position)
    if False:
        raanana

def draw_block_border(color, position, width):
    pygame.draw.rect(surface, color, position, width)

def draw_board():
    draw_block(DARK_BLUE, (0, 0, WIDTH, HEIGHT))    #background
    
    for y in range(rowsNumber):
        for x in range(columnsNumber):
            draw_block(BLUE, ((WIDTH - (block_width * columnsNumber))/2 + (x * block_width), (HEIGHT - (block_height * rowsNumber))/2 + (y * block_height), block_width, block_height))
            draw_block_border(SILVER, ((WIDTH - (block_width * columnsNumber))/2 + (x * block_width), (HEIGHT - (block_height * rowsNumber))/2 + (y * block_height), block_width, block_height), 1)
    
    draw_block_border(BLACK, ((WIDTH - (block_width * columnsNumber))/2, (HEIGHT - (block_height * rowsNumber))/2, (columnsNumber * block_width), (rowsNumber * block_height)), 3)
    pygame.display.flip()

surface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Triolets")

     

def main():
    run = True
    game = Game(2)
    game.initialise()
    #game.start()
    draw_board()
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        
        
    
    pygame.quit()

if __name__ == "__main__":
    main()

