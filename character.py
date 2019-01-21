import os
import random
import pygame

size = width, height = 100, 600
screen = pygame.display.set_mode(size)


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error as message:
        print('Cannot load image:', name)
        raise SystemExit(message)
    image = image.convert_alpha()
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    return image


class Creature(pygame.sprite.Sprite):
    image = load_image("character.png")

    def __init__(self, g):
        super().__init__(g)
        self.image = Creature.image
        self.rect = self.image.get_rect()
        self.rect.x = 50
        self.rect.y = 50
        self.v_x = 10
        self.v_y = 10

    def update(self):
        self.rect = self.rect

    def move(self, press):
        if press[pygame.K_UP]:
            self.rect = self.rect.move(0, -10)
        if press[pygame.K_DOWN]:
            self.rect = self.rect.move(0, 10)
        if press[pygame.K_LEFT]:
            self.rect = self.rect.move(-10, 0)
        if press[pygame.K_RIGHT]:
            self.rect = self.rect.move(10, 0)
