import pygame

from scripts.pygame_input import *
from scripts.pygame_button import *

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 190, 255)
YELLOW = (255, 255, 0)
GRAY = (170, 170, 170)


def main():
    pygame.init()

    size = width, height = 800, 600
    screen = pygame.display.set_mode(size)

    btn = Button()

    pygame.display.set_caption('MENU')

    start_btn = btn.button_create('START', (350, 150, 100, 35), WHITE, BLUE, on_click_button_game())
    options_btn = btn.button_create('OPTIONS', (350, 200, 100, 35), WHITE, BLUE, on_click_button_options())
    return_btn = btn.button_create('RETURN', (350, 250, 100, 35), WHITE, BLUE, on_click_button_return())
    exit_btn = btn.button_create('EXIT', (350, 300, 100, 35), WHITE, BLUE, on_click_button_exit())

    name_input_box = InputBox(300, 200, 140, 35)
    input_boxes = [name_input_box]

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            for box in input_boxes:
                box.handle_event(event)

            for box in input_boxes:
                box.update()

            screen.fill((30, 30, 30))
            for box in input_boxes:
                box.draw(screen)

            if stage == 'menu':
                btn.button_draw(screen, button_1)
                btn.button_draw(screen, button_3)
            if stage == 'return':
                btn.button_draw(screen, button_1)
            pygame.display.update()


if __name__ == '__main__':
    main()


'''
def main():
    pygame.init()
    clock = pygame.time.Clock()

    stage = 'menu'

    input_box1 = InputBox(300, 200, 140, 32)
    input_boxes = [input_box1]

    size = width, height = 800, 600
    screen = pygame.display.set_mode(size)

    screen_rect = screen.get_rect()

    pygame.display.set_caption('MENU')

    button_1 = menu.button_create("GAME", (350, 150, 100, 35), WHITE, BLUE, menu.start_game)
    button_3 = menu.button_create("EXIT", (350, 250, 100, 35), WHITE, BLUE, None)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            for box in input_boxes:
                box.handle_event(event)

        for box in input_boxes:
            box.update()

        screen.fill((30, 30, 30))
        for box in input_boxes:
            box.draw(screen)

        if stage == 'menu':
            menu.button_draw(screen, button_1)
            menu.button_draw(screen, button_3)
        if stage == 'return':
            menu.button_draw(screen, button_1)
        pygame.display.update()


if __name__ == '__main__':
    main()
    pygame.quit()
    
'''
