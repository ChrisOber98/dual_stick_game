import pygame

from gameplay_window import GameplayWindow
from player import Player
from settings import Settings


class Game:
    def __init__(self):
        pygame.init()

        self.settings = Settings()

        self.screen_window = pygame.display.set_mode(
            (self.settings.window_width, self.settings.window_height)
        )
        pygame.display.set_caption(self.settings.winodw_caption)

        self.gameplay_window = GameplayWindow(self)

        self.player = Player(self)

        self.clock = pygame.time.Clock()

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
                self._check_quit_events(event)
            if event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            if event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_quit_events(self, event):
        self.running = False

    def _check_keydown_events(self, event):
        if event.key == pygame.K_w:
            self.player.is_moving_up = True
        elif event.key == pygame.K_s:
            self.player.is_moving_down = True
        elif event.key == pygame.K_a:
            self.player.is_moving_left = True
        elif event.key == pygame.K_d:
            self.player.is_moving_right = True

    def _check_keyup_events(self, event):
        if event.key == pygame.K_w:
            self.player.is_moving_up = False
        elif event.key == pygame.K_s:
            self.player.is_moving_down = False
        elif event.key == pygame.K_a:
            self.player.is_moving_left = False
        elif event.key == pygame.K_d:
            self.player.is_moving_right = False

    def _update_game(self):
        self._update_gameplay_window()
        self._update_screen_window()
        self.player.update()

    def _update_gameplay_window(self):
        self.gameplay_window.surface.fill(self.settings.gameplay_window_bg_color)

    def _update_screen_window(self):
        self.screen_window.fill(self.settings.window_bg_color)

    def _draw_screen(self):
        self.player.draw()
        self.gameplay_window.draw()
        pygame.display.flip()
        self.clock.tick(self.settings.fps)


if __name__ == "__main__":
    my_game = Game()
    my_game.run_game()
