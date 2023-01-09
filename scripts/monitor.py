import os
import sys
import time

import pygame

import pygame_widgets
from pygame_widgets.progressbar import ProgressBar


def load_image(name, colorkey=None):
    fullname = os.path.join('sprites', name)

    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


class Monitor(pygame.sprite.Sprite):
    image = load_image(r'monitor.png')

    def __init__(self, *group):
        super().__init__(*group)
        self.image = pygame.transform.scale(Monitor.image, (600, 400))
        self.rect = self.image.get_rect()
        self.rect.x = 275
        self.rect.y = 125
        self.status = 'play'

    def work(self):
        global work_percent

        if self.status == 'work':
            work_percent += 0.001

        return work_percent

    def play(self):
        pass

    def swipe(self):
        pass

    def update(self, *args):
        if args and args[0].type == pygame.MOUSEBUTTONDOWN and \
                self.rect.collidepoint(args[0].pos):
            if self.status == 'work':
                self.status = 'play'
            else:
                self.status = 'work'


def main():
    global work_percent

    pygame.init()
    size = width, height = (1000, 700)
    screen = pygame.display.set_mode(size)

    startTime = time.time()

    work_percent = 0
    happy_percent = 0

    all_sprites = pygame.sprite.Group()

    monitor = Monitor(all_sprites)
    work_progress_bar = ProgressBar(screen, 50, 50, 250, 20, monitor.work, curved=False)

    all_sprites.add(monitor)

    running = True

    while running:
        events = pygame.event.get()
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                running = False
            if events.type == pygame.MOUSEBUTTONDOWN:
                monitor.update(events)
            screen.fill((30, 30, 30))

        if work_progress_bar.percent == 1:
            print('YOU WIN')
            running = False

        all_sprites.update()
        all_sprites.draw(screen)

        pygame_widgets.update(events)
        pygame.display.update()


if __name__ == '__main__':
    main()
