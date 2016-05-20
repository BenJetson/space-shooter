import pygame

# Game Title
TITLE = "Protect the Prince"

# Colors
BLACK = (0, 0, 0)
GREY = (125, 125, 125)
LIGHT_GREY = (200, 200, 200)
WHITE = (255, 255, 255)
YELLOW = (246, 255, 0)


# Fonts
FONT_SM = pygame.font.Font("fonts/joystix monospace.ttf", 32)
FONT_MD = pygame.font.Font("fonts/joystix monospace.ttf", 48)
FONT_LG = pygame.font.Font("fonts/joystix monospace.ttf", 64)
FONT_XL = pygame.font.Font("fonts/joystix monospace.ttf", 80)

# Texts
pause_texts = [FONT_MD.render("GAME PAUSED", True, YELLOW),
               FONT_SM.render("Press 'p' to resume.", True, YELLOW)]

start_texts = [FONT_MD.render(TITLE, True, YELLOW),
               FONT_SM.render("Press SPACE to start.", True, YELLOW)]

# Images
cannon_img = pygame.image.load("img/ship.png")
alien_img = pygame.image.load("img/bug.png")
bullet_img = pygame.image.load("img/bullet.png")
bomb_img = pygame.image.load("img/bomb.png")


# Sounds
SHOT = pygame.mixer.Sound("sounds/shot.ogg")
HIT = pygame.mixer.Sound("sounds/hit.ogg")
THEME = pygame.mixer.Sound("sounds/take_a_chance.ogg")


