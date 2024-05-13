import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('graphics/Player.png').convert_alpha()
        self.rect = self.image.get_rect(center = (200,200))
        self.velocity = 0
    
    
    def jump(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            self.velocity = -8

    def gravity(self):
        self.velocity +=0.8
        self.rect.y +=self.velocity


    def update(self):
        self.jump()
        self.gravity()