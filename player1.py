import pygame
import Common

win = Common.win


class player1Object():
    x = 250
    y = 900
    def draw(self,):
        pygame.draw.polygon( win, (150, 50, 250),((self.x, self.y), (self.x, self.y + 10), (self.x + 100, self.y + 10), (self.x + 100, self.y)))
    def run(self,):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.x += 2
        if keys[pygame.K_LEFT]:
            self.x -= 2
        if keys[pygame.K_UP]:
            self.y -= 2
        if keys[pygame.K_DOWN]:
            self.y += 2