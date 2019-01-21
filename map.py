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


class Block(pygame.sprite.Sprite):
    image = load_image("character.png")

    def __init__(self, g, x, y):
        super().__init__(g)
        self.image = Creature.image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Map(pygame.sprite.Group):
    def level_first(self):
        pass


