from settings import *


def show_start_screen():
    screen.fill('black')
    font = pg.font.SysFont('Arial', 48)
    control_text = font.render("W A S D - Управление", True, (255, 255, 255))
    start_text = font.render("Нажмите любую кнопку, чтобы начать", True,
                             (255, 255, 255))
    screen.blit(control_text, (window // 2 - control_text.get_width() // 2,
                               window // 2 - control_text.get_height() // 2 - 30))
    screen.blit(start_text, (window // 2 - start_text.get_width() // 2,
                             window // 2 - start_text.get_height() // 2 + 30))
    pg.display.flip()

    # Ждем, пока игрок не нажмет клавишу движения
    waiting = True
    while waiting:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()
            if event.type == pg.KEYDOWN:
                waiting = False


def show_between_screen():
    screen.fill('black')
    font = pg.font.SysFont('Arial', 48)
    control_text = font.render("Уровень пройден!", True, (255, 255, 255))
    start_text1 = font.render("Нажмите любую кнопку,", True, (255, 255, 255))
    start_text2 = font.render("чтобы начать следующий", True, (255, 255, 255))

    screen.blit(control_text, (window // 2 - control_text.get_width() // 2,
                               window // 2 - control_text.get_height() // 2 - 60))
    screen.blit(start_text1, (window // 2 - start_text1.get_width() // 2,
                              window // 2 - start_text1.get_height() // 2))
    screen.blit(start_text2, (window // 2 - start_text2.get_width() // 2,
                              window // 2 - start_text2.get_height() // 2 + 60))
    pg.display.flip()

    waiting = True
    while waiting:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()
            if event.type == pg.KEYDOWN:
                waiting = False


def show_end_screen():
    screen.fill('black')
    font = pg.font.SysFont('Arial', 48)
    control_text = font.render("Поздравляем!", True, (255, 255, 255))
    start_text1 = font.render("Все уровни пройдены!", True, (255, 255, 255))
    screen.blit(control_text, (window // 2 - control_text.get_width() // 2,
                               window // 2 - control_text.get_height() // 2 - 60))
    screen.blit(start_text1, (window // 2 - start_text1.get_width() // 2,
                              window // 2 - start_text1.get_height() // 2))
    pg.display.flip()

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()
            if event.type == pg.KEYDOWN:
                pg.quit()
                exit()
