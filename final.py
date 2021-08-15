from settings import *
from img_sound_text import *
from view import *

class Final:
    def __init__(self):
        self.final_win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

    def draw_final(self, final_score):
        """Draw the start window"""
        self.final_win.blit(start_bg_img, (0, 0))
        self.final_win.blit(score_img, (117, 50))
        self.final_win.blit(player_img, (100, WIN_HEIGHT - 100))
        self.final_win.blit(talk_img, (150, WIN_HEIGHT - 160))
        Score.draw_text(self.final_win, "按Enter繼續", 18, BLACK, 250, 453)
        Score.draw_text(self.final_win, str(final_score), 120, YELLOW, WIN_WIDTH/2, 160)

        clock = pygame.time.Clock()
        waiting = True
        while waiting:
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # quit
                    pygame.quit()
                    quit()
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_RETURN:  # 按下Enter回初始畫面
                        waiting = False

            pygame.display.update()








