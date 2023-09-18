import pygame



class Pravougaonik:
    def __init__(self, length, height):
        self.length = length
        self.height = height
    
    def crtanje(self, pozadina):
        pygame.draw.rect(pozadina,0, 0, self.length, self.height)
        pygame.display.flip()





def mkTeren(SCREEN_WIDTH, SCREEN_HEIGHT, pozadina):
    Teren = Pravougaonik(SCREEN_WIDTH, SCREEN_HEIGHT)
    Teren.crtanje(pozadina)
    


