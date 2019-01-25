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
    image_left = load_image("character_left.png")
    image_right = load_image("character_right.png")
    image_down = load_image("character_down.png")
    image_up = load_image("character_up.png")

    def __init__(self, g):
        super().__init__(g)
        self.image = Creature.image
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
        self.v_x = 10
        self.v_y = 10

    def update(self):
        if not pygame.sprite.collide_mask(self, block):
            self.rect = self.rect.move(0, 1)

    def move(self, press):
        if press[pygame.K_UP]:
            self.rect = self.rect.move(0, -10)
            self.image = Creature.image_up
        if press[pygame.K_DOWN]:
            self.rect = self.rect.move(0, 10)
            self.image = Creature.image_down
        if press[pygame.K_LEFT]:
            self.rect = self.rect.move(-10, 0)
            self.image = Creature.image_left
        if press[pygame.K_RIGHT]:
            self.rect = self.rect.move(10, 0)
            self.image = Creature.image_right
