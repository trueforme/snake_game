import settings
from settings import *
import time


def show_start_screen():
    screen.fill('black')
    font = pg.font.SysFont('Arial', 48)
    control_text = font.render("W A S D - Управление", True, (255, 255, 255))
    start_text = font.render("Нажмите любую кнопку, чтобы начать", True,
                             (255, 255, 255))
    screen.blit(control_text,
                (window_width // 2 - control_text.get_width() // 2,
                 window_height // 2 - control_text.get_height() // 2 - 30))
    screen.blit(start_text, (window_width // 2 - start_text.get_width() // 2,
                             window_height // 2 - start_text.get_height() // 2 + 30))
    pg.display.flip()

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
    screen.blit(control_text,
                (window_width // 2 - control_text.get_width() // 2,
                 window_height // 2 - control_text.get_height() // 2 - 60))
    start_text1 = font.render("Нажмите любую кнопку,", True, (255, 255, 255))
    start_text2 = font.render("чтобы начать следующий", True, (255, 255, 255))

    screen.blit(start_text1, (window_width // 2 - start_text1.get_width() // 2,
                              window_height // 2 - start_text1.get_height() // 2))
    screen.blit(start_text2, (window_width // 2 - start_text2.get_width() // 2,
                              window_height // 2 - start_text2.get_height() // 2 + 60))
    pg.display.flip()
    time.sleep(2)
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
    text2 = font.render("Нажмите любую кнопку", True, (255, 255, 255))

    screen.blit(control_text,
                (window_width // 2 - control_text.get_width() // 2,
                 window_height // 2 - control_text.get_height() // 2 - 60))
    screen.blit(start_text1, (window_width // 2 - start_text1.get_width() // 2,
                              window_height // 2 - start_text1.get_height() // 2))
    screen.blit(text2, (window_width // 2 - text2.get_width() // 2,
                        window_height // 2 - text2.get_height() // 2 + 120))
    pg.display.flip()
    time.sleep(1)
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()
            if event.type == pg.KEYDOWN:
                return


def show_death_screen():
    screen.fill('black')
    font = pg.font.SysFont('Arial', 48)
    death_text = font.render("Змейка стукнулась..", True, (255, 255, 255))
    retry_text = font.render("Нажмите любую кнопку", True, (255, 255, 255))

    screen.blit(death_text, (window_width // 2 - death_text.get_width() // 2,
                             window_height // 2 - death_text.get_height() // 2 - 60))
    screen.blit(retry_text, (window_width // 2 - death_text.get_width() // 2,
                             window_height // 2 - death_text.get_height() // 2 + 60))
    pg.display.flip()
    time.sleep(1)
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

    new_game_text = font.render("Новая игра", True, (255, 255, 255))
    load_game_text = font.render("Загрузить сохранение", True, (255, 255, 255))
    exit_text = font.render("Выход", True, (255, 255, 255))
    table_record_text = font.render("Таблица рекордов", True, (255, 255, 255))
    infinite_level_text = font.render("Бесконечный режим", True,
                                      (255, 255, 255))

    new_game_rect = new_game_text.get_rect(
        center=(window_width // 2, window_height // 2 - 120))
    load_game_rect = load_game_text.get_rect(
        center=(window_width // 2, window_height // 2))
    infinite_game_rect = infinite_level_text.get_rect(
        center=(window_width // 2, window_height // 2 + 120))
    table_record_rect = table_record_text.get_rect(
        center=(window_width // 2, window_height // 2 + 240))
    exit_rect = exit_text.get_rect(
        center=(window_width // 2, window_height // 2 + 360))

    waiting = True
    while waiting:
        mouse_pos = pg.mouse.get_pos()

        screen.fill('black')
        screen.blit(new_game_text, new_game_rect)
        screen.blit(load_game_text, load_game_rect)
        screen.blit(infinite_level_text, infinite_game_rect)
        screen.blit(exit_text, exit_rect)
        screen.blit(table_record_text, table_record_rect)

        if new_game_rect.collidepoint(mouse_pos):
            pg.draw.rect(screen, (255, 255, 255),
                         new_game_rect.inflate(20, 10), 5)
        if load_game_rect.collidepoint(mouse_pos):
            pg.draw.rect(screen, (255, 255, 255),
                         load_game_rect.inflate(20, 10), 5)
        if infinite_game_rect.collidepoint(mouse_pos):
            pg.draw.rect(screen, (255, 255, 255),
                         infinite_game_rect.inflate(20, 10), 5)
        if table_record_rect.collidepoint(mouse_pos):
            pg.draw.rect(screen, (255, 255, 255),
                         table_record_rect.inflate(20, 10), 5)
        if exit_rect.collidepoint(mouse_pos):
            pg.draw.rect(screen, (255, 255, 255), exit_rect.inflate(20, 10), 5)

        pg.display.flip()

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()
            if event.type == pg.MOUSEBUTTONDOWN:
                if new_game_rect.collidepoint(mouse_pos):
                    return "new_game"

                if load_game_rect.collidepoint(mouse_pos):
                    settings.current_level = load_level_number()
                    return 'level'
                if infinite_game_rect.collidepoint(mouse_pos):
                    return 'infinite'
                if table_record_rect.collidepoint(mouse_pos):
                    return 'table_record'
                elif exit_rect.collidepoint(mouse_pos):
                    pg.quit()
                    exit()


def show_post_level_screen(level_number):
    screen.fill('black')
    font = pg.font.SysFont('Arial', 48)
    control_text = font.render("Уровень пройден!", True, (255, 255, 255))
    next_level_text = font.render("Следующий уровень", True, (255, 255, 255))
    save_progress_text = font.render("Сохранить прогресс", True,
                                     (255, 255, 255))

    control_text_rect = control_text.get_rect(
        center=(window_width // 2, window_height // 2 - 120))
    next_level_rect = next_level_text.get_rect(
        center=(window_width // 2, window_height // 2))
    save_progress_rect = save_progress_text.get_rect(
        center=(window_width // 2, window_height // 2 + 120))

    screen.blit(control_text, control_text_rect)
    screen.blit(next_level_text, next_level_rect)
    screen.blit(save_progress_text, save_progress_rect)
    pg.display.flip()

    waiting = True
    while waiting:
        mouse_pos = pg.mouse.get_pos()

        screen.fill('black')
        screen.blit(control_text, control_text_rect)
        screen.blit(next_level_text, next_level_rect)
        screen.blit(save_progress_text, save_progress_rect)

        if next_level_rect.collidepoint(mouse_pos):
            pg.draw.rect(screen, (255, 255, 255),
                         next_level_rect.inflate(20, 10), 5)
        if save_progress_rect.collidepoint(mouse_pos):
            pg.draw.rect(screen, (255, 255, 255),
                         save_progress_rect.inflate(20, 10), 5)

        pg.display.flip()

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()
            if event.type == pg.MOUSEBUTTONDOWN:
                if next_level_rect.collidepoint(mouse_pos):
                    return level_number + 1
                elif save_progress_rect.collidepoint(mouse_pos):
                    save_progress(level_number=level_number)


def show_infinite_end_screen(snake_length):
    screen.fill('black')
    font = pg.font.SysFont('Arial', 48)

    score_text = font.render(f"Количество набранных очков: {snake_length - 1}",
                             True, (255, 255, 255))
    save_text = font.render("Сохранить результат?", True, (255, 255, 255))
    yes_text = font.render("Да", True, (255, 255, 255))
    no_text = font.render("Нет", True, (255, 255, 255))

    screen.blit(score_text, (
        window_width // 2 - score_text.get_width() // 2,
        window_height // 2 - 100))
    screen.blit(save_text, (
        window_width // 2 - save_text.get_width() // 2, window_height // 2))

    yes_rect = yes_text.get_rect(
        center=(window_width // 2 - 100, window_height // 2 + 100))
    no_rect = no_text.get_rect(
        center=(window_width // 2 + 100, window_height // 2 + 100))

    screen.blit(yes_text, yes_rect)
    screen.blit(no_text, no_rect)
    pg.display.flip()

    waiting = True
    while waiting:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()
            if event.type == pg.MOUSEBUTTONDOWN:
                mouse_pos = pg.mouse.get_pos()
                if yes_rect.collidepoint(mouse_pos):
                    save_progress(
                        score=snake_length)
                    return
                if no_rect.collidepoint(mouse_pos):
                    return


def show_table_record_screen():
    max_level, max_infinite_score = load_score()

    screen.fill('black')
    font = pg.font.SysFont('Arial', 48)

    level_text = font.render(f"Максимальный пройденный уровень: {max_level}",
                             True, (255, 255, 255))
    score_text = font.render(
        f"Максимальные очки в бесконечном режиме: {max_infinite_score}", True,
        (255, 255, 255))
    ok_text = font.render("OK", True, (255, 255, 255))

    screen.blit(level_text, (
        window_width // 2 - level_text.get_width() // 2,
        window_height // 2 - 100))
    screen.blit(score_text, (
        window_width // 2 - score_text.get_width() // 2, window_height // 2))

    ok_rect = ok_text.get_rect(
        center=(window_width // 2, window_height // 2 + 100))

    waiting = True
    while waiting:
        mouse_pos = pg.mouse.get_pos()

        screen.fill('black')
        screen.blit(level_text, (
            window_width // 2 - level_text.get_width() // 2,
            window_height // 2 - 100))
        screen.blit(score_text, (
            window_width // 2 - score_text.get_width() // 2,
            window_height // 2))

        screen.blit(ok_text, ok_rect)

        if ok_rect.collidepoint(mouse_pos):
            pg.draw.rect(screen, (255, 255, 255), ok_rect.inflate(20, 10),
                         5)

        pg.display.flip()

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()
            if event.type == pg.MOUSEBUTTONDOWN:
                if ok_rect.collidepoint(mouse_pos):
                    waiting = False
