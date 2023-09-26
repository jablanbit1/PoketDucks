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
pg.mixer.music.load("RELJA_TORINNO_i_POPOVSKA_-_PROBLEMA_tekst.mp3")
pg.mixer.music.set_volume(0)   #0.5
pg.mixer.music.play(-1)

#patkice
patkica1 = Patkica(SCREEN_WIDTH / 6, SCREEN_HEIGHT - 132, 30, 0)
patkica2 = Patkica(SCREEN_WIDTH * 5 / 6, SCREEN_HEIGHT - 132, 30, 1)

#Dizajn
sky_surface = pg.image.load('slike/NeboPSSL.png').convert_alpha()
ground_surface = pg.image.load('slike/more.png').convert_alpha()
ground_surface_half = pg.image.load('slike/morePola.png').convert_alpha()


potez1 = True
potez2 = False
potez2 = False

inklik = False
kockicaa = False 
x1 = 0
y1 = 0
visina1 = random.randint(460, 480) 
visina2 = random.randint(460, 480)

n = 11

x = SCREEN_WIDTH // 2
x -= 5 * 40
y = SCREEN_HEIGHT - 10.5 * 40


"""
led = []
for i in range(n):
    ledic = []
    x = SCREEN_WIDTH // 2
    x -= 5 * 40
    for j in range(n):
        ledic.append(Santa(x, y))
        x += 40
    led.append(ledic)
    y += 40
"""    
SCREEN_WIDTH = 1080
BLOCK_WIDTH = 40


pattern = [
    " , , , ,*, , , , ",
    " , ,*, ,*, ,*, , ",
    "*, ,*, ,*, ,*, ,*",
    "*, ,*, ,*, ,*, ,*",
]

led = []
num_rows = len(pattern)
num_columns = len(pattern[0])
start_x = SCREEN_WIDTH // 2 - (num_columns // 2) * BLOCK_WIDTH
booo=0
"""
for row in range(num_rows):
    ledic=[]
    for col in range(num_columns):
        if pattern[row][col] == "*":
            x = start_x + col * BLOCK_WIDTH
            y = row * BLOCK_WIDTH
            ledic.append(Santa(x, y))
            booo+=1
        print(booo)
    led.append(ledic)
"""
"""
y = SCREEN_HEIGHT - 10.5 * 40
nx=[]

for i in range(num_rows):
    x = SCREEN_WIDTH - (5 * 40)
    kocke_leda = []
    red = list
    red.append((pattern[i].split(",")))
    for j in range(num_columns):
        if red[j] == "*":
            tupl = Santa(tuple(x, y))
            kocke_leda.append(tupl)
        x+=40
    led.append(kocke_leda)
    y+=40

SCREEN_WIDTH = 800
BLOCK_WIDTH = 40
"""
#--------------------
"""
br_red=[]
br_kolona=[]
brojacI=0
brojacJ=0
led=[]
for i in range(num_rows):
    red=[]
    niz_santi_za_red=[]
    red.append(pattern[i].split(','))
    for j in red:  #1. petlja
        for k in j:  #2. petlja
            if k == "*":
                niz_santi_za_red.append(Santa(x, y))
                brojacJ6+=1
            x+=40
        br_kolona.append(brojacJ)
        brojacI=0
        led.append(niz_santi_za_red)
        y+=40
"""
#-----------------------------------------

promena2 = 1
promena1 = 1

sledeci = 2

font = pg.font.Font(None, 36)
fontt = pg.font.Font(None, 72)
hp1 = font.render('Player 1: ', True, (0, 0, 0))
hp2 = font.render('Player 2: ', True, (0, 0, 0))
pg.mixer.music.load("RELJA_TORINNO_i_POPOVSKA_-_PROBLEMA_tekst.mp3")
pg.mixer.music.set_volume(0.5)
pg.mixer.music.play(-1)
# 

def prikaz(screen, slika, koor):
    screen.blit(slika , koor)

