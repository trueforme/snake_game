from Levels import *
import pygame as pg



SAVE_FILE = "save_data.json"

def run(level):
    level.reset_level()  # Сброс уровня для инициализации всех объектов
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

        # Проверяем, достиг ли игрок цели уровня
        if level.snake.length - 1 >= level.goal:
            running = False  # Заканчиваем выполнение текущего уровня
        level.check_death()
        level.check_eating()
        level.update_game_cells()
        level.tick_game_timings()





def get_level_by_number(number):
    if number == 1:
        return CommonLevel(Snake(), Food(),  lives, Wall(), GameCells(), SpecialFood(), 2, screen)
    if number == 2:
        return LevelStaticObstacles(Snake(), Food(), lives, Wall(), GameCells(),
                                    SpecialFood(), 3, screen)
    if number == 3:
        return LevelDynamicObstacles(Snake(), Food(), lives, Wall(), GameCells(),
                                     SpecialFood(), 4, screen)


def main():
    pg.init()
    clock_main = clock
    game_state = 'main_menu'  # Начальное состояние игры - главное меню
    curr_level = load_progress()
    max_levels = 3  # Количество уровней в игре
    levels_completed = max_levels - curr_level

    while True:
        if game_state == 'main_menu':
            show_main_menu()  # Отображение главного меню
            if handle_main_menu_events():  # Если игрок начал игру
                game_state = 'level'

        elif game_state == 'level':
            level = get_level_by_number(curr_level)
            run(level)
            levels_completed += 1
            show_post_level_screen(curr_level)
            if levels_completed >= max_levels:
                game_state = 'game_over'
            else:
                game_state = 'between_levels'

        elif game_state == 'between_levels':
            show_between_screen()  # Экран между уровнями
            curr_level += 1
            game_state = 'level'  # Переходим к следующему уровню

        elif game_state == 'game_over':
            show_end_screen()  # Экран завершения игры
            game_state = 'main_menu'  # Возвращаемся в главное меню для перезапуска

        clock_main.tick(30)  # Ограничиваем количество кадров в секунду

def handle_main_menu_events():
    waiting = True
    while waiting:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()
            if event.type == pg.KEYDOWN:
                return True  # Игрок нажал клавишу для начала игры


main()
