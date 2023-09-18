import pygame
from PoketDucks.main import *


class Pravougaonik:
    def __init__(self, length, height):
        self.length = length
        self.height = height
    
<<<<<<< HEAD
    def crtanje(self, pozadina):
        pygame.draw.rect(pozadina,0, 0, self.length, self.height)
        pygame.display.flip()

=======
    def crtanje(self, boja):
        pygame.draw.rectangle(screen, boja, [0, 0, self.length, self.height])
        pygame.display.update()
>>>>>>> 854ad189185b79ef87c9cb3b0b267ea348d88c63



def main():
    Teren = Pravougaonik(SCREEN_WIDTH, SCREEN_HEIGHT)
<<<<<<< HEAD
    Teren.crtanje(pozadina)
    
=======
    Teren.crtanje(boja = blue)

>>>>>>> 854ad189185b79ef87c9cb3b0b267ea348d88c63


if __name__ == "__main__":
    main()
