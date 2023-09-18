import pygame
#from main import *


class Pravougaonik:
    def __init__(self, length, height):
        self.length = length
        self.height = height
    
    def crtanje(self, screen, sw):
        #pygame.draw.rect(screen, (0, 0, 255), [0, 0, self.length, self.height])
        pygame.draw.rect(screen, (0, 0, 255), pygame.Rect(0, sw, self.length, self.height))
        #pygame.display.update()


