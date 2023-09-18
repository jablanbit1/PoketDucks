
import pygame as pg

def kreni(patkica, event):
    if event.key == pg.K_LEFT:
            patkica.ky +=5
            patkica.plivaj()
             

    if event.key == pg.K_RIGHT:

            patkica.ky -=5
            patkica.plivaj()  