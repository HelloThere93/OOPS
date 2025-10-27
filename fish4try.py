import os
import pygame
import random
pygame.init()
pygame.display.set_caption("fish")
width = 400
height = 600
screen = pygame.display.set_mode((width, height))
score = 0
class Block(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.image=pygame.Surface([width, height])
        self.image.fill(color)
        self.rect=self.image.get_rect()
    
    def Resetpos(self):
        self.rect.y=random.randrange(-300,-20)
        self.rect.x=random.randrange(0,width)
    
    def update(self):
        self.rect.y += 1
        if self.rect.y > 450:
            self.Resetpos()
        
class Player(Block):
    



foodlist=pygame.sprite.Group() # it amkes a group of sprites(the fishes food)
allsprites=pygame.sprite.Group()# fish + food both


for i in range(50):
    food=Block("black", 20, 15)
    food.rect.x=random.randrange(width)
    food.rect.y=random.randrange(height)
    foodlist.add(food)
    allsprites.add(food)
fish=Block("red", 20,15)    
allsprites.add(fish)
while True:
    
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            quit() 
    
    screen.fill("gray")
    pos = pygame.mouse.get_pos()
    fish.rect.x=pos[0]
    fish.rect.y=pos[1]

    blockhitlist=pygame.sprite.spritecollide(fish, foodlist, True)
    
    for i in blockhitlist:
        score += 1
        print(score)
        
                

    allsprites.draw(screen)
    pygame.display.update()
