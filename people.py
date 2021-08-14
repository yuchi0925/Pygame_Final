# 路人
import pygame
import random
from img_sound_text import people_imgs
from settings import WIN_WIDTH, WIN_HEIGHT, RED


class People(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.type = random.choice(people_imgs)
        self.image = self.type
        self.rect = self.image.get_rect()
        self.radius = 35  # 碰撞圓形半徑
        # pygame.draw.circle(self.image, RED, self.rect.center, self.radius)  #檢查碰撞半徑
        self.rect.x = random.randrange(0, WIN_WIDTH - self.rect.width)
        self.rect.y = random.randrange(-150, -100)
        self.speedy = random.randrange(2, 10)

    def update(self):
        self.rect.y += self.speedy
        # self.rect.x += self.speedx
        if self.rect.top > WIN_HEIGHT or self.rect.left > WIN_WIDTH or self.rect.right < 0:
            self.rect.x = random.randrange(0, WIN_WIDTH - self.rect.width)
            self.rect.y = random.randrange(-150, -100)
            self.speedy = random.randrange(2, 10)