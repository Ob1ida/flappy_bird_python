import pygame
from sys import exit
from Player import Player
from random import randint
from TopObstacle import Obstacle
from bottomObstacle import Obstacle2

def obstacle_movment(obstacle_list):
    if obstacle_list:
        for obstacle_rect in obstacle_list:
            obstacle_rect[0].x -=5
            obstacle_rect[1].x -=5
            
            scr.blit(UpObs,obstacle_rect[0])
            scr.blit(LowObs,obstacle_rect[1])

        obstacle_list = [obstacle for obstacle in obstacle_list if obstacle[1].x >110]

        return obstacle_list    
    else:
        return []
    

def collisions(player,obstacles):
    if obstacles:
        for obs in obstacles:
            if player.colliderect(obs[0]) or player.colliderect(obs[1]): return False


    return True


def collision():
    if pygame.sprite.spritecollide(player.sprite,Top_obs,False) or pygame.sprite.spritecollide(player.sprite,bottom_obs,False):
        return False
    else:
        return True

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
UpObs_rect = UpObs.get_rect(bottomleft = (500,40))
LowObs = pygame.image.load('graphics/lowobs.png')
LowObs_rect = LowObs.get_rect(topleft = (500,190))


#lowest point : 360
#highest point :40
obstacle_list = []

active = True

score = 0
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

        if event.type == obstacle_timer:
            position = randint(40,360)
            Top_obs.add(Obstacle(position))
            bottom_obs.add(Obstacle2(position))

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


        for obs in Top_obs:
            if obs.rect.x < 200:
                score +=1
                print(score)
                obs.kill()

        
       
        active = collision()
        
    else:
        scr.fill('Green')

    pygame.display.update()
    clock.tick(60)