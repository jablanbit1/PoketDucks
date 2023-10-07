import pygame as pg

def kreni(patkica, event, keys):
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
        
    
        if keys[pg.K_LEFT]:
                
                        pg.time.delay(200)
                        patkica.vx = -5
                        patkica.plivaj()


        if keys[pg.K_RIGHT]:
                
                        pg.time.delay(200)
                        patkica.vx = 5
                        patkica.plivaj()
