import os
import random
import pygame

pygame.init()
size = width, height = 800, 600
screen = pygame.display.set_mode(size)


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error as message:
        print('Cannot load image:', name)
        raise SystemExit(message)
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    image = image.convert_alpha()
    return image


class End(pygame.sprite.Sprite):
    image = load_image('final.jpg')

    def __init__(self, g):
        super().__init__(g)
        self.image = End.image
        self.rect = self.image.get_rect()
        self.rect.x = -800
        self.rect.y = 0

    def update(self):
        if self.rect.x < 0:
            self.rect = self.rect.move(10, 0)


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


class Dog(pygame.sprite.Sprite):
    image_right = load_image("dog_right.png", -1)
    image_left = load_image("dog_left.png", -1)

    def __init__(self, g):
        super().__init__(g)
        self.image_right = Dog.image_right
        self.image_left = Dog.image_left
        self.image = self.image_right
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = height - 180

    def update(self):
        if self.rect.x < width and self.image == self.image_right:
            self.rect = self.rect.move(5, 0)
        elif self.rect.x > 0 and self.image == self.image_left:
            self.rect = self.rect.move(-5, 0)
        if self.rect.x >= width - self.rect.width:
            self.image = self.image_left
        elif self.rect.x <= 0:
            self.image = self.image_right


class Creature(pygame.sprite.Sprite):
    image = load_image("character.png", -1)
    image_left = load_image("character_left.png", -1)
    image_right = load_image("character_right.png", -1)
    image_down = load_image("character_down.png", -1)
    image_up = load_image("character_up.png", -1)

    def __init__(self, g):
        super().__init__(g)
        self.image = Creature.image
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = 0
        self.rect.y = 0
        self.v_x = 10
        self.v_y = 80
        self.jump_count = 25
        self.is_jump = False

    def update(self):
        a = [1 if pygame.sprite.collide_mask(self, x) else 0 for x in mm]
        if 1 in a:
            pass
        elif not(self.is_jump):
            self.rect = self.rect.move(0, 5)

    def move(self, press):
        a = [1 if pygame.sprite.collide_mask(self, x) else 0 for x in mm]
        if press[pygame.K_UP]:
            self.is_jump = True

            #изменение у координаты
        if press[pygame.K_DOWN]:
            self.image = Creature.image_down
        if press[pygame.K_LEFT] and 1 in a:
            self.rect = self.rect.move(-10, 0)
            self.image = Creature.image_left
        if press[pygame.K_RIGHT] and 1 in a:
            self.image = Creature.image_right
            self.rect = self.rect.move(10, 0)

    def check(self):
        return not (0 < self.rect.x < width - 50 or 0 < self.rect.y < height - 50)

    def jump(self):
        if self.is_jump:
            if self.jump_count >= -25:
                dy = int((self.jump_count ** 2) / 15)
                if self.jump_count >= 0:
                    self.rect.y -= dy
                else:
                    self.rect.y += dy
                self.jump_count -= 1
            else:
                self.jump_count = 25
                self.is_jump = False

#ЕТО СМЭРТЬ
   # def jump(self):
   #      if self.is_jump:
   #          if self.jump_count >= -20:
   #              dy = (self.jump_count ** 2) // 10
   #              if self.jump_count > 0:
   #                  self.rect.y -= dy
   #              else:
   #                  self.rect.y += dy
   #              self.jump_count -= 1
   #          else:
   #              self.jump_count = 20
   #              self.is_jump = False

end_group = EndGroup()
group_my = pygame.sprite.Group()
mm = []
for i in range(0, width, 20):
    mm.append(Block(group_my, i, height - 40))
pers = Creature(group_my)
dog = Dog(group_my)
running = True
end = End(end_group)
clock = pygame.time.Clock()

while running:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            print('+')
            # all_sprites.process_event(event)
        if event.type == pygame.KEYDOWN:
            pers.move(pygame.key.get_pressed())
    screen.fill((255, 255, 255))
    group_my.update()
    group_my.draw(screen)
    if pers.check():
        end_group.update()
        end_group.draw(screen)
    pygame.display.flip()
    if pers.is_jump:
        pers.jump()
pygame.quit()
