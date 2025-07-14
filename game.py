import pygame
from pygame.locals import *
from random import randint

keys = [False,False,False,False]
pygame.init()
score = 0
width = 600
height = 600
screen = pygame.display.set_mode((width, height))

bg1 = pygame.image.load("cargame/imgs/background.jpeg")
car =  pygame.image.load("cargame/imgs/car.png")
bg  = pygame.transform.scale(car,(100,1600))
car  = pygame.transform.scale(car,(100,100))

fuelx = randint(20,580)
fuely = randint(20,580)
bg  = pygame.transform.scale(bg1,(600,600))
objx = 200
objy = 200
fuel = pygame.image.load("cargame/imgs/fuel.png")
fuel  = pygame.transform.scale(fuel,(100,100))
running = True
while running:
    car_rect = pygame.Rect(objx, objy,100,100)
    fuel_rect = pygame.Rect(fuelx, fuely, 100, 50)
    screen.blit(bg, (0,0))
    screen.blit(car,(objx, objy))
    screen.blit(fuel,(fuelx, fuely))    
    
    if car_rect.colliderect(fuel_rect):
        score += 50
        print(str(score))
        fuelx = randint(100,500)
        fuely = randint(100,500)


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