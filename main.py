import pygame

main_background_colour = (48, 66, 74)
secondary_background_colour = (12, 119, 151)
(width, height) = (946, 500)

screen = pygame.display.set_mode((width, height))

pygame.display.set_caption('Duck Stock')

Icon = pygame.image.load('assets/icon.svg')
pygame.display.set_icon(Icon)

screen.fill(main_background_colour)

pygame.draw.rect(screen, secondary_background_colour,
                 pygame.Rect(0, 0, 153, height))



open_book = pygame.image.load('assets/open-book.png')
open_book_rect = open_book.get_rect()


duck_image = pygame.image.load('assets/duck.svg')

image_size = (100, 100)
new_duck_image = pygame.transform.scale(duck_image, image_size)
duck_rect = new_duck_image.get_rect()


duck_rect.x = (153 - duck_rect.width) // 2
duck_rect.y = (height - duck_rect.height) // 2

screen.blit(new_duck_image, duck_rect)

pygame.display.flip()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
