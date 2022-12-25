import random

import pygame

import Common
import VRAG
import player1
import MACH
Player = player1.player1Object()
vrags = VRAG.vrag1Object()
BAL = MACH.Ball()
all_sprites = pygame.sprite.Group()
all_sprites.add(BAL)
pygame.init()
win = Common.win
FPS = 60
clock = pygame.time.Clock()
a = 0
b = 0

#def ST():
    #print("BAL: ", BAL.rect.top)
    #print("Player: ", Player.y)
    #if (Player.x - 30 < BAL.rect.left < Player.x + 130 or Player.x - 30 < BAL.rect.left + 60 < Player.x + 130) and Player.y + 30  == BAL.rect.top:
    #    if BAL.rand == 4:
    #        BAL.rand = 3
    #    elif BAL.rand == 6:
    #        BAL.rand = 1

def draw_pole():
    pygame.draw.line(win, (250, 250, 250), (0, 0), (5, 1000), 20)
    pygame.draw.line(win, (250, 250, 250), (600, 0), (600, 1000), 20)
    pygame.draw.line(win, (250, 250, 250), (0, 0), (600, 0), 20)
    pygame.draw.line(win, (250, 250, 250), (0, 1000), (600, 1000), 20)
    pygame.draw.lines(win, ((250, 250, 250)), True, ((150, 950), (150, 1000), (450, 1000), (450, 950)), 10)
    pygame.draw.lines(win, ((250, 250, 250)), True, ((150, 50), (150, 0), (450, 0), (450, 50)), 10)
    pygame.draw.circle(win, ((250, 250, 250)), (300, 500), 40)

    if BAL.rect.left < 150 and BAL.rect.left < 450 and BAL.rect.top > 900:
        a + 1
    if BAL.rect.left < 150 and BAL.rect.left < 450 and BAL.rect.top < 20:
        b + 1


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    win.fill((0, 225, 0))


    draw_pole()
    vrags.draw()
    vrags.run()
    Player.draw()
    Player.run()
    all_sprites.draw(win)
    all_sprites.update()
    if BAL.rect.left > 130 and BAL.rect.left < 470 and BAL.rect.top >= 950 and BAL.rect.top <= 951:
        a = a + 1
        BAL.rect.left = 270
        BAL.rect.top = 470
        BAL.rand = random.randint(1, 7)
    if BAL.rect.left > 130 and BAL.rect.left < 470 and BAL.rect.top >= 10 and BAL.rect.top <= 11:
        b = b + 1
        BAL.rect.left = 270
        BAL.rect.top = 470
        BAL.rand = random.randint(1, 6)
    print(a, b)

    pygame.display.update()
    clock.tick(FPS)

