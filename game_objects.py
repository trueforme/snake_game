import random

from random import randrange
from settings import *


def get_random_position():
    return [randrange(*random_range), randrange(*random_range)]


class GameCells:

    def __init__(self):
        self.top = info_height + tile_size // 2
        self.bottom = window_height - tile_size // 2
        self.left = 0 + tile_size // 2
        self.right = window_width - tile_size // 2
        self.game_area = {(x, y): 0 for x in
                          range(self.left, self.right, tile_size)
                          for y in
                          range(self.top, self.bottom, tile_size)}

    def fill_cells_condition(self, snake_segments, wall_segments,
                             food_segments):
        # Очищаем все клетки игрового поля перед обновлением
        for cell in self.game_area.keys():
            self.game_area[cell] = 0

        # Обновляем клетки для стен
        for segment in wall_segments:
            if segment != (0, 0):
                self.game_area[segment.center] = 3

        # Обновляем клетки для змейки
        for segment in snake_segments:
            if segment != (0, 0):
                self.game_area[segment.center] = 2

        # Обновляем клетки для еды
        for segment in food_segments:
            if segment != (0, 0) and segment is not None:
                self.game_area[segment.rect.center] = 1


class Snake:
    def __init__(self):
        self.cell_size = 48
        self.direction = (0, 0)
        self.length = 1
        self.head = pg.Rect(0, 0, self.cell_size, self.cell_size)
        self.segments = [self.head.copy()]

    def move(self):
        self.head.move_ip(self.direction)
        self.segments.append(self.head.copy())
        self.segments = self.segments[-self.length:]

    def get_start_position(self, wall_segments):
        x,y = get_random_position()
        next_pos = pg.Rect(x,y,49,49)
        wall_collapsing = pg.Rect.collidelist(next_pos, wall_segments) == -1
        if wall_collapsing:
               self.head.center = get_random_position()

    def get_new_direction(self, event_key):
        direction_changes = {
            pg.K_w: (0, -tile_size) if self.direction[
                                           1] == 0 else self.direction,
            pg.K_s: (0, tile_size) if self.direction[
                                          1] == 0 else self.direction,
            pg.K_a: (-tile_size, 0) if self.direction[
                                           0] == 0 else self.direction,
            pg.K_d: (tile_size, 0) if self.direction[
                                          0] == 0 else self.direction
        }
        if event_key not in direction_changes.keys():
            return self.direction
        return direction_changes.get(event_key)

    def is_dead(self, wall_segments):
        self_eating = pg.Rect.collidelist(self.head,
                                          self.segments[:-1]) != -1
        wall_collapsing = pg.Rect.collidelist(self.head, wall_segments) != -1
        if (self.head.left < 0 or self.head.right > window_width
                or self.head.top < info_height or self.head.bottom > window_height
                or self_eating or wall_collapsing):
            return True
        return False


class Wall:
    square_segments = []

    def __init__(self):
        self.cell_size = 50
        self.segments = []

    def create_wall_cell(self, game_area, snake_head):
        empty_cells = [cell[0] for cell in game_area.items() if cell[1] == 0]
        head_pos = snake_head.center
        available_pos = [cell for cell in empty_cells
                         if abs(head_pos[0] - cell[0]) > 50 and
                         abs(head_pos[1] - cell[1]) > 50]
        new_pos = available_pos[random.randint(0, len(available_pos) - 1)]
        new_wall = pg.Rect(0, 0,
                           self.cell_size, self.cell_size)
        new_wall.center = new_pos
        self.segments.append(new_wall)

    def create_static_obstacle(self):
        squares = [self.make_square((100, 250)),
                   self.make_square((600, 250)),
                   self.make_square((100, 600)),
                   self.make_square((600, 600))]
        for square in squares:
            for cell in square:
                self.square_segments.append(cell)

    def make_square(self, left_top_corner):
        x0, y0 = left_top_corner[0], left_top_corner[1]
        return [pg.Rect(x, y, self.cell_size, self.cell_size) for x in
                [x0, x0 + self.cell_size] for y in [y0, y0 + self.cell_size]]


class Food:
    def __init__(self):
        self.cell_size = 48
        self.rect = pg.Rect(0, 0, self.cell_size, self.cell_size)
        self.rect.center = get_random_position()

    def take_next_position(self, game_area):
        empty_cells = [cell[0] for cell in game_area.items() if cell[1] == 0]
        new_pos = empty_cells[random.randint(0, len(empty_cells) - 1)]
        self.rect.center = new_pos


class SpecialFood(Food):
    def __init__(self):
        super().__init__()
        self.rect.center = (-100, -100)
        self.appear_time = pg.time.get_ticks()
        self.score_last_spawn = 0
        self.appear_cooldown = -10_001

    def death_check(self):
        current_time = pg.time.get_ticks()
        return current_time - self.appear_time > 3000 and self.rect.center != (
            -100, -100)

    def hide(self):
        self.rect.center = (-100, -100)

    def take_next_position(self, game_area):
        empty_cells = [cell[0] for cell in game_area.items() if cell[1] == 0]
        new_pos = empty_cells[random.randint(0, len(empty_cells) - 1)]
        current_time = pg.time.get_ticks()
        if current_time - self.appear_cooldown > 10_000:
            self.rect.center = new_pos
            self.appear_time = pg.time.get_ticks()

    def was_eaten(self):
        self.rect.center = (-100, -100)
        self.appear_cooldown = pg.time.get_ticks()
