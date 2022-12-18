import pygame.draw


class player1():
    x = 250
    y = 900
    def draw(self, x, y):
        pygame.draw.polygon( win, (150, 150, 150),((self.x, self.y), (self.x, self.y + 20), (self.x + 100, self.y), (self.x + 100, self.y + 20)))
    def run(self, x, y):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.x += 2
        if keys[pygame.K_LEFT]:
            self.x -= 2
        if keys[pygame.K_UP]:
            self.y -= 2
        if keys[pygame.K_DOWN]:
            self.y += 2