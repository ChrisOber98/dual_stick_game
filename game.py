import pygame

from settings import Settings
from ui_border import UiBorder

class Game:
    def __init__(self):
        pygame.init()

        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.window_width, self.settings.window_height))
        pygame.display.set_caption(self.settings.winodw_caption)

        self.ui_border = UiBorder(self)

        self.running = True

    def run_game(self):
        while self.running:
            self._check_events()
            self._update_game()
            self._draw_screen()

        pygame.quit()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._check_quit_events()

    def _check_quit_events(self):
        self.running = False

    def _update_game(self):
        pass

    def _draw_screen(self):
        self.screen.fill(self.settings.window_bg_color)
        self.ui_border.draw()
        pygame.display.flip()



if __name__ == "__main__":
    my_game = Game()
    my_game.run_game()