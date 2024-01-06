import pygame
from pygame.locals import *
from snake import *
from apple import *

class func:
    def teleport(snake, x, y):
        snake.snake.append((x-x%10, y-y%10))
        snake.snake.pop(0)
    def snake_eat_bad_apple(snake, bad_apple_pos):
        return snake.snake[-1]==bad_apple_pos
    def snake_smaller(snake):
        snake.snake.pop(0)
    
