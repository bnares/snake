import pygame
import sys, random
from pygame.math import Vector2



pygame.init()


class Snake:
    def __init__(self):
        self.body = [Vector2(5,10), Vector2(4,10), Vector2(3,10)]
        self.direction = Vector2(1,0)
        self.new_block = False

        self.head_up = pygame.image.load(r"D:\calculation\snake\Snake-main\Snake-main\Graphics\head_up.png").convert_alpha()
        self.head_down = pygame.image.load(r"D:\calculation\snake\Snake-main\Snake-main\Graphics\head_down.png").convert_alpha()
        self.head_right = pygame.image.load(r"D:\calculation\snake\Snake-main\Snake-main\Graphics\head_right.png").convert_alpha()
        self.head_left = pygame.image.load(r"D:\calculation\snake\Snake-main\Snake-main\Graphics\head_left.png").convert_alpha()

        self.tail_up = pygame.image.load(r"D:\calculation\snake\Snake-main\Snake-main\Graphics\tail_up.png").convert_alpha()
        self.tail_down = pygame.image.load(r"D:\calculation\snake\Snake-main\Snake-main\Graphics\tail_down.png").convert_alpha()
        self.tail_right = pygame.image.load(r"D:\calculation\snake\Snake-main\Snake-main\Graphics\tail_right.png").convert_alpha()
        self.tail_left = pygame.image.load(r"D:\calculation\snake\Snake-main\Snake-main\Graphics\tail_left.png").convert_alpha()

        self.body_vertical = pygame.image.load(r"D:\calculation\snake\Snake-main\Snake-main\Graphics\body_vertical.png").convert_alpha()
        self.body_horizontal = pygame.image.load(r"D:\calculation\snake\Snake-main\Snake-main\Graphics\body_horizontal.png").convert_alpha()

        self.body_tr = pygame.image.load(r"D:\calculation\snake\Snake-main\Snake-main\Graphics\body_tr.png").convert_alpha()
        self.body_tl = pygame.image.load(r"D:\calculation\snake\Snake-main\Snake-main\Graphics\body_tl.png").convert_alpha()
        self.body_br = pygame.image.load(r"D:\calculation\snake\Snake-main\Snake-main\Graphics\body_br.png").convert_alpha()
        self.body_bl = pygame.image.load(r"D:\calculation\snake\Snake-main\Snake-main\Graphics\body_bl.png").convert_alpha()
        self.crunch_sound = pygame.mixer.Sound(r"D:\calculation\snake\Snake-main\Snake-main\Sound\crunch.wav")
        self.head = self.head_right
        self.tail = self.tail_left
        self.snake_body = self.body_vertical

    def draw_snake(self):

        self.update_head_graphics()
        self.update_tail_graphics()
        for index, block in enumerate(self.body):
            snake = pygame.Rect(block.x*cell_size, block.y*cell_size, cell_size, cell_size)
            if index ==0:
                win.blit(self.head, snake)

            elif index == len(self.body) - 1:
                win.blit(self.tail,snake)

            else:
                previous_block = self.body[index+1] - block
                next_block = self.body[index-1]-block
                if previous_block.y == next_block.y:
                    self.snake_body = self.body_vertical
                    win.blit(self.snake_body, snake)
                elif previous_block.x == next_block.x:
                    self.snake_body = self.body_horizontal
                    win.blit(self.snake_body, snake)
                else:
                    if ((previous_block.x == -1 and next_block.y ==-1) or (previous_block.y ==-1 and next_block.x ==-1)):
                        win.blit(self.body_tl, snake)

                    if ((previous_block.x == -1 and next_block.y ==-1) or (previous_block.y ==-1 and next_block.x ==-1)):
                        win.blit(self.body_tl, snake)

                    if ((previous_block.x == -1 and next_block.y ==-1) or (previous_block.y ==-1 and next_block.x ==-1)):
                        win.blit(self.body_tl, snake)

                    if ((previous_block.x == -1 and next_block.y ==-1) or (previous_block.y ==-1 and next_block.x ==-1)):
                        win.blit(self.body_tl, snake)





            #else:
               # pygame.draw.rect(win, (183,111,122), snake)
            #pygame.draw.rect(win, (183,111,122), snake)



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


    def update_head_graphics(self):
        head_relation = self.body[1] - self.body[0]

        if head_relation == Vector2(1,0):
            self.head = self.head_left
        elif head_relation == Vector2(-1,0):
            self.head = self.head_right
        elif head_relation == Vector2(0,1):
            self.head = self.head_up
        elif head_relation == Vector2(0,-1):
            self.head = self.head_down

    def update_tail_graphics(self):
        tail_relation = self.body[-2] - self.body[-1]
        if tail_relation == Vector2(1,0):
            self.tail = self.tail_left
        elif tail_relation == Vector2(-1,0):
            self.tail = self.tail_right
        elif tail_relation == Vector2(0,1):
            self.tail = self.tail_up
        elif tail_relation == Vector2(0,-1):
            self.tail = self.tail_down








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
        if self.snake.body[0].x > cell_number-1 or self.snake.body[0].x<0:
            self.game_over()

        elif self.snake.body[0].y> cell_number-1 or self.snake.body[0].y<0:
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