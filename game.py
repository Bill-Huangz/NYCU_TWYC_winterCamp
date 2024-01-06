import pygame
from pygame.locals import *
import random

from snake import *
from apple import *
from extends import *

GAME_ON = True
SPEED = 20

pygame.init()
screen = pygame.display.set_mode((600,600))
clock = pygame.time.Clock()
snake = Snake()
apple = Apple()
bad_apple=Bad_Apple()
apple.set_random_position(600)
bad_apple.set_random_position(600)


while GAME_ON:
    clock.tick(SPEED)
    snake.crawl()
    
    for event in pygame.event.get():
        if event.type == QUIT:
            GAME_ON = False
        if event.type == KEYDOWN:
            if event.key==K_UP and snake.direction != DOWN:
                print("UP")
                snake.direction = UP                
            elif event.key==K_LEFT and snake.direction != RIGHT:
                print("LEFT")
                snake.direction = LEFT                
            elif event.key==K_DOWN and snake.direction != UP:
                print("DOWN")
                snake.direction = DOWN                
            elif event.key==K_RIGHT and snake.direction != LEFT:
                print("RIGHT")
                snake.direction = RIGHT
        if event.type==MOUSEBUTTONDOWN:
            print("TELEPORT")
            func.teleport(snake, pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
                
    
    if snake.wall_collision(600) or snake.self_collision():
        GAME_ON  = False

    if snake.snake_eat_apple(apple.position):
        apple.set_random_position(600)
        snake.snake_bigger()
        SPEED += 0.5
    if func.snake_eat_bad_apple(snake, bad_apple.position):
        bad_apple.set_random_position(600)
        func.snake_smaller(snake)
        SPEED += 0.5
    
    screen.fill((0,0,0))
    for snake_pos in snake.snake[0:-1]:
        screen.blit(snake.skin, snake_pos)
    screen.blit(snake.head, snake.snake[-1])
    screen.blit(apple.apple, apple.position)
    screen.blit(bad_apple.apple, bad_apple.position)

    pygame.display.update()

pygame.quit()