import pygame

pygame.init()
from random import randint
screen=pygame.display.set_mode((800,800))
screen.fill("gray")
run = True
pygame.display.update()
class Rectangle:
    def __init__(self, color,dimensions):
        self.color=color
        self.dimensions=dimensions
        self.screen=screen

       

    def draw(self):
        pygame.draw.rect(self.screen,self.color,self.dimensions)
    
for i in range(1,50):
        colorchoose=randint(1,3)
        if colorchoose == 1:
            colorchoose="black"
        elif colorchoose == 2:
            colorchoose="white"
        elif colorchoose==3:
             colorchoose="yellow"
        rectangle1=Rectangle(colorchoose,(randint(0,800),randint(0,800),randint(0,200),randint(0,200)))
        rectangle1.draw()
        pygame.display.update()
       
while run:
    
    
        
        
        

        pygame.display.update()
        for i in pygame.event.get():

            if i.type == pygame.QUIT:
                run = False
        
