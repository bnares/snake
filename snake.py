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



class Main:
    def __init__(self):
        self.snake = Snake()
        self.fruit = Fruit()

    def draw_elements(self):
        self.snake.draw_snake()
        self.fruit.draw_fruit()

    def update_snake(self):
        self.snake.move_snake()
        self.check_collision()


    def check_collision(self):
        if self.fruit.pos == self.snake.body[0]:
            print("fruit")




cell_size = 30
cell_number = 20

clock = pygame.time.Clock()
win = pygame.display.set_mode((cell_size*cell_number,cell_size*cell_number))




main_game = Main()


SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE,150)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == SCREEN_UPDATE:

            main_game.update_snake()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                main_game.snake.direction = Vector2(0,-1)


            if event.key == pygame.K_DOWN:
                main_game.snake.direction = Vector2(0,1)

            if event.key == pygame.K_LEFT:
                main_game.snake.direction = Vector2(-1,0)

            if event.key == pygame.K_RIGHT:
                main_game.snake.direction = Vector2(1,0)



    win.fill((175, 215, 70))
    main_game.draw_elements()
    pygame.display.flip()
    clock.tick(60)