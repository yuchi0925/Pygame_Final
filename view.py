import pygame
import os
from settings import RED, WHITE
from img_sound_text import font_name


class Health(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)


    def draw_health(surf, hp, x, y):
        if hp < 0:
            hp = 0
        BAR_LENGTH = 100
        BAR_HEIGHT = 15
        fill = hp / 100 * BAR_LENGTH
        outline_rect = pygame.Rect(x, y, BAR_LENGTH, BAR_HEIGHT)  # 防護力外框
        fill_rect = pygame.Rect(x, y, fill, BAR_HEIGHT)  # 防護力填色
        pygame.draw.rect(surf, RED, fill_rect)
        pygame.draw.rect(surf, WHITE, outline_rect, 2)


    # 畫生命數
    def draw_lives(surf, lives, img, x, y):
        for i in range(lives):
            img_rect = img.get_rect()
            img_rect.x = x + 40 * i  # 取固定間隔
            img_rect.y = y
            surf.blit(img, img_rect)



class Score(pygame.sprite.Sprite):
    def __init__(self, score):
        pygame.sprite.Sprite.__init__(self)
        self.text = score

    def add_virus(self):
        self.text += 20

    def draw_text(surf, text, size, color, x, y):
        """Draw Text"""
        font = pygame.font.Font(font_name, size)
        text_surface = font.render(text, True, color)  # 文字, 平滑值, 顏色
        text_rect = text_surface.get_rect()
        text_rect.centerx = x
        text_rect.top = y
        surf.blit(text_surface, text_rect)








