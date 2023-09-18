import pygame
from PoketDucks import main


class Pravougaonik:
    def __init__(self, length, height):
        self.length = length
        self.height = height
    
    def crtanje(self):
        pygame.draw.rectangle(0, 0, self.length, self.height)




def main():
    Teren = Pravougaonik(SCREEN_WIDTH, SCREEN_HEIGHT)
    Teren.crtanje()



if __name__ == "__main__":
    main()
