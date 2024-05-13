import pygame
from random import randint

class Obstacle(pygame.sprite.Sprite):
    def __init__(self,position): 
        super().__init__()
            
        self.image = pygame.image.load('graphics/Upobs.png')
        self.rect = self.image.get_rect(bottomleft=(1100, position))

    def update(self):
        self.obstacle_movement()

    def obstacle_movement(self):
        self.rect.x -= 2
