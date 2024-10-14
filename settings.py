import pygame as pg
import json
import os

delta_time = 120
clock = pg.time.Clock()
time, time_step = 0, 120
lives = 3
game_state = 'main_menu'
current_level = 1

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


def save_progress(level_number: int = None, score: int = None) -> None:
    try:
        if os.path.exists(SAVE_FILE):
            with open(SAVE_FILE, 'r') as save_file:
                save_data = json.load(save_file)
        else:
            save_data = {}

        if level_number is not None:
            save_data["current_level"] = level_number

        if score is not None:
            save_data["infinite_score"] = score

        with open(SAVE_FILE, 'w') as save_file:
            json.dump(save_data, save_file)

    except (IOError, OSError, json.JSONDecodeError) as e:
        print(f"Ошибка при сохранении данных: {e}")


def load_level_number() -> int:
    if os.path.exists(SAVE_FILE):
        try:
            with open(SAVE_FILE, 'r') as save_file:
                save_data = json.load(save_file)
                current_level_number = save_data.get("current_level", 1)
                if isinstance(current_level_number,
                              int) and current_level_number > 0:
                    return current_level_number
        except (IOError, OSError, json.JSONDecodeError) as e:
            print(f"Ошибка при загрузке прогресса: {e}")
    return 1


def load_score():
    try:
        if os.path.exists(SAVE_FILE):
            with open(SAVE_FILE, 'r') as save_file:
                save_data = json.load(save_file)
            max_level = save_data.get("current_level", 1)
            max_infinite_score = save_data.get("infinite_score", 0)
        else:
            max_level = 1
            max_infinite_score = 0
    except (IOError, OSError, json.JSONDecodeError) as e:
        print(f"Ошибка при загрузке данных: {e}")
        max_level = 1
        max_infinite_score = 0

    return max_level, max_infinite_score
