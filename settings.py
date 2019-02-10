"""import pygame

# Initialising sound settings for smoother play
pygame.mixer.pre_init(44100, -16, 2, 2048)
pygame.mixer.init()
pygame.init()"""


class Settings():
    """A class to store all settings for Tankopalypse"""
    
    def __init__(self):
        """Games static settings"""
        # Screen settings
        self.screen_width = 1000
        self.screen_height = 800
        self.bg_color = (0, 0, 0)
        self.name_bg_color = (189, 137, 88)

        # Tanks starting positions and settings
        self.p1_start_loc_x = 50
        self.p1_start_loc_y = int(self.screen_height / 2 - 35)
        # -35 because tank rect is 70, so 35th pixel is its central point
        self.p1_start_facing = 'self.image_r'
        self.p1_lives = 3
        
        self.p2_start_loc_x = int(self.screen_width - 120)
        self.p2_start_loc_y = int(self.screen_height / 2 - 35)
        self.p2_start_facing = 'self.image_l'
        self.p2_lives = 3
        
        self.tank_speed_factor = 3
        
        self.bullet_speed_factor = 12
        self.bullet_cooldown = 30  # or 2 bullets max per sec since we work with 60 ticks per sec clock
        # how much iterations passed since last bullet fired for both players
        # starting  value is same as bullet_cooldown value so the players could fire immediately
        self.last_bullet_fired1 = self.bullet_cooldown
        self.last_bullet_fired2 = self.bullet_cooldown
        
        # always starting game in an inactive mode
        self.game_active = False
