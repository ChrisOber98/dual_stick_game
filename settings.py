class Settings:
    def __init__(self):
        self.fps = 60

        self.window_height = 800
        self.window_width = 1200
        self.window_bg_color = (255, 255, 255)
        self.winodw_caption = "Dual Stick Game"

        self.gameplay_window_offset = 50
        self.gameplay_window_height = (
            self.window_height - self.gameplay_window_offset * 2
        )
        self.gameplay_window_width = self.window_width - self.gameplay_window_offset * 2
        self.gameplay_window_bg_color = (0, 0, 0)

        self.player_width = 25
        self.player_height = 25
        self.player_color = (255, 0, 0)
        self.player_speed = 5
