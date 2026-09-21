import pygame


class GameplayWindow:
    def __init__(self, game):
        self.settings = game.settings

        self.screen_window = game.screen_window
        self.screen_window_rect = game.screen_window.get_rect()

        self.surface = pygame.Surface(
            (self.settings.gameplay_window_width, self.settings.gameplay_window_height)
        )

    def draw(self):
        self.screen_window.blit(
            self.surface,
            (
                self.settings.gameplay_window_offset,
                self.settings.gameplay_window_offset,
            ),
        )
