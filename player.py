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

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        self.is_moving_up = False
        self.is_moving_down = False
        self.is_moving_left = False
        self.is_moving_right = False

    def update(self):
        if self.is_moving_up:
            self.y -= self.settings.player_speed

        if self.is_moving_down:
            self.y += self.settings.player_speed

        if self.is_moving_left:
            self.x -= self.settings.player_speed

        if self.is_moving_right:
            self.x += self.settings.player_speed

        self.rect.x = self.x
        self.rect.y = self.y

    def draw(self):
        pygame.draw.rect(self.screen, self.settings.player_color, self.rect)
