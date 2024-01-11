import pygame

background_colour = (255,255,255)
(width, height) = (300, 200)

screen = pygame.display.set_mode((width, height))

pygame.display.set_caption('Duck Stock')

Icon = pygame.image.load('assets/duck.svg')
pygame.display.set_icon(Icon)

screen.fill(background_colour)

pygame.display.flip()

running = True

while running: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False