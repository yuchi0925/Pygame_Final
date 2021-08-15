# 阿中
from settings import WIN_WIDTH, WIN_HEIGHT, RED
from img_sound_text import *


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = player_img
        self.rect = self.image.get_rect()
        self.radius = 45  # 碰撞圓形半徑
        # pygame.draw.circle(self.image, RED, self.rect.center, self.radius)  #檢查碰撞半徑
        self.rect.centerx = WIN_WIDTH/2
        self.rect.bottom = WIN_HEIGHT - 10
        self.speedx = 8
        self.health = 100      # 生命值
        self.lives = 3         # 復活次數
        self.hidden = False
        self.hide_time = 0
        self.gun = 1
        self.gun_time = 0


    def update(self):
        now = pygame.time.get_ticks()
        if self.gun > 1 and now - self.gun_time > 3000:
            self.gun -= 1
            self.gun_time = now

        if self.hidden and now - self.hide_time > 1000:
            self.hidden = False
            self.rect.centerx = WIN_WIDTH / 2
            self.rect.bottom = WIN_HEIGHT - 10

        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_RIGHT]:
            self.rect.x += self.speedx
        if key_pressed[pygame.K_LEFT]:
            self.rect.x -= self.speedx

        if self.rect.right > WIN_WIDTH:  # player不超出右邊
            self.rect.right = WIN_WIDTH
        if self.rect.left < 0:  # player不超出左邊
            self.rect.left = 0


    def shoot(self, all_sprites, vaccines):
        if not(self.hidden):  # 避免人物復活但還沒出現時 也能發射子彈
            if self.gun == 1:
                vaccine = Vaccine(self.rect.centerx, self.rect.top)
                all_sprites.add(vaccine)
                vaccines.add(vaccine)
                shoot_sound.play()
            elif self.gun >= 2:
                vaccine1 = Vaccine(self.rect.left, self.rect.centery)
                vaccine2 = Vaccine(self.rect.right, self.rect.centery)
                all_sprites.add(vaccine1)
                all_sprites.add(vaccine2)
                vaccines.add(vaccine1)
                vaccines.add(vaccine2)
                shoot_sound.play()


    def hide(self):
        self.hidden = True
        self.hide_time = pygame.time.get_ticks()
        self.rect.center = (WIN_WIDTH/2, WIN_HEIGHT+500)


    def gunup(self):
        self.gun += 1
        self.gun_time = pygame.time.get_ticks()


class Vaccine(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = vaccine_img
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y
        self.speedy = -10


    def update(self):
        self.rect.y += self.speedy
        if self.rect.bottom < 0:  # 疫苗超出視窗外 即移除
            self.kill()