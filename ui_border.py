import pygame


class UiBorder:
    def __init__(self, game):
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()

        self.settings = game.settings

        self.border_color = (0, 0, 0)

        self.border_width = 5

    def draw(self):
        pygame.draw.line(
            self.screen,
            self.border_color,
            self.settings.ui_border_top_left,
            self.settings.ui_border_top_right,
            self.settings.ui_thickness,
        )
        pygame.draw.line(
            self.screen,
            self.border_color,
            self.settings.ui_border_top_right,
            self.settings.ui_border_bottom_right,
            self.settings.ui_thickness,
        )
        pygame.draw.line(
            self.screen,
            self.border_color,
            self.settings.ui_border_bottom_right,
            self.settings.ui_border_bottom_left,
            self.settings.ui_thickness,
        )
        pygame.draw.line(
            self.screen,
            self.border_color,
            self.settings.ui_border_bottom_left,
            self.settings.ui_border_top_left,
            self.settings.ui_thickness,
        )
