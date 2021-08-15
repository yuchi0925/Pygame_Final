from settings import *
from img_sound_text import *
from view import *

class Start:
    def __init__(self):
        self.start_win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

    def draw_init(self):
        """Draw the start window"""
        self.start_win.blit(start_bg_img, (0, 0))
        self.start_win.blit(title_img, (25, 40))
        self.start_win.blit(arrow_right_img, (0, 190))
        self.start_win.blit(arrow_left_img, (-100, 190))
        self.start_win.blit(space_img, (-75, 260))
        self.start_win.blit(move_img, (150, 185))
        self.start_win.blit(shoot_img, (150, 260))
        self.start_win.blit(virus_img, (420, 120))
        self.start_win.blit(player_img, (100, WIN_HEIGHT - 100))
        self.start_win.blit(talk_img, (150, WIN_HEIGHT - 160))
        Score.draw_text(self.start_win, "按Enter開始遊戲", 18, BLACK, 250, 453)

        clock = pygame.time.Clock()
        waiting = True
        while waiting:
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # quit
                    pygame.quit()
                    quit()
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_RETURN:  # 按下SPACE跳出初始畫面
                        waiting = False

            pygame.display.update()








