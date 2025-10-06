import os
import pygame

pygame.init()
pygame.display.set_caption("Space Invaders Game")
screen = pygame.display.set_mode((400, 600))
screen.fill("gray")
pygame.display.update()
ludo = pygame.image.load("matchTheWords/imgs/ludo.png")
candy = pygame.image.load("matchTheWords/imgs/candy.jpg")
subway = pygame.image.load("matchTheWords/imgs/subway.png")
temple = pygame.image.load("matchTheWords/imgs/temple.png")
cr = pygame.image.load("matchTheWords/imgs/clash.jpeg")
ag = pygame.image.load("matchTheWords/imgs/among.jpeg")
clash = pygame.transform.scale(cr,(90,90))
among = pygame.transform.scale(ag,(90,90))
screen.blit(ludo,(50, 0))
screen.blit(candy,(50, 100))
screen.blit(temple,(50, 200))
screen.blit(subway,(50, 300))
screen.blit(clash,(50, 400))
screen.blit(among,(50, 500))

font = pygame.font.SysFont("Fredoka1", 30)
text=font.render("Subway Surfer", True, "black")
screen.blit(text,(200,25))
text=font.render("Temple Run", True, "black")
screen.blit(text,(200,125))
text=font.render("Candy Crush", True, "black")
screen.blit(text,(200,225))
text=font.render("Ludo", True, "black")
screen.blit(text,(200,325))
text=font.render("Among Us", True, "black")
screen.blit(text,(200,425))
text=font.render("Clash Royale", True, "black")
screen.blit(text,(200,525))




pygame.display.update()




while True:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            quit()
        if i.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
        
            pygame.draw.circle(screen, "black",pos, 12.5,0 )    
            pygame.display.update()
        if i.type == pygame.MOUSEBUTTONUP:
            pos2 = pygame.mouse.get_pos()
            pygame.draw.circle(screen, "black",pos2, 12.5,0 )    
            pygame.draw.line(screen, "black", pos, pos2, 2)
            pygame.display.update()

