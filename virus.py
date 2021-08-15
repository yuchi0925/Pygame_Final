# 病毒
import pygame
import random
from img_sound_text import virus_img
from settings import WIN_WIDTH, WIN_HEIGHT, RED


class Virus(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = virus_img
        self.image_ori = self.image  # 每次旋轉要以原圖旋轉，如果以旋轉後的圖再旋轉，失真會疊加造成行為錯誤
        self.rect = self.image.get_rect()
        self.radius = 20   # 碰撞圓形半徑
        # pygame.draw.circle(self.image, RED, self.rect.center, self.radius)  # 檢查碰撞半徑
        self.rect.x = random.randrange(0, WIN_WIDTH - self.rect.width)
        self.rect.y = random.randrange(-150, -100)
        self.speedy = random.randrange(2, 10)
        self.speedx = random.randrange(-3, 3)
        self.total_degree = 0
        self.rotate_degree = random.randrange(-3, 3)  # 病毒旋轉角度


    def rotate(self):
        self.total_degree += self.rotate_degree
        self.total_degree = self.total_degree % 360  # 避免超過360度
        self.image = pygame.transform.rotate(self.image_ori, self.total_degree)
        center_ori = self.rect.center  # 旋轉中心要固定
        self.rect = self.image.get_rect()
        self.rect.center = center_ori


    def update(self):
        self.rotate()
        self.rect.y += self.speedy
        self.rect.x += self.speedx
        if self.rect.top > WIN_HEIGHT or self.rect.left > WIN_WIDTH or self.rect.right < 0:
            self.rect.x = random.randrange(0, WIN_WIDTH - self.rect.width)
            self.rect.y = random.randrange(-150, -100)
            self.speedy = random.randrange(2, 10)
            self.speedx = random.randrange(-3, 3)

