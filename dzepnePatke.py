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
        pg.draw.circle(pozadina, (255, 255, 0), (self.x, self.y),self.r1 )

    def plivaj(self):
        self.x += self.vx
        
    def puckaj(self):
        pass              
                

g = 0.3

class Kockica:
    
    def __init__(self, x, y, vx, vy):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.a = 20
        
    def crtaj(self, pozadina):
        a = self.a
        x = self.x
        y = self.y
        pg.draw.rect(pozadina, (0, 255, 255), pg.Rect(x - a / 2, y - a / 2, a, a))
        pg.display.flip()
        
    def gravitacija(self):
        self.vy += g
        
    def mrdaj(self):
        self.x += self.vx
        self.y += self.vy
    
