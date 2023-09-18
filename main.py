import pygame

SCREEN_WIDTH = 720
SCREEN_HEIGHT = 480

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
running = True

while running:
    screen.fill((200, 200, 240))
    pygame.display.flip()
    clock.tick(60)