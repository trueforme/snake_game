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
            running = False






def get_level_by_number(number):
    if number == 1:
        return CommonLevel(Snake(), Food(),  lives, Wall(), GameCells(), SpecialFood(), 2, screen)
    if number == 2:
        return LevelStaticObstacles(Snake(), Food(), lives, Wall(), GameCells(),
                                    SpecialFood(), 3, screen)
    if number == 3:
        return LevelDynamicObstacles(Snake(), Food(), lives, Wall(), GameCells(),
                                     SpecialFood(), 4, screen)
    if number == 4:
        return InfiniteLevel(Snake(), Food(), lives, Wall(), GameCells(),
                                     SpecialFood(), 100, screen)


def main():
    pg.init()
    clock_main = clock
    game_state = 'main_menu'  # Начальное состояние игры - главное меню
    current_level_number = load_progress()
    max_levels = 3  # Количество уровней в игре

    while True:

        if game_state == 'main_menu':
            game_state = show_main_menu()  # Отображение главного меню  # Если игрок начал игру


        elif game_state == 'level':
            level = get_level_by_number(current_level_number)
            run(level)
            show_post_level_screen(current_level_number)
            if current_level_number >= max_levels:
                game_state = 'game_over'
            else:
                game_state = 'between_levels'

        elif game_state == 'infinite':
            level = get_level_by_number(4)
            run(level)

        elif game_state == 'between_levels':
            show_between_screen()  # Экран между уровнями
            current_level_number += 1
            game_state = 'level'  # Переходим к следующему уровню


        elif game_state == 'game_over':
            show_end_screen()
            show_main_menu()
            game_state = 'main_menu'  # Возвращаемся в главное меню для перезапуска

        clock_main.tick(15)  # Ограничиваем количество кадров в секунду




main()
