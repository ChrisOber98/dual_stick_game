class Settings:
    def __init__(self):
        self.window_height = 800
        self.window_width = 1200
        self.window_bg_color = (255, 255, 255)
        self.winodw_caption = "Dual Stick Game"

        self.ui_border_width = 75
        self.ui_thickness = 5
        self.ui_border_top_left = (self.ui_border_width, self.ui_border_width)
        self.ui_border_top_right = (self.window_width - self.ui_border_width, self.ui_border_width)
        self.ui_border_bottom_left = (self.ui_border_width, self.window_height - self.ui_border_width)
        self.ui_border_bottom_right = (self.window_width - self.ui_border_width, self.window_height - self.ui_border_width)