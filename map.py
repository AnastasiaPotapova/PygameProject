import os
import random
import pygame

size = width, height = 500, 500
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


class Block(pygame.sprite.Sprite):
    image = load_image("block.jpg")

    def __init__(self, g):
        super().__init__(g)
        self.image = Block.image
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 280

    def update(self):
        self.rect = self.rect


