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

patkica1 = Patkica(SCREEN_WIDTH / 6, SCREEN_HEIGHT - 132, 30)
patkica2 = Patkica(SCREEN_WIDTH * 5 / 6, SCREEN_HEIGHT - 132, 30)

sky_surface = pg.image.load('slike/Pozadina-nebo.jpg')
ground_surface = pg.image.load('slike/more.png')

potez1 = False
potez2 = True
inklik = False
kockicaa = False

def pozadina(slika, koor):
    screen.blit(slika, koor)

while running:
    screen.fill((200, 200, 240))
   
    for event in pg.event.get():
            

        if event.type == pg.QUIT:
            pg.quit()
            quit()
        if event.type == pg.MOUSEBUTTONDOWN and not inklik and (potez1 or potez2):
            poz1 = pg.mouse.get_pos()
            x1 = poz1[0]
            y1 = poz1[1]
            inklik = True
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
            if potez2:
                k = Kockica(patkica2.x, patkica2.y, vx, vy)
                k.crtaj(screen)
                kockicaa = True
    

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
        #if k.x < 0 or k.x > SCREEN_WIDTH or k.y > SCREEN_HEIGHT:
            
        
    
    
    pg.display.flip()
    clock.tick(60)
    
pg.quit()
