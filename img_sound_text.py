import pygame
import os

# initialize
pygame.init()
pygame.mixer.init()



# load images
# start_window
title_img = pygame.transform.scale(pygame.image.load("img/title.png"), (450, 140))
arrow_right_img = pygame.transform.scale(pygame.image.load("img/arrow_right.png"), (350, 80))
arrow_left_img = pygame.transform.scale(pygame.image.load("img/arrow_left.png"), (350, 80))
start_bg_img = pygame.transform.scale(pygame.image.load("img/start_bg.png"), (500, 600))
space_img = pygame.transform.scale(pygame.image.load("img/space.png"), (400, 80))
move_img = pygame.transform.scale(pygame.image.load("img/move.png"), (450, 80))
shoot_img = pygame.transform.scale(pygame.image.load("img/shoot.png"), (450, 80))
talk_img = pygame.transform.scale(pygame.image.load("img/talk.png"), (200, 80))

# game_window
background_img = pygame.transform.scale(pygame.image.load("img/background.jpg"), (500, 600))
player_img = pygame.transform.scale(pygame.image.load("img/chen.png"), (70, 100))
player_mini_img = pygame.transform.scale(player_img, (28, 40))
vaccine_img = pygame.transform.scale(pygame.image.load("img/vaccine.png"), (50, 100))
virus_img = pygame.transform.scale(pygame.image.load("img/virus.png"), (45, 45))

# 路人
people_imgs = []
for i in range (1, 7):
    people_img = pygame.transform.scale(pygame.image.load(f"img/people{i}.png"), (36, 72))
    people_imgs.append(people_img)

# 爆炸
expl_anim = {}
expl_anim['large'] = []
expl_anim['small'] = []
for i in range(9):
    expl_img = pygame.image.load(os.path.join("img", f"expl{i}.png"))
    expl_anim['large'].append(pygame.transform.scale(expl_img, (75, 75)))
    expl_anim['small'].append(pygame.transform.scale(expl_img, (30, 30)))

# 道具
mask_img = pygame.transform.scale(pygame.image.load("img/mask.png"), (60, 30))
alcohol_img = pygame.transform.scale(pygame.image.load("img/alcohol.png"), (80, 50))
power_imgs = [mask_img, alcohol_img]



# load music
shoot_sound = pygame.mixer.Sound(os.path.join("sound", "shoot.wav"))
gun_sound = pygame.mixer.Sound(os.path.join("sound", "pow0.wav"))
shield_sound = pygame.mixer.Sound(os.path.join("sound", "pow1.wav"))
die_sound = pygame.mixer.Sound(os.path.join("sound", "die.wav"))
expl_sounds = [pygame.mixer.Sound(os.path.join("sound", "expl0.wav")),
               pygame.mixer.Sound(os.path.join("sound", "expl1.wav"))]
pygame.mixer.music.load(os.path.join("sound", "bgm.mp3"))
pygame.mixer.music.set_volume(0.4)  # 背景音樂調成原本的0.6倍



# load font
font_name = os.path.join("font.ttf")  # 微軟正黑體