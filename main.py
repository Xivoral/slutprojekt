import pygame
import random

#initaliserar pygame
pygame.init()
#skärmdimensioner
skärm_bredd = 800
skärm_höjd = 600
#speletsskärm
screen = pygame.display.set_mode((skärm_bredd, skärm_höjd))
pygame.display.set_caption("Fånga Äpplet")
#färger
GREEN = (0, 255, 0)
BROWN = (150, 75, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
#klockan
clock = pygame.time.Clock()
#spelsats
game = True
#några spelvariabler
korg_bredd = 100
korg_höjd = 50
korg_x = skärm_bredd // 2 - korg_bredd // 2
korg_y = skärm_höjd - korg_höjd - 20
korg_hastighet = 10

äpple_bredd = 50
äpple_höjd = 35
äpple_hastighet = 5

poäng = 0

def måla_korg(x,y):
    pygame.draw.rect(screen, BROWN, [x,y,korg_bredd,korg_höjd])

def måla_äpplen(x,y):
    pygame.draw.ellipse(screen, RED, [x,y,äpple_bredd,äpple_höjd])
    
def visa_poäng(poäng):
    font = pygame.font.SysFont(None, 36)
    text = font.render("Poäng: " + str(poäng), True, WHITE)
    screen.blit(text, (10,10))

def spel_slut():
    font = pygame.font.SysFont(None, 72)
    text = font.render("Spel slut", True, WHITE)
    screen.blit(text, (skärm_bredd // 2 - 150, skärm_höjd // 2 - 36))
    pygame.display.update()
    pygame.time.delay(2000)
    pygame.quit()
    quit()

def spel_loop():
    global poäng
    global korg_x

    äpple_x = random.randint(0, skärm_bredd - äpple_bredd)
    äpple_y = -äpple_höjd

    kör = True
    while kör:
        screen.fill(GREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                kör = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            korg_x -= korg_hastighet
        if keys[pygame.K_RIGHT]:
            korg_x += korg_hastighet
        
        if korg_x < 0:
            korg_x = 0
        elif korg_x > skärm_bredd - korg_bredd:
            korg_x = skärm_bredd - korg_bredd
        
        äpple_y += äpple_hastighet

        if äpple_y + äpple_höjd > korg_y and korg_x < äpple_x + äpple_bredd < korg_x + korg_bredd:
            poäng += 1
            äpple_x = random.randint(0, skärm_bredd - äpple_bredd)
            äpple_y = -äpple_höjd
        
        måla_korg(korg_x, korg_y)
        måla_äpplen(äpple_x, äpple_y)
        visa_poäng(poäng)

        if äpple_y > skärm_höjd:
            spel_slut()
    
        pygame.display.update()
        clock.tick(60)
    





while game:
    spel_loop()
    
