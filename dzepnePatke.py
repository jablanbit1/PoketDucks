import pygame as pg

class Patkica:

    def __init__(self, x, y, r, s):
        self.x = x
        self.y = y
        self.vx = 0
        self.hp = 100
        self.r = r
        if s == 0:
            self.patka_surface = pg.image.load('slike/patka_editovana.png').convert_alpha()
        else: 
            self.patka_surface = pg.image.load('slike/patka1_editovana.png').convert_alpha()


    def crtaj(self, pozadina):
        pg.draw.circle(pozadina, (255, 255, 0), (self.x, self.y), self.r)
        return self.patka_surface
    
    def plivaj(self):
        self.x += self.vx        

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
        
<<<<<<< HEAD
        
=======
class Santa:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.a = 40
        self.postoji = True
        
    def nacrtaj(self, pozadina):
        if self.postoji:
            a = self.a
            x = self.x
            y = self.y
            pg.draw.rect(pozadina, (0, 255, 255), pg.Rect(x - a / 2, y - a / 2, a, a))
        
    def crash(self, kockica):
        if self.postoji and abs(self.x - kockica.x) < (self.a + kockica.a) / 2 and abs(self.y - kockica.y) < (self.a + kockica.a) / 2:
            self.postoji = False
>>>>>>> d9ef7b0222baed0f34a3c479a093036fbdce0f2c
