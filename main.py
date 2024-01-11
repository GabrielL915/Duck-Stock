import pygame

main_background_colour = (19, 1, 57)
secondary_background_colour = (15, 0, 46)
(width, height) = (946, 500)

screen = pygame.display.set_mode((width, height))

pygame.display.set_caption('Duck Stock')

Icon = pygame.image.load('assets/duck.svg')
pygame.display.set_icon(Icon)

screen.fill(main_background_colour)

pygame.draw.rect(screen, secondary_background_colour, pygame.Rect(0, 0, 153, height))
pygame.draw.rect(screen, secondary_background_colour, pygame.Rect(700, 0, width - 700, height))

pygame.display.flip()

running = True

while running: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False