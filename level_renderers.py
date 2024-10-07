
import settings
from settings import *




def show_start_screen():
    screen.fill('black')
    font = pg.font.SysFont('Arial', 48)
    control_text = font.render("W A S D - Управление", True, (255, 255, 255))
    start_text = font.render("Нажмите любую кнопку, чтобы начать", True,
                             (255, 255, 255))
    screen.blit(control_text, (window_width // 2 - control_text.get_width() // 2,
                               window_height // 2 - control_text.get_height() // 2 - 30))
    screen.blit(start_text, (window_width // 2 - start_text.get_width() // 2,
                             window_height // 2 - start_text.get_height() // 2 + 30))
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

    screen.blit(control_text, (window_width // 2 - control_text.get_width() // 2,
                               window_height // 2 - control_text.get_height() // 2 - 60))
    screen.blit(start_text1, (window_width // 2 - start_text1.get_width() // 2,
                              window_height // 2 - start_text1.get_height() // 2))
    screen.blit(start_text2, (window_width // 2 - start_text2.get_width() // 2,
                              window_height // 2 - start_text2.get_height() // 2 + 60))
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
    screen.blit(control_text, (window_width // 2 - control_text.get_width() // 2,
                               window_height // 2 - control_text.get_height() // 2 - 60))
    screen.blit(start_text1, (window_width // 2 - start_text1.get_width() // 2,
                              window_height // 2 - start_text1.get_height() // 2))
    pg.display.flip()

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()
            if event.type == pg.KEYDOWN:
                return


def show_main_menu():
    screen.fill('black')
    font = pg.font.SysFont('Arial', 48)

    # Тексты кнопок
    new_game_text = font.render("Новая игра", True, (255, 255, 255))
    load_game_text = font.render("Загрузить сохранение", True,
                                 (255, 255, 255))
    exit_text = font.render("Выход", True, (255, 255, 255))

    infinite_level_text = font.render("Бесконечный режим", True, (255, 255, 255))

    # Координаты кнопок
    new_game_rect = new_game_text.get_rect(
        center=(window_width // 2, window_height // 2 - 120))
    load_game_rect = load_game_text.get_rect(center=(window_width // 2, window_height // 2))
    infinite_game_rect = infinite_level_text.get_rect(center=(window_width // 2, window_height //2 + 120))
    exit_rect = exit_text.get_rect(center=(window_width // 2, window_height // 2 + 240))

    # Отрисовка кнопок
    screen.blit(new_game_text, new_game_rect)
    screen.blit(load_game_text, load_game_rect)
    screen.blit(infinite_level_text,infinite_game_rect)
    screen.blit(exit_text, exit_rect)
    pg.display.flip()

    # Ждем, пока игрок не нажмет на одну из кнопок
    waiting = True
    while waiting:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()
            if event.type == pg.MOUSEBUTTONDOWN:
                # Получаем позицию клика
                mouse_pos = pg.mouse.get_pos()

                # Проверяем, попал ли клик в одну из кнопок
                if new_game_rect.collidepoint(mouse_pos):
                    waiting = False  # Запуск новой игры
                    save_progress(1)

                if load_game_rect.collidepoint(mouse_pos):
                    settings.current_level = load_progress()
                    waiting = False
                    return 'level'
                if infinite_game_rect.collidepoint(mouse_pos):
                    waiting = False
                    return 'infinite'
                elif exit_rect.collidepoint(mouse_pos):
                    pg.quit()
                    exit()


def show_post_level_screen(level_number):
    screen.fill('black')
    font = pg.font.SysFont('Arial', 48)

    next_level_text = font.render("Следующий уровень", True, (255, 255, 255))
    save_progress_text = font.render("Сохранить прогресс", True,
                                     (255, 255, 255))

    next_level_rect = next_level_text.get_rect(
        center=(window_width // 2, window_height // 2 - 40))
    save_progress_rect = save_progress_text.get_rect(
        center=(window_width // 2, window_height // 2 + 40))

    screen.blit(next_level_text, next_level_rect)
    screen.blit(save_progress_text, save_progress_rect)
    pg.display.flip()

    waiting = True
    while waiting:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()
            if event.type == pg.MOUSEBUTTONDOWN:
                mouse_pos = pg.mouse.get_pos()

                # Проверяем, на какую кнопку кликнул игрок
                if next_level_rect.collidepoint(mouse_pos):
                    waiting = False
                    return "next"
                elif save_progress_rect.collidepoint(mouse_pos):
                    save_progress(level_number)
                    print(
                        f"Progress saved at level {level_number}!")  # Для отладки


