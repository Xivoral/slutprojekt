import pygame
#initaliserar pygame
pygame.init()
#speletsskärm
screen = pygame.display.set_mode((800, 600))
#färger
GREEN = (0, 255, 0)
BROWN = (150, 75, 0)
RED = (255, 0, 0)
#klockan
clock = pygame.time.Clock()
#spelsats
game = True
#spelloopen
while game:
    
    screen.fill(GREEN)
    pygame.display.update()
    clock.tick(60)
    for event in pygame.event.get():      
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    
