import os
import pygame
import random
pygame.init()
pygame.display.set_caption("Space Invaders Game")
width = 400
height = 600
screen = pygame.display.set_mode((width, height))
score = 0
maxfood = 51
class Block(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.image=pygame.Surface([width, height])
        self.image.fill(color)
        self.rect=self.image.get_rect()
foodlist=pygame.sprite.Group() # it amkes a group of sprites(the fishes food)
allsprites=pygame.sprite.Group()# fish + food both

for i in range(maxfood):
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
    font=pygame.font.SysFont("Arial",50)
    for i in blockhitlist:
        score += 1
        print(score)
        
    allsprites.draw(screen)
    text=font.render("Score Is "+str(score),True, "Black" )
    screen.blit(text,(150,250))
    pygame.display.update()

    if score == maxfood:
        text1= font.render("you won", True, "Black")
        screen.blit(text1,(50,50))
        pygame.display.update()         

    
    
                

    
    pygame.display.update()
