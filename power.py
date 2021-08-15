# 道具
import pygame
import random
from settings import WIN_HEIGHT
from img_sound_text import power_imgs


class Power(pygame.sprite.Sprite):
    def __init__(self, center):
        pygame.sprite.Sprite.__init__(self)
        self.type = random.choice(power_imgs)
        self.image = self.type
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.speedy = 3


    def update(self):
        self.rect.y += self.speedy
        if self.rect.top > WIN_HEIGHT:
            self.kill()
