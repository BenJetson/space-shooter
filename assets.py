import pygame

TITLE = "Protect the Prince"

# Colors
BLACK = (0, 0, 0)
GREY = (125, 125, 125)
LIGHT_GREY = (200, 200, 200)
WHITE = (255, 255, 255)
YELLOW = (246, 255, 0)
RED = (255, 0, 0)


# Fonts
FONT_SM = pygame.font.Font("fonts/chary.ttf", 32)
FONT_MD = pygame.font.Font("fonts/chary.ttf", 48)
FONT_LG = pygame.font.Font("fonts/chary.ttf", 64)
FONT_XL = pygame.font.Font("fonts/chary.ttf", 96)


# Images
cannon_img = pygame.image.load("img/ship.png")
alien_img = pygame.image.load("img/bug.png")
bullet_img = pygame.image.load("img/bullet.png")
bomb_img = pygame.image.load("img/bomb.png")
fairy_img = pygame.image.load("img/fairy.png")
goblin1_img = pygame.image.load("img/goblin1.png")
goblin2_img = pygame.image.load("img/goblin2.png")
goblin3_img = pygame.image.load("img/goblin3.png")
goblin4_img = pygame.image.load("img/goblin4.png")
goblin5_img = pygame.image.load("img/goblin5.png")
goblin6_img = pygame.image.load("img/goblin6.png")

# Sounds
SHOT = pygame.mixer.Sound("sounds/shot.ogg")
HIT = pygame.mixer.Sound("sounds/hit.ogg")
THEME = pygame.mixer.Sound("sounds/take_a_chance.ogg")


# Texts
pause_texts = [FONT_MD.render("GAME PAUSED", True, YELLOW),
               FONT_SM.render("Press 'p' to resume.", True, YELLOW)]

start_texts = [FONT_MD.render(TITLE, True, YELLOW),
               FONT_SM.render("Press SPACE to start.", True, YELLOW)]

end_texts = [FONT_XL.render("GAME OVER!", True, RED),
             FONT_MD.render("Press 'r' to restart", True, RED)]