import time
from start_window import *
from player import *
from virus import *
from power import *
from anime import *
from people import *
from final import *


# initialize
pygame.init()
pygame.mixer.init()

# set the window
window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

# set the title
pygame.display.set_caption("病毒防衛戰")

# set the clock
clock = pygame.time.Clock()

# 讓音樂循環播放
pygame.mixer.music.play(-1)

# 病毒離開視窗後加回視窗
def new_virus():
    virus = Virus()
    all_sprites.add(virus)
    viruses.add(virus)

# 路人離開視窗後加回視窗
def new_people():
    person = People()
    all_sprites.add(person)
    people.add(person)

# timer
def timer():
    global pause_time
    current_time = time.time()  # 取得遊戲現在秒數
    total_seconds = int(current_time - START_TIME - pause_time)  # 程式實際執行秒數 = 現在累積秒數 - 開始秒數
    min = str(total_seconds // 60).zfill(2)  # zfill(2) -> 不滿兩位數自動往左補0
    sec = str(total_seconds % 60).zfill(2)
    time_str = min + ":" + sec
    time_font = pygame.font.SysFont(font_name, 35)
    time_text = time_font.render(time_str, True, WHITE)  # 文字變數 = 字體變數.render(文字, 平滑值, 文字顏色)
    window.blit(time_text, (5, WIN_HEIGHT - 25))

# pause
def pause():
    global is_pause, pause_time
    now_time = time.time()  # 紀錄暫停開始時間
    while is_pause:
        window.blit(start_bg_img, (0, 0))
        window.blit(pause_img, (50, 100))
        window.blit(player_img, (100, WIN_HEIGHT - 100))
        window.blit(talk_img, (150, WIN_HEIGHT - 160))
        Score.draw_text(window, "按P繼續遊戲", 18, BLACK, 250, 453)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    end_time = time.time()  # 紀錄暫停結束時間
                    pause_time = end_time - now_time
                    is_pause = False
        pygame.display.update()
        clock.tick(5)


show_init = True  # 判斷是否顯示start_window
running = True
is_pause = False
show_final = False
pause_time = 0


# --- Game Loop ---
while running:
    clock.tick(FPS)
    start_win = Start()
    if show_init:
        start_win.draw_init()
        show_init = False

        # set start time
        START_TIME = time.time()

        # creat a group
        all_sprites = pygame.sprite.Group()
        viruses = pygame.sprite.Group()
        vaccines = pygame.sprite.Group()
        powers = pygame.sprite.Group()
        people = pygame.sprite.Group()

        player = Player()
        all_sprites.add(player)  # add class Player() in all_sprites

        for i in range(8):  # 畫面同時有8個病毒 // Level 1
            new_virus()

        score = 0  # 分數歸零




    # 取得輸入
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # quit
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:  # 按SPACE發射
                player.shoot(all_sprites, vaccines)
            elif event.key == pygame.K_p:  # 按P暫停
                is_pause = True
                pause()


    # 更新遊戲
    all_sprites.update()

    total_seconds = time.time() - START_TIME

    # 畫面同時有7個病毒 2個人 // Level 2
    if 20.017 > total_seconds > 20:
        for i in range(1):
            new_virus()
        for i in range(2):
            new_people()

    # 畫面同時有7個病毒 3個人 // Level 3
    if 35.017 > total_seconds > 35:
        for i in range(1):
            new_people()

    # 畫面同時有9個病毒 4個人 // Level 4
    if 50.017 > total_seconds > 50:
        for i in range(2):
            new_virus()
        for i in range(1):
            new_people()


    # 病毒 疫苗hit
    hits = pygame.sprite.groupcollide(viruses, vaccines, True, True)
    for hit in hits:
        random.choice(expl_sounds).play()
        score += 20
        expl = Explosion(hit.rect.center, 'large')
        all_sprites.add(expl)
        if random.random() > 0.9:  # 掉道具機率10%
            pow = Power(hit.rect.center)
            all_sprites.add(pow)
            powers.add(pow)
        new_virus()

    # 路人 疫苗hit
    hits = pygame.sprite.groupcollide(people, vaccines, True, True)
    for hit in hits:
        player.health -= 15
        if player.health <= 0:
            die_sound.play()
            player.lives -= 1
            player.health = 100
            player.hide()
        new_people()

    # 路人 阿中hit
    hits = pygame.sprite.spritecollide(player, people, True)
    for hit in hits:
        player.health -= 20
        new_people()
        expl = Explosion(hit.rect.center, 'small')
        all_sprites.add(expl)
        if player.health <= 0:
            die_sound.play()
            player.lives -= 1
            player.health = 100
            player.hide()

    # pygame.sprite.collide_circle -> 加強碰撞判斷
    # 阿中 病毒hit
    hits = pygame.sprite.spritecollide(player, viruses, True, pygame.sprite.collide_circle)
    for hit in hits:
        player.health -= 20
        new_virus()
        expl = Explosion(hit.rect.center, 'small')
        all_sprites.add(expl)
        if player.health <= 0:
            die_sound.play()
            player.lives -= 1
            player.health = 100
            player.hide()

    # 阿中 道具hit
    hits = pygame.sprite.spritecollide(player, powers, True)
    for hit in hits:
        if hit.type == mask_img:
            player.health += 25
            if player.health > 100:
                player.health = 100
            pow0_sound.play()
        elif hit.type == alcohol_img:
            player.gunup()
            pow1_sound.play()
    if player.lives == 0:
        final_score = score
        show_final = True

    if show_final:
        final = Final()
        final.draw_final(final_score)
        show_init = True
        show_final = False



    # 畫面顯示
    window.fill(WHITE)
    window.blit(background_img, (0, 0))
    all_sprites.draw(window)  # draw items in all_sprites on the window
    Score.draw_text(window, str(score), 25, WHITE, WIN_WIDTH/2, 15)
    Score.draw_text(window, "按P暫停", 20, WHITE, 460, 570)
    Health.draw_health(window, player.health, 5, 27.5)
    Health.draw_lives(window, player.lives, player_mini_img, WIN_WIDTH - 120, 15)
    timer()

    pygame.display.update()


pygame.quit()