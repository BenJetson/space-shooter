# Imports
import pygame
pygame.init()

import os
import random
from assets import *
from sprites import Cannon, Alien
from scenery import Ground, Mountains, Stars

# Initialize game engine
pygame.init()

# Set window position
os.environ['SDL_VIDEO_WINDOW_POS'] = "15, 30:"

# Window settings
WIDTH = 1000
HEIGHT = 660
TITLE = "Name of Game"

# Make window
screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption(TITLE)

# Timer
clock = pygame.time.Clock()
refresh_rate = 60

# Data
score_file = "data/high_score.txt"

# Stages
START = 0
PLAYING = 1
PAUSED = 2
DELAY = 3
GAME_OVER = 4

delay_ticks = 45

# Settings
cannon_speed = 4
bullet_speed = 6
bomb_speed = 3
drop_amount = 12

initial_shot_limit = 5
initial_alien_speed = 2
initial_bomb_rate = 5

sound_on = True
default_high_score = 2000

# Make scenery objects
ground = Ground(0, 560, 1000, 5)
mountains = Mountains(0, 480, 1000, 80, 9)
stars = Stars(0, 0, 1000, 560, 125)

def get_high_score():
    if os.path.exists(score_file):
        with open(score_file, 'r') as f:
            return max([int(f.read().strip()), default_high_score])
    else:
        return default_high_score

def update_high_score():
    if not os.path.exists('data'):
        os.mkdir('data')

    with open((score_file), 'w') as f:
        f.write(str(high_score))

def reset():
    global  cannon, alien_speed, bomb_rate, shot_limit, score, level, stage

    cannon = Cannon(480, 540)
    alien_speed = initial_alien_speed
    bomb_rate = initial_bomb_rate
    shot_limit = initial_shot_limit

    score = 0
    level = 1
    stage = START

    setup()

def setup():
    global aliens, bombs, bullets, stage, delay_ticks, high_score

    a1 = Alien(400, 90, alien_speed)
    a2 = Alien(500, 90, alien_speed)
    a3 = Alien(600, 90, alien_speed)
    aliens = [a1, a2, a3]
    
    bombs = []
    bullets = []

    delay_ticks = 45
    stage = DELAY

    high_score = get_high_score()

def advance():
    global level, alien_speed, bomb_rate

    level += 1
    alien_speed += 0.5
    bomb_rate += 1

    setup()

def end_game():
    global stage

    stage = GAME_OVER

def display_start_screen():
    pass

def display_pause_screen():
    pass

def display_end_screen():
    pass

def display_stats(score, level, high_score, power):
    pass


# hide mouse cursor over screen
pygame.mouse.set_visible(0)


# Game loop
done = False
reset()

while not done:
    # Event processing
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        
        elif event.type == pygame.KEYDOWN:
            if stage == START:
                if event.key == pygame.K_SPACE:
                    stage = DELAY

            elif stage == PLAYING:
                if event.key == pygame.K_SPACE and len(bullets) < shot_limit:
                    cannon.shoot(bullets, -bullet_speed)
                    score -= 1

                elif event.key == pygame.K_p:
                    stage = PAUSED

            elif stage == PAUSED:
                if event.key == pygame.K_p:
                    stage = PLAYING

            elif stage == GAME_OVER:
                if event.key == pygame.K_r:
                    reset()

    if stage == PLAYING:
        key = pygame.key.get_pressed()

        if key[pygame.K_RIGHT]:
            cannon.move(cannon_speed)
        elif key[pygame.K_LEFT]:
            cannon.move(-cannon_speed)


    # Game logic
    if stage == DELAY:
        if delay_ticks > 0:
            delay_ticks -= 1
        else:
            stage = PLAYING

    if stage == PLAYING:
        # process cannon
        cannon.update()

        # process enemies
        fleet_hits_edge = False

        for a in aliens:
            a.update()

            r = random.randint(0, 1000)
            if r < bomb_rate:
                a.drop_bomb(bombs, bomb_speed)

            if a.x <= 0 or a.x + a.w >= WIDTH:
                fleet_hits_edge = True

        if fleet_hits_edge:
            for a in aliens:
                a.reverse_and_drop(drop_amount)

        # process bombs
        for b in bombs:
            b.update(ground)

            if b.intersects(cannon):
                b.kill()
                cannon.apply_damage(20)

        # process bullets
        for b in bullets:
            b.update()

            for a in aliens:
                if b.intersects(a):
                    b.kill()
                    a.kill()


        # update score
        for a in aliens:
            if not a.alive:
                score += a.value

        # check game status
        if cannon.alive == False:
            end_game()
        elif len(aliens) == 0:
            advance()


    # Drawing code
    screen.fill(BLACK)

    if stage == START:
        display_start_screen()

    elif stage in [PLAYING, PAUSED, DELAY, GAME_OVER]:
        stars.draw(screen)
        mountains.draw(screen)
        ground.draw(screen)

        cannon.draw(screen)

        for a in aliens:
            a.draw(screen)

        for b in bullets:
            b.draw(screen)

        for b in bombs:
            b.draw(screen)

    if stage == PAUSED:
        display_pause_screen()
    if stage == GAME_OVER:
        display_end_screen()

    display_stats(score, level, high_score, cannon.shield)


    # Update screen
    pygame.display.flip()
    clock.tick(refresh_rate)


    # Remove killed objects
    aliens = [a for a in aliens if a.alive]
    bullets = [b for b in bullets if b.alive]
    bombs = [b for b in bombs if b.alive]


# Close window on quit
pygame.quit()
