import settings
from Levels import *
import pygame as pg

SAVE_FILE = "save_data.json"

def run(level):
    level.reset_level()
    running = True
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()
            if event.type == pg.KEYDOWN:
                level.snake.direction = level.snake.get_new_direction(event.key)
        level.draw_basics()
        level.draw_info_panel()
        level.check_death()
        level.check_eating()
        level.update_game_cells()
        level.tick_game_timings()

        if level.snake.length - 1 >= level.goal:
            settings.game_state = "between_levels"
            return
        if settings.game_state in ["main_menu","game_over"]:
            return






def get_level_by_number(number):
    if number == 1:
        return CommonLevel(Snake(), Food(),  lives, Wall(), GameCells(), SpecialFood(), 2, screen)
    if number == 2:
        return LevelStaticObstacles(Snake(), Food(), lives, Wall(), GameCells(),
                                    SpecialFood(), 3, screen)
    if number == 3:
        return LevelDynamicObstacles(Snake(), Food(), lives, Wall(), GameCells(),
                                     SpecialFood(), 4, screen)
    if number == 8:
        return InfiniteLevel(Snake(), Food(), 1, Wall(), GameCells(),
                                     SpecialFood(), 100, screen)


def main():
    pg.init()
    clock_main = clock
    current_level_number = load_progress()
    max_level_number = 3  # Количество уровней в игре

    while True:
        if settings.game_state == 'main_menu':
            settings.game_state = show_main_menu()

        if settings.game_state == 'new_game':
            current_level_number = 1
            settings.game_state = 'level'

        if settings.game_state == 'level':
            level = get_level_by_number(current_level_number)
            run(level)

            if (current_level_number == max_level_number and
                    settings.game_state != 'game_over'):
                settings.game_state = 'main_menu'
                show_end_screen()
        print(settings.game_state)

        if settings.game_state == 'infinite':
            level = get_level_by_number(8)
            run(level)

        if settings.game_state == 'between_levels':
            current_level_number = show_post_level_screen(current_level_number)
            print(current_level_number)
            # Экран между уровнями
            if current_level_number > max_level_number:
                show_end_screen()
            settings.game_state = 'level'  # Переходим к следующему уровню


        if settings.game_state == 'game_over':
            settings.game_state = 'main_menu' # Возвращаемся в главное меню для перезапуска

        clock_main.tick(15)  # Ограничиваем количество кадров в секунду




main()
