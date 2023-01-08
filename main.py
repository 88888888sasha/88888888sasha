import random

import pygame

import Common
import VRAG
import player1
import MACH
import sqlite3
Player = player1.player1Object()
vrags = VRAG.vrag1Object()
BAL = MACH.Ball()
all_sprites = pygame.sprite.Group()
all_sprites.add(BAL)
pygame.init()
win = Common.win
FPS = 60
clock = pygame.time.Clock()
def kas():
    if Player.y < BAL.rect.top + 60  < Player.y + 10  and Player.x - 60 < BAL.rect.left < Player.x + 140:
        if BAL.rand == 4:
            BAL.rand = 3
        elif BAL.rand == 6:
             BAL.rand = 1
        elif BAL.rand == 5:
            BAL.rand = 2
        elif BAL.rand == 1:
            BAL.rand = 6
        elif BAL.rand == 3:
            BAL.rand = 4
    if vrags.y - 10 < BAL.rect.top  < vrags.y + 10  and vrags.x - 60 < BAL.rect.left < vrags.x + 140:
        if BAL.rand == 1:
            BAL.rand = 6
        elif BAL.rand == 3:
             BAL.rand = 4
        elif BAL.rand == 2:
            BAL.rand = 5
        elif BAL.rand == 6:
            BAL.rand = 1
        elif BAL.rand == 4:
            BAL.rand = 3
a = 0
b = 0
l = 1
u = 0
def draw_pole():
    pygame.draw.line(win, (250, 250, 250), (0, 0), (5, 1000), 20)
    pygame.draw.line(win, (250, 250, 250), (600, 0), (600, 1000), 20)
    pygame.draw.line(win, (250, 250, 250), (0, 0), (600, 0), 20)
    pygame.draw.line(win, (250, 250, 250), (0, 1000), (600, 1000), 20)
    pygame.draw.lines(win, ((250, 250, 250)), True, ((150, 950), (150, 1000), (450, 1000), (450, 950)), 10)
    pygame.draw.lines(win, ((250, 250, 250)), True, ((150, 50), (150, 0), (450, 0), (450, 50)), 10)
    pygame.draw.circle(win, ((250, 250, 250)), (300, 500), 40)
def run():
    if BAL.rect.top > vrags.y:
        if vrags.x > BAL.rect.left:
            vrags.x -= 6
        if vrags.x < BAL.rect.left:
            vrags.x += 6
    else:
        if vrags.x > 250:
            vrags.x -= 6
        if vrags.x < 250:
            vrags.x += 6
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    win.fill((0, 225, 0))


    if l == 1:
        u += 1
        draw_pole()
        all_sprites.update()
        vrags.draw()
        run()
        Player.run()
        Player.draw()
        all_sprites.draw(win)
        kas()
        if BAL.rect.left > 130 and BAL.rect.left < 470 and BAL.rect.top >= 950 and BAL.rect.top <= 955:
            a = a + 1
            BAL.rect.left = 270
            BAL.rect.top = 470
            BAL.rand = random.randint(1, 6)
        if BAL.rect.left > 130 and BAL.rect.left < 470 and BAL.rect.top >= 10 and BAL.rect.top <= 15:
            b = b + 1
            BAL.rect.left = 270
            BAL.rect.top = 470
            BAL.rand = random.randint(1, 6)
        time = u // 60
        con = sqlite3.connect("play.sqlite")
        cur = con.cursor
        que_create = '''
        CREATE TABLE IF NOT EXISTS class (
            id INTEGER PRIMARY KEY,
            you INTEGER
            vrag INTEGER
            time INTEGER
        )
        '''
        cur.execute(que_create)
        con.commit()
        que_insert = '''
        INSERT INTO class (you, vrag, time) VALUES
            (a, b, time)
        '''
    f1 = pygame.font.Font(None, 100)
    d = str(str(a) + "     " + str(b))
    text1 = f1.render(d, 1, (100, 0, 0))
    win.blit(text1, (215, 466))
    w = 0
    if a >= 4 or b >= 4:
        if b >= 4:
            o = "You WIN!!!"
        if a >= 4:
            o = "You LOOSE!!!"
        c = "Заново"
        z = ("YOU = " + str(b))
        v = ("VRAG = " + str(a))
        pygame.draw.rect(win, (250, 250, 250), (0, 0, 600, 1000))
        pygame.draw.rect(win, (0, 250, 250), (0, 0, 600, 1000), 20)
        pygame.draw.rect(win, (0, 250, 0), (200, 700, 200, 126))
        n = ("time = " + str(time) + " second")
        f1 = pygame.font.Font(None, 100)
        f2 = pygame.font.Font(None, 60)
        text1 = f1.render(o, 1, (0, 0, 0))
        text2 = f2.render(c, 1, (0, 0, 0))
        text3 = f2.render(z, 1, (0, 0, 0))
        text4 = f2.render(v, 1, (0, 0, 0))
        text5 = f2.render(n, 1, (0, 0, 0))
        win.blit(text1, (100, 200))
        win.blit(text2, (220, 750))
        win.blit(text3, (160, 300))
        win.blit(text4, (160, 400))
        win.blit(text5, (160, 500))
        print()
        l = 0
        p = pygame.mouse.get_pos()
        for i in pygame.event.get():
            if i.type == pygame.MOUSEBUTTONDOWN and (700 < p[1] < 826 and 200 < p[0] < 400):
                l = 1
                a = 0
                b = 0
                BAL.rect.left = 270
                BAL.rect.top = 470
                Player.x = 250
                Player.y = 900
                vrags.x = 250
                vrags.y = 100
                u = 0


    pygame.display.update()
    clock.tick(FPS)

