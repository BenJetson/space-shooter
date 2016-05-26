# Import pygame
import pygame

pygame.init()  # Initializing here before loading other modules that depend on it.

# More imports
import os
import random
from assets import *
from sprites import Fairy, Goblin, Ground, SpaceShip
from scenery import Mountains

# Stages
START = 0
PLAYING = 1
PAUSED = 2
DELAY = 3
GAME_OVER = 4
HELP = 5

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
score = 0

# Settings
sound_on = False

# Data settings
score_file = "data/high_score.txt"
default_high_score = 100

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
def show_texts_centered(surface, array, yval_start=HEIGHT / 2 - 100, spacing=25):
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

    with open(score_file, 'w') as f:
        f.write(str(score))


def start():
    global fairy, goblin_speed, bomb_rate, shot_limit, score, level, stage, shots, hits

    fairy = Fairy(480, 540)
    goblin_speed = initial_alien_speed
    bomb_rate = initial_bomb_rate
    shot_limit = initial_shot_limit

    score = 0
    shots = 0
    hits = 0
    level = 1
    stage = START


def setup():
    global goblins, bombs, bullets, stage, ticks, level_ufos

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

    level_ufos = [SpaceShip()]

    bombs = []
    bullets = []

    ticks = delay_ticks
    stage = DELAY
    if sound_on:
        THEME.play(loops=-1)


def advance():
    global level, goblin_speed, bomb_rate

    level += 1
    goblin_speed += 0.5
    bomb_rate += 1

    setup()


def end_game():
    global stage

    if sound_on:
        THEME.stop()

    stage = GAME_OVER


def draw_centered_mute():
    if not sound_on:
        screen.blit(mute_img, [screen.get_rect().centerx - (mute_img.get_width() / 2), 15])


def display_start_screen(screen, high_score):
    show_texts_centered(screen, start_texts)
    if not sound_on:
        screen.blit(mute_img, [WIDTH - mute_img.get_width() - 25, HEIGHT - mute_img.get_height() - 25])


def display_pause_screen(screen):
    show_texts_centered(screen, pause_texts)


def display_end_screen(screen, shots, hits):
    new_end_texts = end_texts

    shots_render = FONT_MD.render(("Shots: " + str(shots)), True, RED)
    hits_render = FONT_MD.render(("Hits: " + str(hits)), True, RED)

    screen.blit(shots_render, [40, HEIGHT - 20 - shots_render.get_height()])
    screen.blit(hits_render, [WIDTH - 40 - hits_render.get_width(), HEIGHT - 20 - hits_render.get_height()])

    show_texts_centered(screen, new_end_texts)


def display_help_screen(screen):
    show_texts_centered(screen, help_texts, yval_start=50, spacing=0)
    draw_centered_mute()


def display_stats(screen, score, level, high_score, shield):
    score_text = FONT_SM.render("SCORE: " + str(score), True, ORANGE)
    level_text = FONT_SM.render("LEVEL:" + str(level), True, ORANGE)
    high_score_text = FONT_SM.render("HIGH SCORE: " + str(high_score), True, ORANGE)
    shield_text = FONT_XS.render("SHIELD:", True, ORANGE)
    shield_bar = pygame.draw.rect(screen, ORANGE, [WIDTH - 15 - shield, 15 + shield_text.get_height(), shield, 15])

    screen.blit(level_text, [15, 15])
    screen.blit(shield_text, [WIDTH - 15 - shield_text.get_width(), 15])
    show_texts_centered(screen, [score_text, high_score_text], 15, 0)


def toggle_sound():
    global sound_on

    if sound_on:
        THEME.stop()
        sound_on = False
    elif not sound_on:
        THEME.play(loops=-1)
        sound_on = True


# Make scenery objects
ground = Ground(0, 560, 1000, 100)
mountains = Mountains(0, 480, 1000, 80, 9)

# Get high score
high_score = read_high_score()
start_texts.append(FONT_SM.render("HIGH SCORE: " + str(high_score), True, YELLOW))

# Controller Optimization

ctrl_a = 0
ctrl_a_prevstate = 0
ctrl_x = 0
ctrl_x_prevstate = 0


def controller_button_fixer():
    global ctrl_a_prevstate, ctrl_a, ctrl_x_prevstate, ctrl_x

    ctrl_a_currstate = controller.a()

    if ctrl_a_currstate != ctrl_a_prevstate:
        ctrl_a_prevstate = ctrl_a_currstate
        ctrl_a = ctrl_a_currstate

    ctrl_x_currstate = controller.x()

    if ctrl_x_currstate != ctrl_x_prevstate:
        ctrl_x_prevstate = ctrl_x_currstate
        ctrl_x = ctrl_x_currstate


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

                if event.key == pygame.K_h:
                    stage = HELP

            elif stage == HELP:
                if event.key == pygame.K_SPACE:
                    stage = START

            elif stage == PLAYING:
                if event.key == pygame.K_SPACE and len(bullets) < shot_limit:
                    if sound_on:
                        SHOT.play()
                    fairy.shoot(bullets, -bullet_speed)
                    score -= 1
                    shots += 1

                elif event.key == pygame.K_p:
                    stage = PAUSED

            elif stage == PAUSED:
                if event.key == pygame.K_p:
                    stage = PLAYING

            elif stage == GAME_OVER:
                if event.key == pygame.K_r:
                    start()

            if event.key == pygame.K_s:
                toggle_sound()

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

        if ctrl_x == 1:
            toggle_sound()
            ctrl_x = 0

        if stage == START:
            if controller.start() == 1:
                setup()

            if controller.y() == 1:
                stage = HELP

        elif stage == HELP:
            if controller.back() == 1:
                stage = START

        elif stage == PLAYING:
            if ctrl_a == 1 and len(bullets) < shot_limit:
                if sound_on:
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

        for u in level_ufos:
            u.update()

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
                    hits += 1
                    if sound_on:
                        HIT.play()

            for u in level_ufos:
                if b.intersects(u):
                    u.kill()
                    score += u.value

            if b.y + b.h < 0:
                b.kill()

        # check game status
        if not fairy.alive:
            end_game()
        elif len(goblins) == 0:
            advance()

        if score > high_score:
            high_score = score
            save_high_score(score)

    # Drawing code
    screen.fill(SKY_BLUE)

    if stage == START:
        screen.blit(start_img, [0, 0])
        display_start_screen(screen, high_score)

    if stage == HELP:
        display_help_screen(screen)

    elif stage in [PLAYING, PAUSED, DELAY, GAME_OVER]:
        mountains.draw(screen)
        ground.draw(screen)
        pygame.draw.ellipse(screen, SUN, [800, 50, 100, 100])
        fairy.draw(screen)

        if not sound_on:
            screen.blit(mute_img, [screen.get_rect().centerx - (mute_img.get_width() / 2) + 200, 15])

        for g in goblins:
            g.draw(screen)

        for b in bullets:
            b.draw(screen)

        for u in level_ufos:
            u.draw(screen)

        for b in bombs:
            b.draw(screen)

        if stage == PAUSED:
            display_pause_screen(screen)
        if stage == GAME_OVER:
            display_end_screen(screen, shots, hits)

        display_stats(screen, score, level, high_score, fairy.shield)

    # Update screen
    pygame.display.flip()
    clock.tick(refresh_rate)

    # Remove killed objects
    if stage not in [START, HELP]:
        goblins = [g for g in goblins if g.alive]
        bullets = [b for b in bullets if b.alive]
        bombs = [b for b in bombs if b.alive]
        level_ufos = [u for u in level_ufos if u.alive]

# Close window on quit
pygame.quit()
