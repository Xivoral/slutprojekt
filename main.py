import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
game = True

while game:
    pygame.display.flip()
    clock.tick(60)

