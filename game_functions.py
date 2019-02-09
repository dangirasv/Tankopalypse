import sys
import pygame

from time import sleep
from obstacle import Obstacle
from bullet import Bullet


def check_keydown_events(event, game_set, screen, p1, p2, bullets1, bullets2):
    """Respond to keypresses"""
    # adding extra False's so the tank would only move in 4 directions even if more then one kay is pressed (up + right)
    if event.key == pygame.K_w:
        p1.moving_up = True
        p1.w = True
        p1.moving_right = False
        p1.moving_left = False
    elif event.key == pygame.K_d:
        p1.moving_right = True
        p1.d = True
        p1.moving_up = False
        p1.moving_down = False
    elif event.key == pygame.K_s:
        p1.moving_down = True
        p1.s = True
        p1.moving_right = False
        p1.moving_left = False
    elif event.key == pygame.K_a:
        p1.moving_left = True
        p1.a = True
        p1.moving_up = False
        p1.moving_down = False
    elif event.key == pygame.K_UP:
        p2.moving_up = True
        p2.w = True
        p2.moving_right = False
        p2.moving_left = False
    elif event.key == pygame.K_RIGHT:
        p2.moving_right = True
        p2.d = True
        p2.moving_up = False
        p2.moving_down = False
    elif event.key == pygame.K_DOWN:
        p2.moving_down = True
        p2.s = True
        p2.moving_right = False
        p2.moving_left = False
    elif event.key == pygame.K_LEFT:
        p2.moving_left = True
        p2.a = True
        p2.moving_up = False
        p2.moving_down = False
    elif event.key == pygame.K_j:
        fire_bullet1(game_set, screen, p1, bullets1)
    elif event.key == pygame.K_RSHIFT:
        fire_bullet2(game_set, screen, p2, bullets2)
    elif event.key == pygame.K_ESCAPE:
        sys.exit()


def check_keyup_events(event, p1, p2):
    """Respond to key release, continuously checking if previously pressed buttons before the one that's being checked
    have been released or on, if not - continue the movement in that direction"""
    if event.key == pygame.K_w:
        p1.moving_up = False
        p1.w = False
        if p1.d:
            p1.moving_right = True
        elif p1.a:
            p1.moving_left = True
    elif event.key == pygame.K_d:
        p1.moving_right = False
        p1.d = False
        if p1.w:
            p1.moving_up = True
        elif p1.s:
            p1.moving_down = True
    elif event.key == pygame.K_s:
        p1.moving_down = False
        p1.s = False
        if p1.d:
            p1.moving_right = True
        elif p1.a:
            p1.moving_left = True
    elif event.key == pygame.K_a:
        p1.moving_left = False
        p1.a = False
        if p1.w:
            p1.moving_up = True
        elif p1.s:
            p1.moving_down = True
    elif event.key == pygame.K_UP:
        p2.moving_up = False
        p2.w = False
        if p2.d:
            p2.moving_right = True
        elif p2.a:
            p2.moving_left = True
    elif event.key == pygame.K_RIGHT:
        p2.moving_right = False
        p2.d = False
        if p2.w:
            p2.moving_up = True
        elif p2.s:
            p2.moving_down = True
    elif event.key == pygame.K_DOWN:
        p2.moving_down = False
        p2.s = False
        if p2.d:
            p2.moving_right = True
        elif p2.a:
            p2.moving_left = True
    elif event.key == pygame.K_LEFT:
        p2.moving_left = False
        p2.a = False
        if p2.w:
            p2.moving_up = True
        elif p2.s:
            p2.moving_down = True        


def check_events(game_set, screen, p1, p2, bullets1, bullets2, play_button, score):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, game_set, screen, p1, p2, bullets1, bullets2)
            
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, p1, p2)
            
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(game_set, screen, p1, p2, bullets1, bullets2, play_button, mouse_x, mouse_y, score)


def check_play_button(game_set, screen, p1, p2, bullets1, bullets2, play_button, mouse_x, mouse_y, score):
    """Start a new game when the player clicks Play."""
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not game_set.game_active:
        game_set.confirm.play()  # pressed button sound effect
        # Hide the mouse cursor
        pygame.mouse.set_visible(False)
        # Run the game and reset player stats
        game_set.game_active = True
        game_set.p1_lives = 3
        game_set.p2_lives = 3
        reset_stage(game_set, screen, p1, p2, bullets1, bullets2)
        score.prep_players()
        score.prep_lives()
        pygame.mixer.music.load('sound/combat.ogg')
        pygame.mixer.music.play(-1)
    

def create_obstacles(screen, obstacles):
    # Create obstacles
    ob1 = Obstacle(screen, 'horizontal', 393, 140)
    obstacles.add(ob1)
    ob2 = Obstacle(screen, 'horizontal', 393, 616)
    obstacles.add(ob2)
    ob3 = Obstacle(screen, 'vertical', 240, 293)
    obstacles.add(ob3)
    ob4 = Obstacle(screen, 'vertical', 716, 293)
    obstacles.add(ob4)


