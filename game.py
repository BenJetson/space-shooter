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
score_file = "data/scores.txt"

# Stages
START = 0
PLAYING = 1
PAUSED = 2
DELAY = 3
GAME_OVER = 4


# Settings
shot_limit = 5
cannon_speed = 4
bullet_speed = 6
alien_speed = 2
bomb_speed = 3
bomb_rate = 5
drop_amount = 10
delay_ticks = 45

extra_life_points = 1000 # then at 2000, 4000, 8000, ...
sound_on = True
default_high_score = 2000

# Make cannon
cannon = Cannon(480, 540)

# Make background objects
ground = Ground(0, 560, 1000, 5)
mountains = Mountains(0, 480, 1000, 80, 9)
stars = Stars(0, 0, 1000, 560, 125)

def start():
    global  score, lives, level, stage

    score = 0
    lives = 3
    level = 1
    stage = START

    setup()

def setup():
    global aliens, bombs, bullets, stage, delay_ticks

    a1 = Alien(400, 90, alien_speed)
    a2 = Alien(500, 90, alien_speed)
    a3 = Alien(600, 90, alien_speed)
    aliens = [a1, a2, a3]
    
    bombs = []
    bullets = []

    delay_ticks = 45
    stage = DELAY

def advance():
    global level, alien_speed, bomb_rate

    level += 1
    alien_speed += 0.5
    bomb_rate += 1

    setup()

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

def display_start_screen():
    pass

def display_stats():
    pass

def display_end_screen():
    pass

# hide mouse cursor over screen
pygame.mouse.set_visible(0)


# Game loop
done = False
high_score = get_high_score()
start()

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

                elif event.key == pygame.K_p:
                    stage = PAUSED

            elif stage == PAUSED:
                if event.key == pygame.K_p:
                    stage = PLAYING

            elif stage == GAME_OVER:
                if event.key == pygame.K_r:
                    start()

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
        cannon.update()

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

        for b in bullets:
            b.update(aliens)

        for b in bombs:
            b.update(cannon, ground)

        for a in aliens:
            if not a.alive:
                score += 10
                print(score)

    # Drawing code
    screen.fill(BLACK)

    if stage == START:
        display_start_screen()

    elif stage == PLAYING or stage == PAUSED or stage == DELAY:
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

    elif stage == GAME_OVER:
        display_end_screen()


    # Update screen
    pygame.display.flip()
    clock.tick(refresh_rate)


    # Remove killed objects
    aliens = [a for a in aliens if a.alive]
    bullets = [b for b in bullets if b.alive]
    bombs = [b for b in bombs if b.alive]

    # check cannon kill
    if cannon.alive == False:
        stage = GAME_OVER

    # check level clear
    if len(aliens) == 0:
        advance()


# Close window on quit
pygame.quit()
