from game_objects import Snake, Food, Wall, GameCells, SpecialFood
from level_renderers import *

class BaseLevel:
    def __init__(self, snake, food, live_count, wall, game_cells, gold, goal, game_screen):
        self.snake = snake
        self.food = food
        self.lives = live_count
        self.wall = wall
        self.game_cells = game_cells
        self.gold = gold
        self.screen = game_screen
        self.goal = goal
        self.time_step = 120
        self.time_now = 0
        self.time = 0
        self.number = 1

    def reset_level(self):
        self.screen.fill('black')
        self.time, self.time_step = 0, 120
        if self.lives <= 0:
            # отправка в мейн
            exit()
        self.snake = Snake()
        self.food = Food()
        self.gold = SpecialFood()
        self.game_cells = GameCells()
        self.wall = Wall()
        self.snake.get_start_position(self.wall.segments)
        self.food.take_next_position(self.game_cells.game_area)

    def draw_info_panel(self):
        font = pg.font.SysFont('game', 36)
        score_text = font.render(f"Score: {self.snake.length - 1}", True, (255, 255, 255))
        lifes_text = font.render(f"Lives: {self.lives}", True, (255, 255, 255))
        goal_text = font.render(f"Goal: {self.goal}", True, (255, 255, 255))
        self.screen.blit(score_text, (10, 10))
        self.screen.blit(lifes_text, (10, 50))
        self.screen.blit(goal_text, (600, 10))

    def check_death(self):
        if self.snake.is_dead(self.wall.segments + self.wall.square_segments):
            self.lives -= 1
            self.reset_level()

    def check_eating(self):
        if self.snake.head.center == self.food.rect.center:
            self.snake.length += 1
            self.update_game_cells()
            self.food.take_next_position(self.game_cells.game_area)
            self.update_game_cells()
            self.time_step = max(90, self.time_step - 2)
        if self.snake.head.center == self.gold.rect.center:
            self.gold.hide()
            self.gold.score_last_spawn = self.snake.length - 1
            self.snake.length += 3
            self.gold.was_eaten()
            self.update_game_cells()
        if self.snake.length > 5 and self.gold.rect.center == (-100, -100) and self.gold.score_last_spawn + 6 < self.snake.length:
            self.gold.take_next_position(self.game_cells.game_area)
        if self.gold.death_check():
            self.gold.hide()

    def update_game_cells(self):
        self.game_cells.fill_cells_condition(
            self.snake.segments,
            self.wall.segments + self.wall.square_segments,
            [self.food, self.gold]
        )

    def tick_game_timings(self):
        self.time_now = pg.time.get_ticks()
        if self.time_now - self.time > self.time_step:
            self.time = self.time_now
            self.snake.move()

        pg.display.flip()
        clock.tick(60)

    def draw_basics(self):
        self.screen.fill('black')
        pg.draw.rect(self.screen, 'blue', pg.Rect(0, 0, window_width, 150))
        pg.draw.rect(self.screen, 'red', self.food.rect)
        [pg.draw.rect(self.screen, 'green', segment) for segment in self.snake.segments]
        [pg.draw.rect(self.screen, 'blue', segment) for segment in self.wall.segments]
        [pg.draw.rect(self.screen, 'blue', segment) for segment in self.wall.square_segments]
        pg.draw.rect(self.screen, 'yellow', self.gold.rect)

class CommonLevel(BaseLevel):
    pass  # No changes needed for Level1, behavior is handled in `run`

class LevelStaticObstacles(BaseLevel):
    def create_static_obstacles(self):
        self.wall.create_static_obstacle()

    def reset_level(self):
        super().reset_level()
        self.create_static_obstacles()

class LevelDynamicObstacles(BaseLevel):
    def check_obstacles_condition(self):
        if self.snake.head.colliderect(self.food.rect) and self.snake.length % 2 == 0:
            self.wall.create_wall_cell(self.game_cells.game_area, self.snake.head)
            self.update_game_cells()


    def check_eating(self):
        self.check_obstacles_condition()
        super().check_eating()

    def reset_level(self):
        super().reset_level()
        self.wall.square_segments.clear()