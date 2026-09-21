import pygame


class Player:
    def __init__(self, game):
        self.settings = game.settings

        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()

        self.rect = pygame.Rect(
            (0, 0), (self.settings.player_width, self.settings.player_height)
        )
        self.rect.center = self.screen_rect.center

    def draw(self):
        pygame.draw.rect(self.screen, self.settings.player_color, self.rect)
