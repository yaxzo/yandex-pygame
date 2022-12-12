import pygame
import pygame_menu
from pygame import display


class MenuWindow:
    def __init__(self):
        pass


def main():
    pygame.init()

    window = pygame.display.set_mode((600, 400))
    menu_window = pygame_menu.Menu('', 600, 400, theme=pygame_menu.themes.THEME_DARK)
    menu = MenuWindow()
    menu_window.mainloop(window)

    running = True
    while running:
        pygame.display.set_caption('Menu')

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        pygame.display.flip()
    pygame.quit()


if __name__ == '__main__':
    main()
