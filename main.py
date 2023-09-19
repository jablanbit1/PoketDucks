import pygame as pg
from dzepnePatke import *
from Teren import Pravougaonik
from kretnja import kreni
from dizajn.dizajn import *
import random


SCREEN_WIDTH = 1080
SCREEN_HEIGHT = 720

g = 0.4

pg.init()
screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pg.time.Clock()
running = True

#patkice
patkica1 = Patkica(SCREEN_WIDTH / 6, SCREEN_HEIGHT - 132, 30, 0)
patkica2 = Patkica(SCREEN_WIDTH * 5 / 6, SCREEN_HEIGHT - 132, 30, 1)

#Dizajn
sky_surface = pg.image.load('slike/NeboPSSL.png').convert_alpha()
ground_surface = pg.image.load('slike/more.png').convert_alpha()
ground_surface_half = pg.image.load('slike/morePola.png').convert_alpha()

potez2 = False
potez1 = True
potez2 = False

inklik = False
kockicaa = False
x1 = 0
y1 = 0
visina1 = random.randint(501, 530)
visina2 = random.randint(501, 530)

promena2 = 1
promena1 = 1

sledeci = 2

font = pg.font.Font(None, 36)
fontt = pg.font.Font(None, 72)
hp1 = font.render('Player 1: ', True, (0, 0, 0))
hp2 = font.render('Player 2: ', True, (0, 0, 0))

def prikaz(slika, koor):
    screen.blit(slika, koor)

while running:
    screen.fill((200, 200, 240))
    prikaz(sky_surface, (0, 0))
    prikaz(ground_surface, (-10, 600))
    visina = 530
    promena = 1
    if visina < 500 or visina > 530:
        promena*=-1
    visina+=1*promena
    prikaz(patkica1.crtaj(screen), ( patkica1.x ,visina))
    prikaz(patkica2.crtaj(screen), (patkica2.x, visina))
    
    #print('potez1: ', potez1)
    if inklik:
        if potez1:
            pg.draw.line(screen, (0, 0, 0),(patkica1.x, patkica1.y), (patkica1.x + (x1 - tren[0]), patkica1.y + (y1 - tren[1])), 6)
        if potez2:
            pg.draw.line(screen, (0, 0, 0),(patkica2.x, patkica2.y), (patkica2.x + (x1 - tren[0]), patkica2.y + (y1 - tren[1])), 6)

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
        keys = pg.key.get_pressed()
        if potez1 :
            
            kreni(patkica1, event, keys)

        if potez2 :
            kreni(patkica2, event, keys)

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

            #Kretanje patke
    
            
    

    """
    Teren = Pravougaonik(SCREEN_WIDTH, 100)
    Teren.crtanje(screen, SCREEN_HEIGHT-100)
    """

    prikaz(sky_surface, (0, 0))
    prikaz(ground_surface, (-10, 600))

    if visina1 <= 500 or visina1 >= 540:
        promena1 *= -1
    visina1 += 1*promena1

    if visina2 <= 500 or visina2 >= 540:
        promena2 *= -1
    visina2 += 1*promena2

    prikaz(patkica1.crtaj(), (100, visina1))
    prikaz(patkica2.crtaj(), (840, visina2))


    if kockicaa:
        k.crtaj(screen)
        k.mrdaj()
        k.gravitacija()
        if k.x < 0 or k.x > SCREEN_WIDTH or k.y > SCREEN_HEIGHT:
            if sledeci == 1:
                potez1 = True
            if sledeci == 2:
                potez2 = True
        if abs(k.x - patkica1.x) < (k.a + patkica1.r) / 2 and abs(k.y - patkica1.y) < (k.a + patkica1.r) / 2 and sledeci == 1:
            patkica1.hp -= 10
            kockicaa = False
            potez1 = True
            potez2 = False
            sledeci = 2

        if abs(k.x - patkica2.x) < (k.a + patkica2.r) / 2 and abs(k.y - patkica2.y) < (k.a + patkica2.r) / 2 and sledeci == 2:
            patkica2.hp -= 10
            kockicaa = False
            potez2 = True
            potez1 = False
            sledeci = 1
                
    print(sledeci)
    
    hp1 = font.render('Player 1: ' + str(patkica1.hp), True, (0, 0, 0))
    hp2 = font.render('Player 2: ' + str(patkica2.hp), True, (0, 0, 0))
                    
    #Teren = Pravougaonik(SCREEN_WIDTH, 100)
    #Teren.crtanje(screen, SCREEN_HEIGHT - 100)
    
    
    
    if patkica1.hp == 0:
        txt = fontt.render('PLAYER 2 WINS!', True, (0, 0, 0))
        screen.blit(txt, (SCREEN_WIDTH // 2 - 200, SCREEN_HEIGHT // 2))
        potez1 = False
        potez2 = False
    if patkica2.hp == 0:
        txt = fontt.render('PLAYER 1 WINS!', True, (0, 0, 0))
        screen.blit(txt, (SCREEN_WIDTH // 2 - 200, SCREEN_HEIGHT // 2))
        potez1 = False
        potez2 = False
    
    screen.blit(hp1, (30, 30))
    screen.blit(hp2, (SCREEN_WIDTH - 200, 30))
    
    patkica1.crtaj(screen)
    patkica2.crtaj(screen)
    

    
    pg.display.flip()
    clock.tick(60)
    
pg.quit()
