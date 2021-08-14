"""
class Buttons:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        self.frame = None

    def clicked(self, x: int, y: int) -> bool:
        if self.rect.collidepoint(x, y):
            return True
        return False

    def create_frame(self, x: int, y: int):
        if self.clicked(x, y):
            x, y, w, h = self.rect
            self.frame = pygame.Rect(x - 5, y - 5, w + 10, h + 10)
        else:
            self.frame = None

    def draw_frame(self, win):
        if self.frame is not None:
            pygame.draw.rect(win, WHITE, self.frame, 10)




self.sound_btn = Buttons(350, 315, 50, 50)
        self.mute_btn = Buttons(0, 0, 50, 50)
        self.buttons = [self.sound_btn, self.mute_btn]

                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        if self.sound_btn.clicked(x, y):
                            pygame.mixer.music.unpause()
                        elif self.mute_btn.clicked(x, y):
                            pygame.mixer.music.pause()
            for button in self.buttons:
                Buttons.create_frame(button, x, y)
                Buttons.draw_frame(button, self.start_win)
"""
