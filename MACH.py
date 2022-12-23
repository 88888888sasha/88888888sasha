import random

import pygame
import Common

win = Common.win

class Ball(pygame.sprite.Sprite):
    # Создаем инициализатор(конструктор)
    def __init__(self):
        # Вызываем конструктор самого класса Sprite
        super().__init__()
        # Загружаем изображение
        self.image = pygame.image.load('WhiteBall.png')
        # Настраиваем его. Не нужно здесь ничего менять, просто копируйте
        # Здесь я поставил convert_alpha, чтобы правильно работала прозрачность
        #self.image = self.image.convert()
        self.image = self.image.convert_alpha()
        colorkey = self.image.get_at((0, 0))
        self.image.set_colorkey(colorkey)
        # Задаем размер. Первая 100 - ширина, вторая 100 - высота
        self.image = pygame.transform.scale(self.image, (60, 60))
        # Задаем границы
        self.rect = self.image.get_rect()
        self.rect.left = 270
        self.rect.top = 470
        self.s = random.randrange(1, 7)
        self.rand = 0

    def update(self):
        self.rand = self.s
        if self.rand == 1:
            self.rect.left -= 1
            self.rect.top -= 1
        elif self.rand == 2:
            self.rect.left -= 1
        elif self.rand == 3:
            self.rect.left -= 1
            self.rect.top += 1
        elif self.rand == 4:
            self.rect.left += 1
            self.rect.top += 1
        elif self.rand == 5:
            self.rect.left += 1
        elif self.rand == 6:
            self.rect.left += 1
            self.rect.top -= 1

