import os
import random
import pygame

pygame.init()
size = width, height = WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
FPS = 60


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


def terminate():
    pygame.quit()


def start_screen():
    intro_text = ["GrayCat", "",
                  "Правила игры",
                  "Действия игры происходят в сером и мрачном мире,",
                  "где все цвета забрали злые собаки.",
                  "Но некоторые цвета сбежали из-за заточения ввиде звезд!",
                  "Но им нужна помощь","Ваша задача забрать все звезды и сделать мир цветным!"]

    fon = pygame.transform.scale(load_image('fon.jpg'), (WIDTH, HEIGHT))
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 30)
    text_coord = 50
    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color('black'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 10
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            # if event.type == pygame.MOUSEMOTION:
            #     mouse.activ(pygame.mouse.get_pos())
            #     pygame.mouse.set_visible(False)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if btn.process_event(event):
                    return 'data/level1.txt'
        # mg.update()
        # mg.draw(screen)
        btn_group.update()
        btn_group.draw(screen)

        pygame.display.flip()
        clock.tick(FPS)


def game(level_name):
    mm = []
    with open(level_name, 'r') as x:
        data = x.read()
    data = data.split('\n')
    lst = [[], []]
    lst[0] = [x.split(',') for x in data[0].split(';')]
    lst[1] = [x.split(',') for x in data[1].split(';')]
    for i in lst[0]:
        mm.append(Block(group_my, int(i[1]), int(i[0])))
    for i in lst[1]:
        Star(star_group, int(i[0]), int(i[1]))
    running = True
    clock = pygame.time.Clock()
    while running:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                print(event.pos)
                # all_sprites.process_event(event)
            if event.type == pygame.KEYDOWN:
                pers.move(pygame.key.get_pressed())
            if event.type == pygame.KEYUP:
                pers.x = 0
            if event.type == pygame.MOUSEMOTION:
                mouse.activ(pygame.mouse.get_pos())
                pygame.mouse.set_visible(False)
        screen.fill((255, 255, 255))
        door_group.update()
        door_group.draw(screen)
        group_my.update()
        group_my.draw(screen)
        pers_group.update()
        pers_group.draw(screen)
        star_group.check()
        star_group.update()
        star_group.draw(screen)
        if pers.bonuse_counter > 20:
            boss_group.update()
            boss_group.draw(screen)
        if pers.check():
            end_group.update()
            end_group.draw(screen)
        mg.draw(screen)
        pygame.display.flip()


class Button(pygame.sprite.Sprite):
    image = load_image('start.png')

    def __init__(self, g, x, y):
        super().__init__(g)
        self.image = Button.image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        self.rect = self.rect

    def process_event(self, event):
        if self.rect.collidepoint(event.pos):
            return True


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


class Door(pygame.sprite.Sprite):
    image = load_image("door.jpg")

    def __init__(self, g, x, y):
        super().__init__(g)
        self.image = Door.image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        self.rect = self.rect


class Mouse(pygame.sprite.Sprite):
    image = load_image('arrow.jpg', -1)

    def __init__(self, group):
        super().__init__(group)
        self.image = Mouse.image
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0

    def activ(self, a):
        self.rect.x = a[0]
        self.rect.y = a[1]


class StarGroup(pygame.sprite.Group):
    def check(self):
        for sprite in self.sprites():
            if sprite.check():
                sprite.kill()


class Star(pygame.sprite.Sprite):
    image = load_image("star.png")

    def __init__(self, g, x, y):
        super().__init__(g)
        self.image = Star.image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        self.rect = self.rect

    def check(self):
        return pygame.sprite.spritecollideany(self, pers_group)


class EndGroup(pygame.sprite.Group):
    pass


class MouseGroup(pygame.sprite.Group):
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
    image_right = load_image("dog_right.jpg", -1)
    image_left = load_image("dog_left.jpg", -1)

    def __init__(self, g):
        super().__init__(g)
        self.image_right = Dog.image_right
        self.image_left = Dog.image_left
        self.image = self.image_right
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = height - 95

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
    image = load_image("character'.jpg", -1)
    image_left = load_image("character_left.png", -1)
    image_right = load_image("character_right.png", -1)
    image_up = load_image("character_up.png")

    def __init__(self, g):
        super().__init__(g)
        self.image = Creature.image
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = 0
        self.rect.y = 0
        self.jump_count = 15
        self.is_jump = False
        self.x = 0
        self.y = 0
        self.bonuse_counter = 0
        self.k = False

    def update(self):
        if pygame.sprite.spritecollideany(self, group_my):
            pass
        else:  # not(self.is_jump):
            self.rect = self.rect.move(0, 5)
        if self.x == 1 and self.k == pygame.sprite.spritecollideany(self, group_my):
            if self.rect.x + 5 < width:
                self.rect = self.rect.move(5, 0)
            else:
                self.rect.x = 0
        if self.x == -1 and self.k == pygame.sprite.spritecollideany(self, group_my):
            if self.rect.x - 5 > 0:
                self.rect = self.rect.move(-5, 0)
            else:
                self.rect.x = width - 50
        self.k = pygame.sprite.spritecollideany(self, group_my)


        if pers.is_jump:
            pers.jump()
        if pygame.sprite.spritecollideany(self, star_group):
            self.bonuse_counter += 10

    def move(self, press):
        if press[pygame.K_UP]:
            self.is_jump = True
            # self.image = Creature.image_up
            # self.rect.width = self.image.get_rect().width
            # self.rect.height = self.image.get_rect().height
        if press[pygame.K_LEFT]:
            self.x = -1
            self.image = Creature.image_left
            self.rect.width = self.image.get_rect().width
            self.rect.height = self.image.get_rect().height
        if press[pygame.K_RIGHT]:
            self.image = Creature.image_right
            self.rect.width = self.image.get_rect().width
            self.rect.height = self.image.get_rect().height
            self.x = 1

    def check(self):
        return not (0 < self.rect.x < width - 50 or 0 < self.rect.y < height - 50) or \
               pygame.sprite.spritecollideany(self, door_group)

    def jump(self):
        if self.is_jump:
            if self.jump_count >= -15:
                dy = int((self.jump_count ** 2) / 10)
                if self.jump_count >= 0:
                    self.rect = self.rect.move(0, -dy)
                self.jump_count -= 1
            else:
                self.jump_count = 15
                self.is_jump = False


class Boss(pygame.sprite.Sprite):
    image = load_image('ghost.jpg', -1)

    def __init__(self, g):
        super().__init__(g)
        self.image = Boss.image
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = 0
        self.rect.y = 0
        self.v = 1

    def update(self):
        if pers.rect.x > self.rect.x:
            self.rect = self.rect.move(self.v, 0)
        elif pers.rect.x < self.rect.x:
            self.rect = self.rect.move(-self.v, 0)

        if pers.rect.y > self.rect.y:
            self.rect = self.rect.move(0, self.v)
        elif pers.rect.y < self.rect.y:
            self.rect = self.rect.move(0, -self.v)

        if abs(pers.rect.x - self.rect.x) <= 150 and abs(pers.rect.y - self.rect.y) <= 150:
            self.v = 3
        else:
            self.v = 1



end_group = EndGroup()
group_my = pygame.sprite.Group()
pers_group = pygame.sprite.Group()
star_group = StarGroup()
door_group = pygame.sprite.Group()
btn_group = pygame.sprite.Group()
boss_group = pygame.sprite.Group()
boss = Boss(boss_group)
mg = MouseGroup()
dog = Dog(group_my)
pers = Creature(pers_group)
end = End(end_group)
mouse = Mouse(mg)
door = Door(door_group, 400, height - 100)
btn = Button(btn_group, 10, 400)
k = None
while not(k):
    k = start_screen()
game(k)

pygame.quit()
