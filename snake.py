import pygame
import sys, random
from pygame.math import Vector2



pygame.init()


class Snake:
    def __init__(self):
        self.body = [Vector2(5,10), Vector2(6,10), Vector2(7,10)]
        self.direction = Vector2(1,0)
    def draw_snake(self):
        for block in self.body:
            snake = pygame.Rect(block.x*cell_size, block.y*cell_size, cell_size, cell_size)
            pygame.draw.rect(win, (183,111,122), snake)

    def move_snake(self):
        body_copy = self.body[ : -1]

        body_copy.insert(0,body_copy[0]+self.direction)

        self.body = body_copy[:]




class Fruit:
    def __init__(self):
        self.x = random.randint(0, cell_number-1)
        self.y = random.randint(0,cell_number-1)
        self.pos = Vector2(self.x, self.y)


    def draw_fruit(self):
        fruit = pygame.Rect(int(self.pos.x*cell_size), int(self.pos.y*cell_size), cell_size,cell_size)
        pygame.draw.rect(win, (126,166,114), fruit)

cell_size = 30
cell_number = 20

clock = pygame.time.Clock()
win = pygame.display.set_mode((cell_size*cell_number,cell_size*cell_number))


fruit = Fruit()
snake = Snake()


SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE,150)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == SCREEN_UPDATE:
            snake.move_snake()

    win.fill((175, 215, 70))
    fruit.draw_fruit()
    snake.draw_snake()


    pygame.display.flip()
    clock.tick(60)