from settings import *
from img_sound_text import *
from view import *

class Final:
    def __init__(self):
        self.final_win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

    def draw_final(self, final_score):
        """Draw the start window"""
        self.final_win.blit(start_bg_img, (0, 0))

        Score.draw_text(self.final_win, f"score : {final_score}", 50, WHITE, WIN_WIDTH/2, 250)

        clock = pygame.time.Clock()
        waiting = True
        while waiting:
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_RETURN:  # 按下Enter回初始畫面
                        waiting = False

            pygame.display.update()








