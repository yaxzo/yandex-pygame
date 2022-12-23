import pygame
import sqlite3


#
class Buttons:
    # func for create button in menu window
    def button_create(self, text, rect, inactive_color, active_color, action):
        font = pygame.font.Font(None, 30)

        button_rect = pygame.Rect(rect)

        text = font.render(text, True, (0, 0, 0))
        text_rect = text.get_rect(center=button_rect.center)

        return [text, text_rect, button_rect, inactive_color, active_color, action, False]

    # func for start game
    def join_in(self, login, password):
        con = sqlite3.connect("Game.db")
        cur = con.cursor()
        result = cur.execute(f"""SELECT * FROM accounts
                                            WHERE login = 'Murmansk' and password = '1916'""").fetchall()
        result = result[0]
        if len(result) == 1:
            print('Good')

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


#
class Board:
    def __init__(self, width, height, numwe, numhe):
        self.width = numwe
        self.height = numhe
        self.board = [[0] * numwe for _ in range(numhe)]
        self.left = 10
        self.top = 10
        self.cell_size_x = (width - 20) // numwe
        self.cell_size_y = (height - 20) // numhe

    def set_view(self, left, top, cell_size_x, cell_size_y):
        self.left = left
        self.top = top
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y

    def render(self, screen):
        for y in range(self.height):
            for x in range(self.width):
                pygame.draw.rect(screen, (0, 0, 0), (
                    x * self.cell_size_x + self.left, y * self.cell_size_y + self.top, self.cell_size_x,
                    self.cell_size_y),
                                 1)

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        self.on_click(cell)

    def on_click(self, cell):
        print(cell)

    def get_cell(self, mouse_pos):
        x = mouse_pos[0]
        y = mouse_pos[1]
        if x > self.left and y > self.top:
            return ((x - self.left) // self.cell_size_x, (y - self.top) // self.cell_size_y)
        return None


if __name__ == '__main__':
    pygame.init()
    size = width, height = 800, 600
    screen = pygame.display.set_mode(size)
    board = Board(width, height, 10, 10)
    running = True
    login = None
    password = None
    # nickname = 'Введите имя'
    # password = 'Введите пароль'
    #
    font1 = pygame.font.Font(None, 80)
    font2 = pygame.font.Font(None, 60)
    text1 = font1.render('ЗА РАБОТУ', False, '#FF0000')
    text2 = font2.render('Введите имя', False, '#000000')
    text3 = font2.render('Введите пароль', False, '#000000')
    #
    b=Buttons()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                board.get_click(event.pos)
        screen.fill((255, 255, 255))
        board.render(screen)
        login = 0
        password = 0
        #
        screen.blit(text1, (board.cell_size_x * 3 + 5, board.cell_size_y * 2 + 20))
        #
        pygame.draw.rect(screen, (200, 200, 200), (board.cell_size_x * 3 + 10, board.cell_size_y * 4 + 10,
                                                   board.cell_size_x * 4, board.cell_size_y * 2 / 3), 0)
        pygame.draw.rect(screen, (0, 255, 0), (board.cell_size_x * 3 + 10, board.cell_size_y * 4 + 10,
                                               board.cell_size_x * 4, board.cell_size_y * 2 / 3
                                               ), 4)
        screen.blit(text2, (board.cell_size_x * 3 + 10, board.cell_size_y * 4 + 10))
        #
        pygame.draw.rect(screen, (200, 200, 200), (board.cell_size_x * 3 + 10, board.cell_size_y * 6 + 10,
                                                   board.cell_size_x * 4, board.cell_size_y * 2 / 3), 0)
        pygame.draw.rect(screen, (0, 255, 0), (board.cell_size_x * 3 + 10, board.cell_size_y * 6 + 10,
                                               board.cell_size_x * 4, board.cell_size_y * 2 / 3
                                               ), 4)
        screen.blit(text3, (board.cell_size_x * 3 + 10, board.cell_size_y * 6 + 10))
        #
        button_1 = b.button_create("Войти", (350, 150, 100, 35), 'A9A9A9', '00FF00', b.join_in(login, password))
        b.button_draw()
        # button_1 = menu.button_create("текст", (коордх, коорду, ширина , высота), задний фон без наведения, фон с наведением, функция)
        #
        pygame.display.flip()
