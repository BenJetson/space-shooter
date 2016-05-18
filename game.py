# Imports
import pygame
import os
from colors import *
from sprites import Cannon, Alien, Bullet, Bomb
from scenery import Ground, Mountains, Stars


# Set window position
os.environ['SDL_VIDEO_WINDOW_POS'] = "15, 30:"


# Initialize game engine
pygame.init()


# Window
SIZE = (1000, 660)
TITLE = "Name of Game"
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)

# Timer
clock = pygame.time.Clock()
refresh_rate = 60

# Sounds
SHOT = pygame.mixer.Sound("sounds/shot.ogg")
HIT = pygame.mixer.Sound("sounds/hit.ogg")
CLANK = pygame.mixer.Sound("sounds/clank.ogg")
THEME = pygame.mixer.Sound("sounds/take_a_chance.ogg")

# Fonts
FONT_SM = pygame.font.Font("fonts/joystix monospace.ttf", 30)
FONT_LG = pygame.font.Font("fonts/joystix monospace.ttf", 70)



# Data
score_file = "data/scores.txt"

# Stages
START = 0
PLAYING = 1
PAUSED = 2
CLEAR = 3
DIE = 4
GAME_OVER = 5


# Settings
shot_limit = 5
cannon_speed = 4
bullet_speed = 6
alien_speed = 2
bomb_speed = 3
extra_life_points = 1000 # then at 2000, 4000, 8000, ...
sound_on = True
default_high_score = 2000

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
    global cannon, aliens, bombs, bullets

    cannon = Cannon(480, 540)
    
    a1 = Alien(400, 90, alien_speed)
    a2 = Alien(500, 90, alien_speed)
    a3 = Alien(600, 90, alien_speed)
    aliens = [a1, a2, a3]
    
    bombs = []
    bullets = []


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
                    stage = PLAYING

            elif stage == PLAYING:
                if event.key == pygame.K_SPACE:
                    cannon.shoot(bullets)

            elif stage == DIE:
                if event.key == pygame.K_SPACE:
                    pass

            elif stage == CLEAR and bonus == 0:
                if event.key == pygame.K_SPACE:
                    pass

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
    if stage == PLAYING:
        cannon.update(aliens, bombs)

        for a in aliens:
            a.update(bullets)

        for b in bullets:
            b.update()

        for b in bombs:
            b.update()
            

    # Drawing code

    ''' draw background '''
    screen.fill(BLACK)
    stars.draw(screen)
    mountains.draw(screen)
    ground.draw(screen)

    ''' draw game objects '''
    cannon.draw(screen)

    for a in aliens:
        a.draw(screen)

    for b in bullets:
        b.draw(screen)

    for b in bombs:
        b.draw(screen)


    # Update screen
    pygame.display.flip()
    clock.tick(refresh_rate)


    # Remove hit objects
    if stage == PLAYING:
        aliens = [a for a in aliens if a.alive == True]
        bullets = [b for b in bullets if b.alive == True]
        bombs = [b for b in bombs if b.alive == True]
        

# Close window on quit
pygame.quit()
