import pygame

pygame.init()

screen=pygame.display.set_mode((500,500))

class Circle:
    def __init__(self, radius, color, pos, circumfrence):
        self.radius=radius
        self.color=color
        self.pos=pos
        self.circumfrence=circumfrence
        self.screen = screen
    def draw(self):
        pygame.draw.circle(self.screen,self.color,self.pos,self.radius,self.circumfrence)


greencircle=Circle(100, "green", (250,250),0)


Run = True



while Run:
    for i in pygame.event.get():
        if i.type==pygame.QUIT:
            run=False
    screen.fill("white")
    greencircle.draw()
    pygame.display.update()
