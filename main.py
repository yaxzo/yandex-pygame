import pygame

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 190, 255)
YELLOW = (255, 255, 0)
GRAY = (170, 170, 170)


# class for create menu
class Menu:
    # initialization class
    def __init__(self):
        pass

    # func for create button in menu window
    def button_create(self, text, rect, inactive_color, active_color, action):
        font = pygame.font.Font(None, 30)

        button_rect = pygame.Rect(rect)

        text = font.render(text, True, BLACK)
        text_rect = text.get_rect(center=button_rect.center)

        return [text, text_rect, button_rect, inactive_color, active_color, action, False]

    # func for start game
    def start_game(self):
        global stage

        stage = 'game'

    def btn_return_click(self):
        global stage

        stage = 'menu'

    # func for check which btn push
    def button_check(self, information, event):
        text, text_rect, rect, inactive_color, active_color, action, hover = information

        if event.type == pygame.MOUSEMOTION:
            # hover = True/False
            information[-1] = rect.collidepoint(event.pos)

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if hover and action:
                action()

    # func for draw btn in window
    def button_draw(self, screen, info):
        text, text_rect, rect, inactive_color, active_color, action, hover = info

        if hover:
            color = active_color
        else:
            color = inactive_color

        pygame.draw.rect(screen, color, rect)
        screen.blit(text, text_rect)


def main():
    pygame.init()
    # game stage
    stage = 'menu'

    menu = Menu()

    size = width, height = 800, 600
    screen = pygame.display.set_mode(size)

    screen_rect = screen.get_rect()

    pygame.display.set_caption('MENU')

    button_1 = menu.button_create("GAME", (350, 150, 100, 35), WHITE, BLUE, menu.start_game)
    button_2 = menu.button_create("OPTIONS", (350, 200, 100, 35), WHITE, BLUE, None)
    button_3 = menu.button_create("EXIT", (350, 250, 100, 35), WHITE, BLUE, None)

    button_return = menu.button_create("RETURN", (300, 400, 200, 75), WHITE, BLUE, menu.btn_return_click)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if stage == 'menu':
                menu.button_check(button_1, event)
                menu.button_check(button_2, event)
                menu.button_check(button_3, event)
            if stage == 'game':
                menu.button_check(button_return, event)

        screen.fill(GRAY)
        pygame.display.flip()

        if stage == 'menu':
            menu.button_draw(screen, button_1)
            menu.button_draw(screen, button_2)
            menu.button_draw(screen, button_3)
        elif stage == 'option':
            menu.button_draw(screen, button_2)
        pygame.display.update()


if __name__ == '__main__':
    main()
