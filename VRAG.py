import pygame
import Common

win = Common.win


class vrag1Object():
    def __init__(self):
        self.x = 100
        self.y = 100
        self.toRight = True
        self.toLeft = False

    def draw(self):
        if self.x == 400:
            self.toLeft = True
            self.toRight = False
        if self.x == 100:
            self.toRight = True
            self.toLeft = False
        if self.toRight:
            self.x += 3
        if self.toLeft:
            self.x -= 3

        pygame.draw.polygon( win, (150, 50, 250),((self.x, self.y), (self.x, self.y + 10), (self.x + 100, self.y + 10), (self.x + 100, self.y)))
    def run(self):
       for i in range(400):
            self.x += 1
       for i in range(400):
            self.x -= 1