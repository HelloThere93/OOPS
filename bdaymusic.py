import pygame
import time
pygame.mixer.init()
run=True
pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Birthday Animation Card")
bdaysound= pygame.mixer.Sound("birthdayimgs/happybirthday.mp3")
img=pygame.image.load("birthdayimgs/BdayImgs1.jpg")
img1=pygame.transform.scale(img,(600,600))

while run:
   
    for i in pygame.event.get():


        if i.type == pygame.QUIT:
            run = False
    
    
    font=pygame.font.SysFont("Arial",50)
    text=font.render("Happy Birthday",True, "Black" )
    screen.blit(img1,(0,0))
    screen.blit(text,(150,250))
    bdaysound.stop()
    bdaysound.play()
    pygame.display.update()

    time.sleep(1.0)
    
    font2=pygame.font.SysFont("Arial",49)
    img2=pygame.image.load("birthdayimgs/BdayImgs2.jpg")
    text2=font2.render("Bless you",True, "Black" )
    screen.blit(img2,(0,0))
    screen.blit(text2,(150,250))
    pygame.display.update()
    
    time.sleep(1.0)
    
    font3=pygame.font.SysFont("Arial",48)
    img3=pygame.image.load("birthdayimgs/BdayImgs3.jpg")
    text3=font3.render("Enjoy this Special Day",True, "Black" )
    screen.blit(img3,(0,0))
    screen.blit(text3,(150,250))
    pygame.display.update()
    
    time.sleep(1.0)
    