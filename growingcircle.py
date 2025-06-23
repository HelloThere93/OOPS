import pygame

pygame.init()

screen=pygame.display.set_mode((800,800))
screen.fill("gray")
run = True
pygame.display.update()
class Circle:
    def __init__(self, radius, color, pos, circumfrence):
        self.radius=radius
        self.color=color
        self.pos=pos
        self.circumfrence=circumfrence
        self.screen=screen
    
    def draw(self):
        pygame.draw.circle(self.screen,self.color,self.pos,self.radius,self.circumfrence)
    def grow(self, r):
        self.radius += r
        pygame.draw.circle(self.screen,self.color,self.pos,self.radius,self.circumfrence)


circle1=Circle(15,"green",(400,400),0)


while run:
   
    for i in pygame.event.get():

        if i.type == pygame.QUIT:
            run = False

        if i.type==pygame.MOUSEBUTTONDOWN:
            # screen.fill("gray")
            circle1.grow(1)
            circle1.draw()
            pygame.display.update()

        if i.type==pygame.MOUSEMOTION:
            pos=pygame.mouse.get_pos()
            circle2=Circle(5,"black",pos,0)
            circle2.draw()
            pygame.display.update()