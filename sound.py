import pygame


class Sound():
    """A class to store all music and sound effect files"""
    # Initialising sound settings for smoother play
    pygame.mixer.pre_init(44100, -16, 2, 2048)
    pygame.mixer.init()
    pygame.init()

    def __init__(self):
        # load sound effects
        self.p1_fire = pygame.mixer.Sound('sound/tank_fire01.ogg')
        self.p2_fire = pygame.mixer.Sound('sound/tank_fire02.ogg')
        self.explosion = pygame.mixer.Sound('sound/explosion.ogg')
        self.confirm = pygame.mixer.Sound('sound/confirm.ogg')
        self.title_music = 'sound/intro.ogg'
        self.battle_music = 'sound/combat.ogg'
        self.victory_music = 'sound/victory.ogg'

    def play(self, music, how_many_times):
        pygame.mixer.music.load(music)
        pygame.mixer.music.play(how_many_times)
