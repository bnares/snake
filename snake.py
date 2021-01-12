import pygame
import sys

pygame.init()


clock = pygame.time.Clock()
win = pygame.display.set_mode((400,500))
win.fill((175,215,70))
test_surface = pygame.Surface((100,200))
test_surface.fill((255,0,0))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    win.blit(test_surface, (50,100))
    pygame.display.update()
    clock.tick(60)