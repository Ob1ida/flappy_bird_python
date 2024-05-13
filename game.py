import pygame
from sys import exit
pygame.init()

scr = pygame.display.set_mode((1000,600))
pygame.display.set_caption('Flappy Bird')
clock  = pygame.time.Clock()

Player = pygame.image.load('graphics/Player.png')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()


    scr.blit(Player,(0,0))

    pygame.display.update()
    clock.tick(60)