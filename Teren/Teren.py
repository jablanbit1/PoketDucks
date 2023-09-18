import pygame
from main import *


class Pravougaonik:
    def __init__(self, length, height):
        self.length = length
        self.height = height
    
    def crtanje(self, boja):
        pygame.draw.rectangle(screen, boja, [0, 0, self.length, self.height])
        pygame.display.update()



def main():
    Teren = Pravougaonik(SCREEN_WIDTH, SCREEN_HEIGHT)
    Teren.crtanje(boja = blue)



if __name__ == "__main__":
    main()
