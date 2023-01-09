import pygame


WHITE = (255, 255, 255)
BLACK = (0,  0,  0)

RED = (255, 0,  0)
GREEN = (0, 255,  0)
BLUE = (0, 0, 255)

YELLOW = (255, 255, 0)


class Button:
    def __init__(self):
        pass

    def button_create(self, text, rect, inactive_color, active_color, action):
        font = pygame.font.Font(None, 40)

        button_rect = pygame.Rect(rect)

        text = font.render(text, True, BLACK)
        text_rect = text.get_rect(center=button_rect.center)

        return [text, text_rect, button_rect, inactive_color, active_color, action, False]

    def button_check(self, info, event):
        text, text_rect, rect, inactive_color, active_color, action, hover = info

        if event.type == pygame.MOUSEMOTION:
            # hover = True/False
            info[-1] = rect.collidepoint(event.pos)

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if hover and action:
                action()

    def button_draw(self, screen, info):
        text, text_rect, rect, inactive_color, active_color, action, hover = info

        if hover:
            color = active_color
        else:
            color = inactive_color

        pygame.draw.rect(screen, color, rect)
        screen.blit(text, text_rect)


def on_click_button_game():
    global stage
    stage = 'game'

    print('You clicked Button 1')


def on_click_button_options():
    global stage
    stage = 'options'

    print('You clicked Button 2')


def on_click_button_exit():
    global stage
    global running

    stage = 'exit'
    running = False

    print('You clicked Button 3')


def on_click_button_return():
    global stage
    stage = 'menu'

    print('You clicked Button Return')


btn = Button()
pygame.init()
screen = pygame.display.set_mode((800, 600))
screen_rect = screen.get_rect()

stage = 'menu'

button_1 = btn.button_create("GAME", (300, 100, 200, 75), RED, GREEN, on_click_button_game)
button_2 = btn.button_create("OPTIONS", (300, 200, 200, 75), RED, GREEN, on_click_button_options)
button_3 = btn.button_create("EXIT", (300, 300, 200, 75), RED, GREEN, on_click_button_exit)

button_return = btn.button_create("RETURN", (300, 400, 200, 75), RED, GREEN, on_click_button_return)
running = True

'''
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if stage == 'menu':
            btn.button_check(button_1, event)
            btn.button_check(button_2, event)
            btn.button_check(button_3, event)
        elif stage == 'game':
            btn.button_check(button_return, event)
        elif stage == 'options':
            btn.button_check(button_return, event)

    screen.fill(BLACK)

    if stage == 'menu':
        btn.button_draw(screen, button_1)
        btn.button_draw(screen, button_2)
        btn.button_draw(screen, button_3)
    elif stage == 'game':
        btn.button_draw(screen, button_return)
    elif stage == 'options':
        btn.button_draw(screen, button_return)
    pygame.display.update()

pygame.quit()
'''
