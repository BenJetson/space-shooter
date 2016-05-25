# Import pygame
import pygame


# Initialize game engine
pygame.init()


# More imports
import os
import random
from assets import *
from sprites import Fairy, Goblin, Ground
from scenery import Mountains


# Stages
START = 0
PLAYING = 1
PAUSED = 2
DELAY = 3
GAME_OVER = 4


# Window settings
WIDTH = 1000
HEIGHT = 660


# Play settings
cannon_speed = 4
bullet_speed = 7
bomb_speed = 5
drop_amount = 12

initial_shot_limit = 3
initial_alien_speed = 2
initial_bomb_rate = 5

sound_on = True


# Data settings
score_file = "data/high_score.txt"
default_high_score = 1000


# Make window
os.environ['SDL_VIDEO_WINDOW_POS'] = "15, 30:"
screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption(TITLE)


# Hide mouse cursor over screen
pygame.mouse.set_visible(0)


# Timer
clock = pygame.time.Clock()
refresh_rate = 60
delay_ticks = 45


# Define functions

def show_texts_centered(surface, array, yval_start=HEIGHT/2-100, spacing=25):
    y_val = yval_start

    for line in array:
        surface.blit(line, [screen.get_rect().centerx - int(line.get_width() / 2), y_val])
        y_val += line.get_height() + spacing

def read_high_score():
    if os.path.exists(score_file):
        with open(score_file, 'r') as f:
            return max([int(f.read().strip()), default_high_score])
    else:
        return default_high_score

def save_high_score(score):
    if not os.path.exists('data'):
        os.mkdir('data')

    with open((score_file), 'w') as f:
        f.write(str(score))

def start():
    global fairy, goblin_speed, bomb_rate, shot_limit, score, level, stage

    fairy = Fairy(480, 540)
    goblin_speed = initial_alien_speed
    bomb_rate = initial_bomb_rate
    shot_limit = initial_shot_limit

    score = 0
    level = 1
    stage = START

def setup():
    global goblins, bombs, bullets, stage, ticks

    goblins = [Goblin(400, 90, goblin_speed),
               Goblin(500, 90, goblin_speed),
               Goblin(600, 90, goblin_speed),
               Goblin(450, 140, goblin_speed),
               Goblin(550, 140, goblin_speed),
               Goblin(400, 190, goblin_speed),
               Goblin(300, 190, goblin_speed),
               Goblin(500, 190, goblin_speed),
               Goblin(600, 190, goblin_speed),
               Goblin(700, 190, goblin_speed)]

    bombs = []
    bullets = []

    ticks = delay_ticks
    stage = DELAY

def advance():
    global level, goblin_speed, bomb_rate

    level += 1
    goblin_speed += 0.5
    bomb_rate += 1

    setup()

def end_game():
    global stage

    stage = GAME_OVER


def display_start_screen(screen, high_score):

    show_texts_centered(screen, start_texts)

def display_pause_screen(screen):

    show_texts_centered(screen, pause_texts)

def display_end_screen(screen):
    show_texts_centered(screen, end_texts)

def display_stats(screen, score, level, high_score, shield):
    score_text = FONT_SM.render("SCORE: " + str(score), True, YELLOW)
    level_text = FONT_SM.render("LEVEL:" + str(level), True, YELLOW)
    high_score_text = FONT_SM.render("HIGH SCORE: " + str(high_score), True, YELLOW)
    shield_text = FONT_SM.render("SHIELD: " + str(shield), True, YELLOW)

    screen.blit(level_text, [15,15])
    screen.blit(shield_text, [WIDTH-15-shield_text.get_width(), 15])
    show_texts_centered(screen, [score_text, high_score_text], 15, 0)



# Make scenery objects
ground = Ground(0,560, 1000, 100)
mountains = Mountains(0, 480, 1000, 80, 9)

# Get high score
high_score = read_high_score()
start_texts.append(FONT_SM.render("HIGH SCORE: " + str(high_score), True, YELLOW))

# Game loop
done = False
start()


while not done:
    # Event processing
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        elif event.type == pygame.KEYDOWN:
            if stage == START:
                if event.key == pygame.K_SPACE:
                    setup()

            elif stage == PLAYING:
                if event.key == pygame.K_SPACE and len(bullets) < shot_limit:
                    SHOT.play()
                    fairy.shoot(bullets, -bullet_speed)
                    score -= 1

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
            fairy.vx = cannon_speed
        elif key[pygame.K_LEFT]:
            fairy.vx = -cannon_speed
        else:
            fairy.vx = 0

    # Controller Handling

    if controllerConnected:
        controller_button_fixer()

        if stage == START:
            if controller.start() == 1:
                setup()

        elif stage == PLAYING:
            if ctrl_a == 1 and len(bullets) < shot_limit:
                SHOT.play()
                fairy.shoot(bullets, -bullet_speed)
                score -= 1
                ctrl_a = 0

            elif controller.back() == 1:
                stage = PAUSED

        elif stage == PAUSED:
            if controller.start() == 1:
                stage = PLAYING

        elif stage == GAME_OVER:
            if controller.start() == 1:
                start()

        if controller.left_stick_axes()[0] > 0:
            fairy.vx = cannon_speed
        elif controller.left_stick_axes()[0] < 0:
            fairy.vx = -cannon_speed
        else:
            fairy.vx = 0

    # Game logic
    if stage == DELAY:
        if ticks > 0:
            ticks -= 1
        else:
            stage = PLAYING

    if stage == PLAYING:
        # process scenery

        # process cannon
        fairy.update()

        # process enemies
        fleet_hits_edge = False

        for g in goblins:
            g.update()

            r = random.randint(0, 1000)
            if r < bomb_rate:
                g.drop_bomb(bombs, bomb_speed)

            if g.x <= 0 or g.x + g.w >= WIDTH:
                fleet_hits_edge = True

        if fleet_hits_edge:
            for g in goblins:
                g.reverse_and_drop(drop_amount)

        # process bombs
        for b in bombs:
            b.update()

            if b.intersects(fairy):
                b.kill()
                fairy.apply_damage(20)
            elif b.intersects(ground):
                b.kill()

        # process bullets
        for b in bullets:
            b.update()

            for g in goblins:
                if b.intersects(g):
                    b.kill()
                    g.kill()
                    score += g.value

            if b.y + b.h < 0:
                b.kill()

        # check game status
        if fairy.alive == False:
            end_game()
        elif len(goblins) == 0:
            advance()


    # Drawing code
    screen.fill(SKY_BLUE)

    if stage == START:
        display_start_screen(screen, high_score)

    elif stage in [PLAYING, PAUSED, DELAY, GAME_OVER]:
        mountains.draw(screen)
        ground.draw(screen)
        pygame.draw.ellipse(screen, SUN, [800, 50, 100, 100])
        fairy.draw(screen)

        for g in goblins:
            g.draw(screen)

        for b in bullets:
            b.draw(screen)

        for b in bombs:
            b.draw(screen)

        if stage == PAUSED:
            display_pause_screen(screen)
        if stage == GAME_OVER:
            display_end_screen(screen)

        display_stats(screen, score, level, high_score, fairy.shield)


    # Update screen
    pygame.display.flip()
    clock.tick(refresh_rate)


    # Remove killed objects
    if stage != START:
        goblins = [g for g in goblins if g.alive]
        bullets = [b for b in bullets if b.alive]
        bombs = [b for b in bombs if b.alive]


# Close window on quit
pygame.quit()
