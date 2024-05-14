import pygame
from random import randint

class Obstacle2(pygame.sprite.Sprite):
    def __init__(self,position): 
        super().__init__()
            
        self.image = pygame.image.load('graphics/lowobs.png').convert_alpha()
        self.rect = self.image.get_rect(topleft=(1100, position + 150))

    def update(self):
        self.obstacle_movement()

    def obstacle_movement(self):
        self.rect.x -= 2