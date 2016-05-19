import pygame

# Colors
BLACK = (0, 0, 0)
GREY = (125, 125, 125)
LIGHT_GREY = (200, 200, 200)
WHITE = (255, 255, 255)


# Fonts
FONT_SM = pygame.font.Font("fonts/joystix monospace.ttf", 32)
FONT_MD = pygame.font.Font("fonts/joystix monospace.ttf", 48)
FONT_LG = pygame.font.Font("fonts/joystix monospace.ttf", 64)
FONT_XL = pygame.font.Font("fonts/joystix monospace.ttf", 80)


# Images
cannon_img = pygame.image.load("img/ship.png")
alien_img = pygame.image.load("img/bug.png")
bullet_img = pygame.image.load("img/bullet.png")
bomb_img = pygame.image.load("img/bomb.png")


# Sounds
SHOT = pygame.mixer.Sound("sounds/shot.ogg")
HIT = pygame.mixer.Sound("sounds/hit.ogg")
CLANK = pygame.mixer.Sound("sounds/clank.ogg")
THEME = pygame.mixer.Sound("sounds/take_a_chance.ogg")


