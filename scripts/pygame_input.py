import pygame
import sqlite3


pygame.init()


screen = pygame.display.set_mode((640, 480))
COLOR_INACTIVE = pygame.Color('lightskyblue3')
COLOR_ACTIVE = pygame.Color('dodgerblue2')
FONT = pygame.font.Font(None, 32)


class InputBox:
    def __init__(self, x, y, w, h, text=''):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.txt_surface = FONT.render(text, True, self.color)
        self.active = False

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if self.rect.collidepoint(event.pos):
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            # Change the current color of the input box.
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    print(self.text)
                    self.text = ''
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                # Re-render the text.
                self.txt_surface = FONT.render(self.text, True, self.color)

    def update(self):
        # Resize the box if the text is too long.
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, screen):
        # Blit the text.
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        # Blit the rect.
        pygame.draw.rect(screen, self.color, self.rect, 2)

    def return_value(self):
        return self.text

    def add_user(self, username, password):
        value = (username, 0000000)
        cur.execute('''INSERT INTO(username, user_password) VALUES(?, ?)''', value)
        con.commit()

    def user_in_db(self, username):
        check = cur.execute('''SELECT * FROM accounts WHERE username = ?''', (username,)).fetchall()

        if check:
            print('yep')
            return True
        return False

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

    name = input_box1.return_value()

    if not input_box1.user_in_db(name):
        input_box1.add_user(name, 000000)


if __name__ == '__main__':
    main()
    pygame.quit()
'''
