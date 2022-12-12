import pygame
import pygame_menu

pygame.init()
surface = pygame.display.set_mode((600, 400))


def set_difficulty(value, difficulty):
    # Do the job here !
    pass


def start_the_game():
    # Do the job here !
    pass


menu = pygame_menu.Menu('GAME NAME', 600, 400, theme=pygame_menu.themes.THEME_DARK)

menu.add.text_input('Имя: ', default='Георгий')
menu.add.selector('Сложность: ', [('Легко', 1), ('Средне', 2)], onchange=set_difficulty)
menu.add.button('Играть', start_the_game)
menu.add.button('Выйти', pygame_menu.events.EXIT)

menu.mainloop(surface)
