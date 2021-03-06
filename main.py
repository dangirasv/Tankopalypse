import pygame
from pygame.sprite import Group

import game_functions as gf
from settings import Settings
from tank import Tank
from button import Button
from score import Score
from sound import Sound


def run_game():
    # Initialize game, settings and screen object
    pygame.init()
    main_clock = pygame.time.Clock()
    game_set = Settings()
    screen = pygame.display.set_mode((game_set.screen_width, game_set.screen_height))
    pygame.display.set_caption('Tankopalypse')

    # Create the Play button
    play_button = Button(game_set, screen, 'Play')

    # Create Player tanks
    p1 = Tank(game_set, screen, 'black', 'p1')
    p2 = Tank(game_set, screen, 'red', 'p2')

    # Create instances for player names and lives
    score = Score(game_set, screen)

    # Create instance for sound management, start title music
    sound = Sound()
    sound.play(sound.title_music, -1)  # -1 for continuous play

    # Create obstacles
    obstacles = Group()
    gf.create_obstacles(screen, obstacles)

    # Create two bullet groups, each for separate player
    bullets1 = Group()
    bullets2 = Group()

    while True:
        gf.check_events(game_set, screen, p1, p2, bullets1, bullets2, play_button, score, sound)
        if game_set.game_active:
            p1.update()
            p2.update()
            gf.update_bullets(game_set, screen, p1, p2, obstacles, bullets1, bullets2, score, sound)
        gf.update_screen(game_set, screen, p1, p2, obstacles, bullets1, bullets2, play_button, score)
        main_clock.tick(60)  # limiting iterations per sec, or FPS


run_game()

"""
To do:
Add tank explosion animation
"""