def player_obs_col(game_set, screen, p1, p2, obstacles, bullets1, bullets2, score):
    """Check if tanks smash in the obstacles"""
    if pygame.sprite.spritecollideany(p1, obstacles):
        game_set.explosion.play()
        p1_hit(game_set, score)
        reset_stage(game_set, screen, p1, p2, bullets1, bullets2)
    elif pygame.sprite.spritecollideany(p2, obstacles):
        game_set.explosion.play()
        p2_hit(game_set, score)
        reset_stage(game_set, screen, p1, p2, bullets1, bullets2)
    
        
def reset_stage(game_set, screen, p1, p2, bullets1, bullets2):
    """Show winning screen if any player have no lives left, else just reset"""
    if game_set.p1_lives == 0:
        victory_screen('images/bg_dirt_p2win.bmp', screen, game_set)

    elif game_set.p2_lives == 0:
        victory_screen('images/bg_dirt_p1win.bmp', screen, game_set)

    else:
        sleep(1)
        p1.starting_loc()
        p2.starting_loc()
        bullets1.empty()
        bullets2.empty()
        game_set.last_bullet_fired1 = (game_set.bullet_cooldown - 2)
        game_set.last_bullet_fired2 = (game_set.bullet_cooldown - 2)


def victory_screen(image, screen, game_set):
    """Displays victory screen (once one player looses all lives) and resets back to title screen after 4 sec"""
    sleep(1)
    screen.fill(game_set.bg_color)
    bg_image = pygame.image.load(image).convert()  # convert() optimises the image handling, runs game smoother
    screen.blit(bg_image, [0, 0])
    pygame.display.flip()
    pygame.mouse.set_visible(True)
    pygame.mixer.music.load('sound/victory.ogg')
    pygame.mixer.music.play()
    sleep(4)
    game_set.game_active = False
    pygame.mixer.music.load('sound/intro.ogg')
    pygame.mixer.music.play(-1)


def update_screen(game_set, screen, p1, p2, obstacles, bullets1, bullets2, play_button, score):
    """Update images on the screen and flip to the new screen"""
    # Redraw the screen during each pass through the loop
    if game_set.game_active:
        bg_image = pygame.image.load('images/bg_dirt.bmp').convert()
        screen.blit(bg_image, [0, 0])  # [x, y] coordinates for top left corner
        for ob in obstacles.sprites():
            ob.blitme()  # drawing obstacles on the ground
        bullets1.draw(screen)
        bullets2.draw(screen)
        p1.blitme()
        p2.blitme()
        # Draw the score information
        score.show_score()
    else:
        # Title screen if the game is inactive
        screen.fill(game_set.bg_color)
        bg_image = pygame.image.load('images/title_screen.bmp').convert()
        screen.blit(bg_image, [100, 50])
        play_button.draw_button()
    
    # Make the most recently drawn screen visible
    pygame.display.flip()


"""Bullets"""


def fire_bullet1(game_set, screen, player, bullets):
    # checking if bullets can be fired before doing so
    if game_set.last_bullet_fired1 >= game_set.bullet_cooldown:
        game_set.p1_fire.play()
        new_bullet = Bullet(game_set, screen, player)
        bullets.add(new_bullet)
        game_set.last_bullet_fired1 = 0


def fire_bullet2(game_set, screen, player, bullets):
    # checking if bullets can be fired before doing so
    if game_set.last_bullet_fired2 >= game_set.bullet_cooldown:
        game_set.p2_fire.play()
        new_bullet = Bullet(game_set, screen, player)
        bullets.add(new_bullet)
        game_set.last_bullet_fired2 = 0


def update_bullets(game_set, screen, p1, p2, obstacles, bullets1, bullets2, score):
    # bullet fire cooldown triggers
    game_set.last_bullet_fired1 += 1
    game_set.last_bullet_fired2 += 1
    bullets1.update()
    bullets2.update()
    # erasing bullets that hit the wall or went out of screen
    del_bullets(bullets1, obstacles)
    del_bullets(bullets2, obstacles)
    # checking if player hit opposing player with bullets
    if pygame.sprite.spritecollideany(p2, bullets1):  # p1 hit p2
        game_set.explosion.play()
        p2_hit(game_set, score)
        reset_stage(game_set, screen, p1, p2, bullets1, bullets2)
    if pygame.sprite.spritecollideany(p1, bullets2):
        game_set.explosion.play()
        p1_hit(game_set, score)
        reset_stage(game_set, screen, p1, p2, bullets1, bullets2)
    # check collision between bullets and tank collision with walls
    pygame.sprite.groupcollide(bullets1, bullets2, True, True)  # remove bullets that collided with each other
    player_obs_col(game_set, screen, p1, p2, obstacles, bullets1, bullets2, score)
    

def del_bullets(bullets, obstacles):
    # Get rid of bullets that have disappeared
    for bullet in bullets.copy():
        if bullet.x < -10 or bullet.x > 1010 or bullet.y < -10 or bullet.y > 810:
            bullets.remove(bullet)
    # Get rid of bullets that have hit the walls
    for bullet in bullets.copy():
        if pygame.sprite.spritecollideany(bullet, obstacles):
            bullets.remove(bullet)


def p1_hit(game_set, score):
    game_set.p1_lives -= 1
    score.prep_lives()


def p2_hit(game_set, score):
    game_set.p2_lives -= 1
    score.prep_lives()
