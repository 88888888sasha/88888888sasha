import pygame
import Common

win = Common.win


class player1Object():
    def __init__(self):
        self.x = 250
        self.y = 900
    def draw(self,):
        pygame.draw.polygon( win, (150, 50, 250),((self.x, self.y), (self.x, self.y + 10), (self.x + 100, self.y + 10), (self.x + 100, self.y)))
    def run(self,):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.x += 3
        if keys[pygame.K_LEFT]:
            self.x -= 3
        if keys[pygame.K_UP]:
            self.y -= 3
        if keys[pygame.K_DOWN]:
            self.y += 3