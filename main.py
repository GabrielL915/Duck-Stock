import pygame


def initialize_game():
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Duck Stock')
    icon = pygame.image.load('assets/icon.svg')
    pygame.display.set_icon(icon)
    return screen


def load_assets():
    book = pygame.image.load('assets/book.png')
    book = pygame.transform.scale(book, (50, 70))
    duck_image = pygame.transform.scale(
        pygame.image.load('assets/duck.svg'), (100, 100))
    return book, duck_image


def handle_quit_event(event):
    if event.type == pygame.QUIT:
        return False
    return True


def handle_keydown_event(event):
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_r and (pygame.key.get_mods() & pygame.KMOD_CTRL):
            print("Ctrl+R pressed - Refreshing the screen")


def handle_mousedown_event(event):
    global dragging, offset_x, offset_y
    if event.type == pygame.MOUSEBUTTONDOWN:
        if book_rect.collidepoint(event.pos):
            dragging = True
            mouse_x, mouse_y = event.pos
            offset_x = book_rect.x - mouse_x
            offset_y = book_rect.y - mouse_y


def handle_mouseup_event(event):
    global dragging
    if event.type == pygame.MOUSEBUTTONUP and dragging:
        dragging = False
        if book_rect.x < 180:
            book_rect.x, book_rect.y = start_x, start_y


def handle_mousemotion_event(event):
    if event.type == pygame.MOUSEMOTION and dragging:
        mouse_x, mouse_y = event.pos
        book_rect.x = mouse_x + offset_x
        book_rect.y = mouse_y + offset_y


def handle_events():
    for event in pygame.event.get():
        continue_running = handle_quit_event(event)
        if not continue_running:
            return False

        handle_keydown_event(event)
        handle_mousedown_event(event)
        handle_mouseup_event(event)
        handle_mousemotion_event(event)

    return True


def update_screen():
    screen.fill(main_background_colour)
    pygame.draw.rect(screen, secondary_background_colour,
                     pygame.Rect(0, 0, 200, height))
    screen.blit(new_duck_image, duck_rect)
    screen.blit(book, book_rect)
    pygame.display.flip()


main_background_colour = (48, 66, 74)
secondary_background_colour = (12, 119, 151)
(width, height) = (946, 500)
dragging = False
start_x, start_y = 74, 400

screen = initialize_game()
book, new_duck_image = load_assets()
book_rect = book.get_rect()
book_rect.x, book_rect.y = start_x, start_y
duck_rect = new_duck_image.get_rect()
duck_rect.x, duck_rect.y = (
    200 - duck_rect.width) // 2, (height - duck_rect.height) // 2

running = True
while running:
    running = handle_events()
    update_screen()

pygame.quit()
