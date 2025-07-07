import pygame
from pygame.locals import *
keys = [False,False,False,False]
pygame.init()

width = 600
height = 600
screen = pygame.display.set_mode((width, height))

bg = pygame.image.load("rocket/imgs/bground.png")
rocket =  pygame.image.load("rocket/imgs/rocket.png")

objx = 200
objy = 200


running = True
while running:
    screen.blit(bg, (0,0))
    screen.blit(rocket,(objx, objy))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key== K_UP:
                keys[0]=True
            if event.key== K_DOWN:
                keys[1]=True
            if event.key== K_RIGHT:
                keys[2]=True
            if event.key== K_LEFT:
                keys[3]=True
        if event.type == pygame.KEYUP:
            if event.key== K_UP:
                keys[0]=False
            if event.key== K_DOWN:
                keys[1]=False
            if event.key== K_RIGHT:
                keys[2]=False
            if event.key== K_LEFT:
                keys[3]=False
    if keys[0]==True:
        objy -= 0.5
    if keys[1]==True:
        objy += 0.1
    if keys[2]==True:
        objx += 0.1
    if keys[3]==True:
        objx -= 0.1
    
    objy+= 0.1
    if objy> height:
        running=False

        
    pygame.display.update()

pygame.quit()