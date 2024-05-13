import pygame
from sys import exit
from Player import Player
pygame.init()


#setting up the screen
scr = pygame.display.set_mode((1000,600))
pygame.display.set_caption('Flappy Bird')


clock  = pygame.time.Clock()
#loading the images and creating rect

Ground = pygame.image.load('graphics/ground.png')
Sky = pygame.image.load('graphics/Sky.png')

#obstacles
UpObs = pygame.image.load('graphics/Upobs.png')
UpObs_rect = UpObs.get_rect(bottomleft = (500,150))
LowObs = pygame.image.load('graphics/lowobs.png')
LowObs_rect = LowObs.get_rect(topleft = (500,300))



velocity = 0

player = pygame.sprite.GroupSingle()
player.add(Player())

print(Sky.get_height())

#sitting a timer for spawning obss

obstacle_timer = pygame.USEREVENT +1
pygame.time.set_timer(obstacle_timer,1000)

runnig = True
while runnig:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                velocity = -11
        #if event.type == obstacle_timer:
            #print('')
            
    #blit the objects on screen (:
    scr.blit(Sky,(0,0))
    scr.blit(Ground,(0,556))
    scr.blit(UpObs,UpObs_rect)
    scr.blit(LowObs,LowObs_rect)
    player.draw(scr)
    ###player.update()
    pygame.draw.rect(scr,'Yellow',UpObs_rect,1)
    velocity += 0.8

    UpObs_rect.x -= 2
    LowObs_rect.x -= 2

    #if Playerr_rect.colliderect(UpObs_rect):
        #runnig = False
    pygame.display.update()
    clock.tick(60)