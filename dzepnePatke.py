import pygame as pg

class Patkica:

    def __init__(self, x, y, r1):
        self.x = x
        self.y = y
        self.vx = 0
        self.vy = 0
        self.hp = 100
        self.r1 = r1
        #self.r2 = r2


    def crtaj(self, pozadina):
        pg.draw.circle(pozadina, (0, 255, 255), (self.x, self.y),self.r1 )

    def plivaj(self):
        self.x += self.vx
        
    def puckaj():
        pass
      