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
    open_book = pygame.image.load('assets/open-book.png')
    open_book = pygame.transform.scale(open_book, (500, 400))
    duck_image = pygame.transform.scale(
        pygame.image.load('assets/duck.svg'), (100, 100))
    return book, open_book, duck_image


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
    screen.blit(current_book, book_rect)
    pygame.display.flip()


main_background_colour = (48, 66, 74)
secondary_background_colour = (12, 119, 151)
(width, height) = (946, 500)
dragging = False
start_x, start_y = 74, 400

screen = initialize_game()
book, open_book, new_duck_image = load_assets()
book_rect = book.get_rect()
book_rect.x, book_rect.y = start_x, start_y
duck_rect = new_duck_image.get_rect()
duck_rect.x, duck_rect.y = (
    200 - duck_rect.width) // 2, (height - duck_rect.height) // 2
current_book = book
book_opened = False

running = True
while running:
    running = handle_events()

    # This block should be inside the while loop
    if book_rect.x > 180 and not book_opened:
        book_opened = True
        current_book = open_book

        # Choose font and size
        font = pygame.font.SysFont('Arial', 24)

        # Render the text
        text_surface = font.render('TESTE', True, (0, 0, 0))  # Text color is black

        # Position the text
        text_x = 90  # Adjust these values as needed
        text_y = 20

        # Blit the text onto the open book
        current_book.blit(text_surface, (text_x, text_y))
    elif book_rect.x <= 180:
        current_book = book
        book_opened = False

    update_screen()

pygame.quit()

