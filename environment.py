import pygame
from Snake import Snake, random_food
import config


class SnakeEnvironment:
    def __init__(self, render=False):
        self.render_graphics = render
        if self.render_graphics:
            pygame.init()
            self.screen = pygame.display.set_mode((config.WINDOW_SIZE, config.WINDOW_SIZE))
            pygame.display.set_caption("Snake AI")
            self.clock = pygame.time.Clock()


        self.snake = None
        self.food = None
        self.done = False
        self.score = 0


    def reset(self):
        self.snake = Snake()
        self.food = random_food(self.snake.body)
        self.done = False
        self.score = 0
        return self.get_state()


    def step(self, action):
        if self.done:
            return self.get_state(), 0, True


        self.snake.set_dir(action)
        self.snake.move()
        reward = config.WEIGHTS[0]


        current_length = len(self.snake.body)


        base, exp = config.WEIGHTS[3]
        reward += base ** (exp * (len(self.snake.body) - 1))


        if self.snake.check_collision():
            reward = config.WEIGHTS[2]
            self.done = True
        elif self.snake.body[0] == self.food:
            self.snake.grow = True
            self.score += 1
            reward += config.WEIGHTS[1]
            self.food = random_food(self.snake.body)


        return self.get_state(), reward, self.done


    def get_state(self):
        hx, hy = self.snake.body[0]
        fx, fy = self.food
        dx, dy = self.snake.direction
        return hx, hy, fx, fy, dx, dy


    def render(self):
        if not self.render_graphics:
            return


        self.screen.fill(config.BLACK)
        for x, y in self.snake.body:
            pygame.draw.rect(self.screen, config.GREEN, (x * config.CELL_SIZE, y * config.CELL_SIZE, config.CELL_SIZE, config.CELL_SIZE))


        fx, fy = self.food
        pygame.draw.rect(self.screen, config.RED, (fx * config.CELL_SIZE, fy * config.CELL_SIZE, config.CELL_SIZE, config.CELL_SIZE))


        pygame.display.flip()
        self.clock.tick(config.FPS)