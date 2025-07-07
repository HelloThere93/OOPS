import pygame

pygame.init()
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Light Switch")

button_img = pygame.image.load("light/imgs/button.png")
button_img = pygame.transform.scale(button_img, (100, 50))

light_off_img = pygame.image.load("light/imgs/lightoff.png")
light_off_img = pygame.transform.scale(light_off_img, (200, 100))

light_on_img = pygame.image.load("light/imgs/lighton.png")
light_on_img = pygame.transform.scale(light_on_img, (200, 100))

light_on = False
button_rect = pygame.Rect(150, 200, 100, 50)

running = True
while running:
    screen.fill((30, 30, 30))

    if light_on:
        screen.blit(light_on_img, (100, 50))
    else:
        screen.blit(light_off_img, (100, 50))

    screen.blit(button_img, (150, 200))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if button_rect.collidepoint(event.pos):
                light_on = not light_on

    pygame.display.update()

pygame.quit()

