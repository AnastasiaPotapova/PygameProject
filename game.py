import os
import random
import pygame

pygame.init()
size = width, height = 479, 320
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


class End(pygame.sprite.Sprite):
    image = load_image('finish.png')

    def __init__(self, g):
        super().__init__(g)
        self.image = End.image
        self.rect = self.image.get_rect()
        self.rect.x = -479
        self.rect.y = 0

    def update(self):
        if self.rect.x < 0:
            self.rect = self.rect.move(1, 0)


class EndGroup(pygame.sprite.Group):
    pass


class Block(pygame.sprite.Sprite):
    image = load_image("block.jpg")

    def __init__(self, g, x, y):
        super().__init__(g)
        self.image = Block.image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        self.rect = self.rect


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
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = 0
        self.rect.y = 0
        self.v_x = 10
        self.v_y = 10

    def update(self):
        a = [1 if pygame.sprite.collide_mask(self, x) else 0 for x in mm]
        if 1 in a:
            pass
        else:
            self.rect = self.rect.move(0, 1)

    def move(self, press):
        if press[pygame.K_UP]:
            self.rect = self.rect.move(0, -100)
            self.image = Creature.image_up
        if press[pygame.K_DOWN]:
            self.image = Creature.image_down
        if press[pygame.K_LEFT]:
            self.rect = self.rect.move(-10, 0)
            self.image = Creature.image_left
        if press[pygame.K_RIGHT]:
            self.rect = self.rect.move(10, 0)
            self.image = Creature.image_right

    def check(self):
        return not(0 < self.rect.x < width - 50 or 0 < self.rect.y < height-50)


end_group = EndGroup()
group_my = pygame.sprite.Group()
pers = Creature(group_my)
mm = []
for i in range(0, width, 20):
    mm.append(Block(group_my, i, 280 - i*0.5))
running = True
end = End(end_group)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            print('+')
            # all_sprites.process_event(event)
        if event.type == pygame.KEYDOWN:
            pers.move(pygame.key.get_pressed())
        # if ballrect.colliderect(bliprect):
    screen.fill((255, 255, 255))
    group_my.update()
    group_my.update()
    group_my.draw(screen)
    if pers.check():
        end_group.update()
        end_group.draw(screen)
    pygame.display.flip()

pygame.quit()
