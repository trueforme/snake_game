from game_objects import Snake, Food, Wall, GameCells, SpecialFood

from level_renderers import *

pg.init()
clock = pg.time.Clock()


class SnakeGame:
    def __init__(self, snake, food, delta_time, live_count, wall, game_cells, gold,
                 goal, game_screen):
        self.snake = snake
        self.food = food
        self.time_step = delta_time
        self.lives = live_count

        self.wall = wall
        self.game_cells = game_cells
        self.gold = gold
        self.screen = game_screen
        self.goal = goal
        self.time_now = 0
        self.time = 0

    def reset_level(self):
        screen.fill('black')
        self.time, self.time_step = 0, 120
        if self.lives <= 0:
            exit()
        self.snake = Snake()
        self.gold = SpecialFood()
        self.game_cells = GameCells()
        self.wall = Wall()
        self.snake.get_start_position()
        self.food.take_next_position(self.game_cells.game_area)

    def draw_info_panel(self, goal):
        font = pg.font.SysFont('game', 36)
        score_text = font.render(f"Score: {self.snake.length - 1}", True,
                                 (255, 255, 255))
        lifes_text = font.render(f"Lifes: {self.lives}", True, (255, 255, 255))
        goal_text = font.render(f"Goal: {goal}", True,
                                (255, 255, 255))
        screen.blit(score_text, (10, 10))
        screen.blit(lifes_text, (10, 50))
        screen.blit(goal_text, (600, 10))

    def check_death(self):
        if self.snake.is_dead(self.wall.segments + self.wall.square_segments):
            self.lives -= 1
            self.reset_level()

    def check_eating(self):
        if self.snake.head.center == self.food.rect.center:
            self.snake.length += 1
            self.game_cells.fill_cells_condition(self.snake.segments,
                                                 self.wall.segments + self.wall.square_segments,
                                                 [self.food, self.gold])
            self.food.take_next_position(self.game_cells.game_area)
            self.game_cells.fill_cells_condition(self.snake.segments,
                                                 self.wall.segments + self.wall.square_segments,
                                                 [self.food, self.gold])
            self.time_step = max(10, self.time_step - 2)
        if self.snake.head.center == self.gold.rect.center:
            self.gold.hide()
            self.gold.score_last_spawn = self.snake.length - 1
            self.snake.length += 3
            self.gold.was_eaten()
            self.game_cells.fill_cells_condition(self.snake.segments,
                                                 self.wall.segments + self.wall.square_segments,
                                                 [self.food, self.gold])
        if self.snake.length > 5 and self.gold.rect.center == (
                -100,
                -100) and self.gold.score_last_spawn + 6 < self.snake.length:
            self.gold.take_next_position(self.game_cells.game_area)
        if self.gold.death_check():
            self.gold.hide()

    def tick_game_timings(self):
        self.time_now = pg.time.get_ticks()
        if self.time_now - self.time > self.time_step:
            self.time = self.time_now
            self.snake.move()

        pg.display.flip()
        clock.tick(60)

    def draw_basics(self):
        screen.fill('black')

        pg.draw.rect(screen, 'blue', pg.Rect(0, 0, window_width, 150))
        pg.draw.rect(screen, 'red', self.food.rect)
        [pg.draw.rect(screen, 'green', segment) for segment in
         self.snake.segments]
        [pg.draw.rect(screen, 'blue', segment) for segment in
         self.wall.segments]
        [pg.draw.rect(screen, 'blue', segment) for segment in
         self.wall.square_segments]
        pg.draw.rect(screen, 'yellow', self.gold.rect)

    def run_basic_level(self):
        show_start_screen()
        self.goal = 10
        self.snake.get_start_position()
        self.food.take_next_position(self.game_cells.game_area)
        running = True
        while running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    exit()
                if event.type == pg.KEYDOWN:
                    self.snake.direction = self.snake.get_new_direction(
                        event.key)

            self.draw_basics()
            self.draw_info_panel(self.goal)

            if self.snake.length - 1 >= self.goal:
                running = False
                self.reset_level()
                show_between_screen()

            self.check_death()
            self.check_eating()
            self.game_cells.fill_cells_condition(self.snake.segments,
                                                 self.wall.segments + self.wall.square_segments,
                                                 [self.food, self.gold])
            self.tick_game_timings()

    def run_level_with_static_obstacles(self):
        self.goal = 15
        self.snake.get_start_position()
        self.create_static_obstacles()
        self.food.take_next_position(self.game_cells.game_area)
        running = True
        while running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    exit()
                if event.type == pg.KEYDOWN:
                    self.snake.direction = self.snake.get_new_direction(
                        event.key)

            self.draw_basics()
            self.draw_info_panel(self.goal)

            if self.snake.length - 1 >= self.goal:
                running = False
                self.reset_level()
                show_between_screen()

            self.check_death()
            self.check_eating()
            self.tick_game_timings()

    def run_final_level(self):
        self.goal = 20
        self.lives += 3
        self.snake.get_start_position()
        self.food.take_next_position(self.game_cells.game_area)
        running = True
        while running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    exit()
                if event.type == pg.KEYDOWN:
                    self.snake.direction = self.snake.get_new_direction(
                        event.key)

            self.draw_basics()
            self.draw_info_panel(self.goal)

            if self.snake.length - 1 >= self.goal:
                running = False
                self.reset_level()
                show_end_screen()

            self.check_death()
            self.check_obstacles_condition()
            self.check_eating()
            self.game_cells.fill_cells_condition(self.snake.segments,
                                                 self.wall.segments + self.wall.square_segments,
                                                 [self.food, self.gold])
            self.tick_game_timings()

    def check_obstacles_condition(self):
        self.wall.square_segments = []
        if self.snake.head.center == self.food.rect.center:
            self.game_cells.fill_cells_condition(self.snake.segments,
                                                 self.wall.segments + self.wall.square_segments,
                                                 [self.food, self.gold])
            self.wall.create_wall_cell(self.game_cells.game_area,
                                       self.snake.head)

    def create_static_obstacles(self):
        self.wall.create_static_obstacle()


game = SnakeGame(Snake(), Food(), time_step, lives, Wall(), GameCells(),
                 SpecialFood(),
                 goal=5, game_screen=screen)


def main():
    game.run_basic_level()
    game.run_level_with_static_obstacles()
    game.run_final_level()


main()
