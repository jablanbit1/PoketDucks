import pygame as pg

class Patkica:

    def __init__(self, x, y, r, s):
        self.x = x
        self.y = y
        self.vx = 0
        self.vy = 0
        self.hp = 100
        self.r = r
        #self.r2 = r2
        if s == 0:
            self.patka_surface = pg.image.load('slike/patka_editovana.png')
        else: 
            self.patka_surface = pg.image.load('slike/patka1_editovana.png')


    def crtaj(self):
        #pg.draw.circle(pozadina, (255, 255, 0), (self.x, self.y),self.r1 
        return self.patka_surface
    
    def plivaj(self):
        self.x += self.vx
        
    def puckaj(self):
        pass              

                

g = 0.4

class Kockica:
    
    def __init__(self, x, y, vx, vy):
        self.x = x
        self.y = y
        self.vx = vx * (-0.1)
        self.vy = vy * (-0.1)
        self.a = 20
        
    def crtaj(self, pozadina):
        a = self.a
        x = self.x
        y = self.y
        pg.draw.rect(pozadina, (0, 255, 255), pg.Rect(x - a / 2, y - a / 2, a, a))
        
    def gravitacija(self):
        self.vy += g
        
    def mrdaj(self):
        self.x += self.vx
        self.y += self.vy
     
