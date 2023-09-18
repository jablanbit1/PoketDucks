import pygame as pg
from dzepnePatke import *
from Teren import Pravougaonik

SCREEN_WIDTH = 1080
SCREEN_HEIGHT = 720

g = 0.4

pg.init()
screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pg.time.Clock()
running = True


patkica1 = Patkica(SCREEN_WIDTH / 6, SCREEN_HEIGHT - 200, 30 )
patkica2 = Patkica(SCREEN_WIDTH * 5 / 6, SCREEN_HEIGHT - 132, 30)

#Dizajn
sky_surface = pg.image.load('slike/Pozadina-nebo.jpg')
ground_surface = pg.image.load('slike/more.png')


#patkica1 = 



potez2 = False
potez1 = True
inklik = False
kockicaa = False
x1 = 0
y1 = 0

sledeci = 2



def pozadina(slika, koor):
    screen.blit(slika, koor)

while running:
    screen.fill((200, 200, 240))
    
    for event in pg.event.get():
        tren = pg.mouse.get_pos()
        if event.type == pg.QUIT:
            pg.quit()
            quit()
        if event.type == pg.MOUSEBUTTONDOWN and not inklik and (potez1 or potez2):
            poz1 = pg.mouse.get_pos()
            x1 = poz1[0]
            y1 = poz1[1]
            inklik = True
        if inklik:
            if potez1:
                    pg.draw.line(screen, (20, 20, 20), (patkica1.x, patkica1.y), (patkica1.x + (x1 - tren[0]), patkica1.y + (y1 - tren[1])), 6)
            if potez2:
                    pg.draw.line(screen, (20, 20, 20), (patkica2.x, patkica2.y), (patkica2.x + (x1 - tren[0]), patkica2.y + (y1 - tren[1])), 6)
        if event.type == pg.MOUSEBUTTONUP and inklik:
            poz2 = pg.mouse.get_pos()
            x2 = poz2[0]
            y2 = poz2[1]
            inklik = False
            vx = x2 - x1
            vy = y2 - y1           
            if potez1:
                k = Kockica(patkica1.x, patkica1.y, vx, vy)
                k.crtaj(screen)
                kockicaa = True
                potez1 = False
                sledeci = 2
                
            if potez2:
                k = Kockica(patkica2.x, patkica2.y, vx, vy)
                k.crtaj(screen)
                kockicaa = True
                potez2 = False
                sledeci = 1
                
    

    Teren = Pravougaonik(SCREEN_WIDTH, 100)
    Teren.crtanje(screen, SCREEN_HEIGHT-100)

    pozadina(sky_surface, (0, 0))
    pozadina(ground_surface, (0, 600))

    patkica1.crtaj(screen)
    patkica2.crtaj(screen)
    
    if kockicaa:
        k.crtaj(screen)
        k.mrdaj()
        k.gravitacija()
        if k.x < 0 or k.x > SCREEN_WIDTH or k.y > SCREEN_HEIGHT:
            if sledeci == 1:
                potez1 = True
                pass
            if sledeci == 2:
                potez2 = True
                pass
        
    
                    
    Teren = Pravougaonik(SCREEN_WIDTH, 100)
    Teren.crtanje(screen, SCREEN_HEIGHT-100)
    
    pg.display.flip()
    clock.tick(60)
    
pg.quit()
