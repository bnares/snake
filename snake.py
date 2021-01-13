import pygame
import sys, random
from pygame.math import Vector2



pygame.init()


class Snake:
    def __init__(self):
        self.body = [Vector2(5,10), Vector2(4,10), Vector2(3,10)]
        self.direction = Vector2(1,0)
        self.new_block = False

    def draw_snake(self):
        for block in self.body:
            snake = pygame.Rect(block.x*cell_size, block.y*cell_size, cell_size, cell_size)
            pygame.draw.rect(win, (183,111,122), snake)

    def move_snake(self):
        if self.new_block == False:
            body_copy = self.body[ : -1]
            body_copy.insert(0,body_copy[0]+self.direction)
            self.body = body_copy[:]

        else:
            body_copy = self.body[: ]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]
            self.new_block = False

    def add_block(self):
        self.new_block = True








class Fruit:
    def __init__(self):
        self.randomize()

    def draw_fruit(self):
        fruit = pygame.Rect(int(self.pos.x*cell_size), int(self.pos.y*cell_size), cell_size,cell_size)
        #pygame.draw.rect(win, (126,166,114), fruit)
        win.blit(apple,fruit)


    def randomize(self):
        self.x = random.randint(0, cell_number - 1)
        self.y = random.randint(0, cell_number - 1)
        self.pos = Vector2(self.x, self.y)




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

            #nowa pozycja fruit

            self.fruit.randomize()

            #add another block to the end of snake

            self.snake.add_block()

    def check_fail(self):
        #check if snake is autside of the screen
        if self.snake.body[0].x > cell_number or self.snake.body[0].x<0:
            self.game_over()

        elif self.snake.body[0].y> cell_number or self.snake.body[0].y<0:
            self.game_over()

        #check if snake does not colide with itself
        for block in self.snake.body[1:]:
            if self.snake.body[0]== block:
                self.game_over()

    def game_over(self):
        pygame.quit()
        sys.exit()

cell_size = 30
cell_number = 20

clock = pygame.time.Clock()
win = pygame.display.set_mode((cell_size*cell_number,cell_size*cell_number))

apple = pygame.image.load(r"D:\calculation\snake\Snake-main\Snake-main\Graphics\apple.png").convert_alpha()


main_game = Main()


SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE,150)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == SCREEN_UPDATE:
            main_game.check_collision()
            main_game.update_snake()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if main_game.snake.direction.y != 1:
                    main_game.snake.direction = Vector2(0,-1)


            if event.key == pygame.K_DOWN:
                if main_game.snake.direction.y != -1:
                    main_game.snake.direction = Vector2(0,1)

            if event.key == pygame.K_LEFT:
                if main_game.snake.direction.x != 1:
                    main_game.snake.direction = Vector2(-1,0)

            if event.key == pygame.K_RIGHT:
                if main_game.snake.direction.x != -1:
                    main_game.snake.direction = Vector2(1,0)



    win.fill((175, 215, 70))
    main_game.draw_elements()
    main_game.check_fail()
    pygame.display.flip()
    clock.tick(60)