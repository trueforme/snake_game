import pygame as pg


window = 800
window_height = 800
window_width = 800
info_height = 150
tile_size = 50
game_area_height = window_height - info_height
game_area_width = window_width
time, time_step = 0, 120
random_range = (150 + tile_size // 2, window - tile_size // 2, tile_size)
clock = pg.time.Clock()
screen = pg.display.set_mode([window_width, window_height])
lives = 3
directions = {pg.K_w: (0, -tile_size), pg.K_s: (0, +tile_size),
              pg.K_a: (-tile_size, 0), pg.K_d: (tile_size, 0)}
