import pygame
import sqlite3


def main():
    clock = pygame.time.Clock()
    input_box1 = InputBox(100, 100, 140, 35)
    input_box2 = InputBox(100, 300, 140, 35)
    input_boxes = [input_box1, input_box2]
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                username = input_box1.return_value()
                print(username)
                result = input_box1.user_in_db(username)
                password = input_box2.return_value()
                print(password)
                if not result:
                    input_box1.add_user(username, password)
                running = False

                con.close()
            for box in input_boxes:
                box.handle_event(event)

        for box in input_boxes:
            box.update()

        screen.fill((30, 30, 30))
        for box in input_boxes:
            box.draw(screen)

        pygame.display.flip()
        clock.tick(30)


if __name__ == '__main__':
    main()
    pygame.quit()
