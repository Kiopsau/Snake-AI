import pygame
import sys


import Snake
import config


pygame.init()
screen = pygame.display.set_mode((config.WINDOW_SIZE, config.WINDOW_SIZE))
clock = pygame.time.Clock()
pygame.display.set_caption("Snake Game")


def main():
    snake = Snake.Snake()
    food = Snake.random_food(snake.body)
    score = 0


    running = True
    while running:
        clock.tick(config.FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    snake.change_direction((0,-1))
                elif event.key == pygame.K_DOWN:
                    snake.change_direction((0,1))
                elif event.key == pygame.K_LEFT:
                    snake.change_direction((-1,0))
                elif event.key == pygame.K_RIGHT:
                    snake.change_direction((1,0))
       
        snake.move()


        if snake.check_collision():
            print(f"Game Over! Score: {score}")
            pygame.quit()
            sys.exit()


        if snake.body[0] == food:
            snake.grow = True
            score += 1
            food = Snake.random_food(snake.body)
       
        screen.fill(config.BLACK)
        for x, y in snake.body:
            pygame.draw.rect(screen, config.GREEN, (x * config.CELL_SIZE, y * config.CELL_SIZE, config.CELL_SIZE, config.CELL_SIZE))
       
        fx, fy = food
        pygame.draw.rect(screen, config.RED, (fx* config.CELL_SIZE, fy * config.CELL_SIZE, config.CELL_SIZE, config.CELL_SIZE))


        pygame.display.flip()


if __name__ == "__main__":
    main()