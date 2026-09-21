import pygame


class Player:
    def __init__(self, game):
        self.settings = game.settings

        self.screen_window = game.screen_window
        self.screen_window_rect = game.screen_window.get_rect()

        self.gameplay_window = game.gameplay_window
        self.gameplay_window_rect = game.gameplay_window.surface.get_rect()

        self.rect = pygame.Rect(
            (0, 0), (self.settings.player_width, self.settings.player_height)
        )
        self.rect.center = self.gameplay_window_rect.center

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        self.is_moving_up = False
        self.is_moving_down = False
        self.is_moving_left = False
        self.is_moving_right = False

    def update(self):
        if self.is_moving_up and self.rect.top > self.gameplay_window_rect.top:
            self.y -= self.settings.player_speed

        if self.is_moving_down and self.rect.bottom < self.gameplay_window_rect.bottom:
            self.y += self.settings.player_speed

        if self.is_moving_left and self.rect.left > self.gameplay_window_rect.left:
            self.x -= self.settings.player_speed

        if self.is_moving_right and self.rect.right < self.gameplay_window_rect.right:
            self.x += self.settings.player_speed

        self.rect.x = self.x
        self.rect.y = self.y

    def draw(self):
        pygame.draw.rect(
            self.gameplay_window.surface, self.settings.player_color, self.rect
        )
