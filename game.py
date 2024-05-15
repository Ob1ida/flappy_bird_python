import pygame
from sys import exit
from Player import Player
from random import randint
from TopObstacle import Obstacle
from bottomObstacle import Obstacle2

def collision():
    if pygame.sprite.spritecollide(player.sprite,Top_obs,False) or pygame.sprite.spritecollide(player.sprite,bottom_obs,False):
        return False
    else:
        return True
def update_score():
    score_surf = font.render(str(score),False,'Black')
    score_rect = score_surf.get_rect(center = (500,50))
    scr.blit(score_surf,score_rect)
    pass
pygame.init()

#setting up the screen
scr = pygame.display.set_mode((1000,600))
pygame.display.set_caption('Flappy Bird')
score = 0
font = pygame.font.Font('font/Pixeltype.ttf',50)
score_surf = font.render(str(score),False,'Black')
score_rect = score_surf.get_rect(center = (500,50))
clock  = pygame.time.Clock()
#loading the images and creating rect

Ground = pygame.image.load('graphics/ground.png')


Sky = pygame.image.load('graphics/Sky.png')

#obstacles
UpObs = pygame.image.load('graphics/Upobs.png')
UpObs_rect = UpObs.get_rect(bottomleft = (500,40))
LowObs = pygame.image.load('graphics/lowobs.png')
LowObs_rect = LowObs.get_rect(topleft = (500,190))


#lowest point : 360
#highest point :40
obstacle_list = []

active = True


Top_obs = pygame.sprite.Group()
bottom_obs = pygame.sprite.Group()

player = pygame.sprite.GroupSingle()
player.add(Player())

print(Sky.get_height())

#sitting a timer for spawning obss

obstacle_timer = pygame.USEREVENT +1
pygame.time.set_timer(obstacle_timer,2000)

runnig = True
while runnig:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if active:
            if event.type == obstacle_timer:
                position = randint(40,360)
                Top_obs.add(Obstacle(position))
                bottom_obs.add(Obstacle2(position))
       # if not active:
            #if event.type == pygame.KEYDOWN :
             #   if event.key == pygame.K_SPACE:
                  #  if player.death():
                       # pass
                    
            
    if active: 
                     
        #blit the objects on screen (:
        scr.blit(Sky,(0,0))
        bottom_obs.draw(scr)
        bottom_obs.update()
        scr.blit(Ground,(0,556))
        player.draw(scr)
        player.update()
        Top_obs.draw(scr)
        Top_obs.update()

        update_score()
        for obs in Top_obs:
            if obs.rect.x <= 200:
                score +=1
                print(score)
                

        if player.sprite.dead():
            active = 0
       
        active = collision()
        
    else:
        scr.fill('Green')

    pygame.display.update()
    clock.tick(60)