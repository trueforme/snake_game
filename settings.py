from typing import TextIO

import pygame as pg
import json
import os


delta_time = 120
clock = pg.time.Clock()
time, time_step = 0, 120
lives = 3
game_state = 'main_menu'
current_level = 1

window = 1200
window_height = 800
window_width = 1200
info_height = 150
tile_size = 50
game_area_height = window_height - info_height
game_area_width = window_width
random_range = (200 + tile_size // 2, 800 - tile_size // 2, tile_size)

screen = pg.display.set_mode([window_width, window_height])

directions = {pg.K_w: (0, -tile_size), pg.K_s: (0, +tile_size),
              pg.K_a: (-tile_size, 0), pg.K_d: (tile_size, 0)}




SAVE_FILE = "save_data.json"

def save_progress(level_number: int) -> None:
    print('tried to save')
    save_data = {"current_level": level_number}
    try:
        with open(SAVE_FILE, 'w') as save_file:  # type: TextIO
            json.dump(save_data, save_file)
    except (IOError, OSError) as e:
        print(f"Ошибка при сохранении прогресса: {e}")

def load_progress() -> int:
    if os.path.exists(SAVE_FILE):
        try:
            with open(SAVE_FILE, 'r') as save_file:  # type: TextIO
                save_data = json.load(save_file)
                # Проверка, что данные корректны и представляют целое число
                current_level = save_data.get("current_level", 1)
                if isinstance(current_level, int) and current_level > 0:
                    return current_level
        except (IOError, OSError, json.JSONDecodeError) as e:
            print(f"Ошибка при загрузке прогресса: {e}")
    # Если файл не существует или произошла ошибка, возвращаем 1
    return 1