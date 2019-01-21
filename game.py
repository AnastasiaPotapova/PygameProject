import os
import random
import pygame
from character import Creature
#from map import Map

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
        self.rect.x = 0
        self.rect.y = 0

    def update(self):
        while self.rect.x != 479:
            print(self.rect.x)
            self.rect = self.rect.move(1, 0)


class EndGroup(pygame.sprite.Group):
    pass



end_group = EndGroup()
group_my = pygame.sprite.Group()
pers = Creature(group_my)
running = True
end = End(end_group)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            print('+')
            #all_sprites.process_event(event)
        if event.type == pygame.KEYDOWN:
            print('-')
            pers.move(pygame.key.get_pressed())
        #if ballrect.colliderect(bliprect):
    screen.fill((255, 255, 255))
    pers.update()
    group_my.draw(screen)

    # all_sprites.update()
    # all_sprites.draw(screen)
    # if all_sprites.check_boom():
    #     #end_group.update()
    #     end_group.draw(screen)
    pygame.display.flip()

pygame.quit()