while running:
    screen.fill((200, 200, 240))
    prikaz(screen ,sky_surface, (0, 0))
    prikaz(screen, ground_surface, (-10, 600))

    """visina = 530
    promena = 1
    if visina < 500 or visina > 530:
        promena*=-1
    visina+=1*promena
    prikaz(screen, patkica1.crtaj_slika(), (patkica1.x - 160, visina))
    prikaz(screen, patkica2.crtaj_slika(), (patkica2.x - 100, visina))
    """#prikaz(sky_surface, (0, 0))
    #prikaz(ground_surface, (-10, 600))
    """
    for i in range(num_rows):
        for j in range(br_kolona[i]):
            led[i][j].nacrtaj(screen)
    """
    #print('potez1: ', potez1)
    if inklik:
        if potez1:
            pg.draw.line(screen, (0, 0, 0),(patkica1.x, visina1 + 80), (patkica1.x + (x1 - tren[0]), patkica1.y + (y1 - tren[1])), 6)
        if potez2:
            pg.draw.line(screen, (0, 0, 0),(patkica2.x, visina2 + 80), (patkica2.x + (x1 - tren[0]), patkica2.y + (y1 - tren[1])), 6)

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
        if potez1:
            kreni(patkica1, keys, event)

        if potez2:
            kreni(patkica2, keys, event)

        if event.type == pg.MOUSEBUTTONUP and inklik:
            poz2 = pg.mouse.get_pos()
            x2 = poz2[0]
            y2 = poz2[1]
            inklik = False
            vx = (x2 - x1) / 1.2
            vy = (y2 - y1) / 1.2
                   
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


    """promena1 = random.random()
    promena2 = random.random()  
    """
    if visina1 < 460 or visina1 > 480:
        promena1 *= -1
    visina1 -= promena1
    #print ("Visina: ", visina1, "\nPromena: ", promena1)

    if visina2 < 460 or visina2 > 480:
        promena2 *= -1
    visina2 -= 1*promena2

    #prikaz(screen, patkica1.crtaj(screen), (100, visina1))
    #prikaz(screen, patkica2.crtaj(screen), (840, visina2))

    prikaz(screen, patkica1.crtaj_slika(), (patkica1.x-120, visina1))
    prikaz(screen, patkica2.crtaj_slika(), (patkica2.x-120, visina2))
    

    if kockicaa:
        k.crtaj(screen)
        k.mrdaj()
        k.gravitacija()
        
        if k.x < 0 or k.x > SCREEN_WIDTH or k.y > SCREEN_HEIGHT:
            if sledeci == 1:
                potez1 = True
            if sledeci == 2:
                potez2 = True
                
        if abs(k.x - patkica1.x+20) < (k.a + patkica1.r) / 2 and abs(k.y - visina1-20) < (k.a + patkica1.r) / 2 and sledeci == 1:
            patkica1.hp -= 10
            kockicaa = False
            potez1 = True
            potez2 = False
            sledeci = 2

        if abs(k.x - patkica2.x-10) < (k.a + patkica2.r) / 2 and abs(k.y - visina2-10) < (k.a + patkica2.r) / 2 and sledeci == 2:
            patkica2.hp -= 10
            kockicaa = False
            potez2 = True
            potez1 = False
            sledeci = 1
            
        stop = False
            
        for i in range(n):
            for j in range(n):
                komadic = led[i][j]
                dx = abs(komadic.x - k.x)
                dy = abs(komadic.y - k.y)
                d = (komadic.a + k.a) / 2
                if komadic.postoji and dx < d and dy < d and not stop:
                    led[i][j].crash(k)
                    stop = True
                    if sledeci == 1:
                        kockicaa = False
                        potez1 = True
                        potez2 = False
                        sledeci = 2
                        print('1. gadja led, igra 2.')
                    elif sledeci == 2:
                        kockicaa = False
                        potez2 = True
                        potez1 = False
                        sledeci = 1
                        print('2. gadja led, igra 1.')
            if stop:
                break
                
    
    pg.draw.circle(screen, (100,100,100), (patkica2.x, patkica2.y), patkica2.r)
    hp1 = font.render('Player 1: ' + str(patkica1.hp), True, (0, 0, 0))
    hp2 = font.render('Player 2: ' + str(patkica2.hp), True, (0, 0, 0))
    pg.draw.rect(screen, (255, 0, 0), pg.Rect(30, 58, 100, 25))
    pg.draw.rect(screen, (0, 255, 0), pg.Rect(30, 58, patkica1.hp, 25))
    pg.draw.rect(screen, (255, 0, 0), pg.Rect(881, 58, 100, 25))
    pg.draw.rect(screen, (0, 255, 0), pg.Rect(881, 58, patkica2.hp, 25))
                    
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
    
    """patkica1.crtaj(screen)
    patkica2.crtaj(screen)
    """
    prikaz(screen, ground_surface_half, (0, 650))
    pg.display.flip()
    clock.tick(60)
    
pg.quit()
