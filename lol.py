import pygame

pygame.init()

screen = pygame.display.set_mode((500,500))

class Circle:
    def __init__(self, radius, color, pos, circumfrence):
        self.radius = radius
        self.color = color
        self.pos = pos
        self.circumfrence = circumfrence
        self.screen = screen
    def draw(self):
        pygame.draw.circle(self.screen, self.color, self.pos, self.radius, self.circumfrence)

circle1 = Circle(50, "red", (100, 100), 0)
circle2 = Circle(75, "blue", (400, 100), 0)
circle3 = Circle(30, "green", (250, 400), 0)
circle4 = Circle(90, "purple", (250, 250), 0)

run = True

while run:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            run = False
    screen.fill("white")
    circle1.draw()
    circle2.draw()
    circle3.draw()
    circle4.draw()
    pygame.display.update()

pygame.quit()
