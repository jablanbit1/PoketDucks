import pygame as pg

def kreni(patkica, keys):
    #while(event.type==pg.KEYDOWN):    
    #if event.type == pg.KEYDOWN:
        #while event.type != pg.KEYUP:
        #print(event.type)       
        """if event.key == pg.K_LEFT:
                        
                patkica.vx =-5
                patkica.plivaj()
                print(patkica.vx)
                        

        if event.key == pg.K_RIGHT:
                        
                patkica.vx =5
                print(patkica.vx)
                patkica.plivaj()"""
        
    
        if keys[pg.K_LEFT] and patkica.x>0:
                
                        patkica.vx = -5
                        patkica.plivaj()
                        pg.time.delay(50)


        if keys[pg.K_RIGHT] and patkica.x<1080:
                
                        patkica.vx = 5
                        patkica.plivaj()
                        pg.time.delay(50)