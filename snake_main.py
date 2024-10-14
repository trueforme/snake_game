from Levels import *
import pygame as pg



def run(level):
    level.reset_level()
    running = True
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()
            if event.type == pg.KEYDOWN:
                level.snake.get_new_direction(event.key)
        level.draw_basics()
        level.draw_info_panel()
        level.check_death()
        level.check_eating()
        level.update_game_cells()
        level.tick_game_timings()

        if level.snake.length - 1 >= level.goal:
            settings.game_state = "between_levels"
            return
        if settings.game_state in ["main_menu", "game_over"]:
            return


def get_level_by_number(number):
    if number == 1:
        return CommonLevel(Snake(), Food(), lives, Wall(), GameCells(),
                           SpecialFood(), 2, screen)
    if number == 2:
        return LevelStaticObstacles(Snake(), Food(), lives, Wall(),
                                    GameCells(),
                                    SpecialFood(), 3, screen)
    if number == 3:
        return LevelDynamicObstacles(Snake(), Food(), lives, Wall(),
                                     GameCells(),
                                     SpecialFood(), 4, screen)
    if number == 8:
        return InfiniteLevel(Snake(), Food(), 1, Wall(), GameCells(),
                             SpecialFood(), 777, screen)


def main():
    pg.init()
    clock_main = clock
    settings.current_level = load_level_number()
    max_level_number = 3

    while True:
        print(settings.current_level)
        if settings.game_state == 'main_menu':
            settings.game_state = show_main_menu()

        if settings.game_state == 'new_game':
            settings.current_level = 1
            settings.game_state = 'level'

        if settings.game_state == 'level':
            level = get_level_by_number(settings.current_level)
            run(level)

        if settings.game_state == 'infinite':
            level = get_level_by_number(8)
            run(level)

            show_infinite_end_screen(level.snake.length)

            settings.game_state = 'main_menu'
        if settings.game_state == 'between_levels':
            settings.current_level = show_post_level_screen(settings.current_level)
            settings.game_state = 'level'
            if settings.current_level > max_level_number:
                show_end_screen()
                settings.game_state = 'main_menu'

        if settings.game_state == 'game_over':
            settings.game_state = 'main_menu'

        if settings.game_state == 'table_record':
            show_table_record_screen()
            settings.game_state = 'main_menu'

        clock_main.tick(60)


main()
