import pygame
from xbox360_controller import XBox360Controller

# Controller Config Stuff
try:
    controller = XBox360Controller(0)
    controllerConnected = True
except:
    controllerConnected = False

TITLE = "Protect the Prince"

# Colors
BLACK = (0, 0, 0)
GREY = (125, 125, 125)
LIGHT_GREY = (200, 200, 200)
WHITE = (255, 255, 255)
YELLOW = (246, 255, 0)
ORANGE = (204, 102, 0)
RED = (255, 0, 0)
GREEN = (144, 219, 24)
MOUNTAIN_BLUE = (109, 148, 176)
SKY_BLUE = (19, 216, 242)
SUN = (244, 252, 0)

# Fonts
FONT_XS = pygame.font.Font("fonts/boogaloo.ttf", 18)
FONT_SM = pygame.font.Font("fonts/boogaloo.ttf", 32)
FONT_MD = pygame.font.Font("fonts/boogaloo.ttf", 48)
FONT_LG = pygame.font.Font("fonts/boogaloo.ttf", 64)
FONT_XL = pygame.font.Font("fonts/boogaloo.ttf", 96)


# Images
cannon_img = pygame.image.load("img/ship.png")
alien_img = pygame.image.load("img/bug.png")
bullet_img = [pygame.image.load("img/bullet.png"),
              pygame.image.load("img/bullet1.png"),
              pygame.image.load("img/bullet2.png")]
bomb_img = pygame.image.load("img/bomb.png")
fairy_img = pygame.image.load("img/fairy.png")
prince_img = pygame.image.load("img/Prince.png")
goblin_img = [pygame.image.load("img/goblin1.png"),
                pygame.image.load("img/goblin2.png"),
                pygame.image.load("img/goblin3.png"),
                pygame.image.load("img/goblin4.png"),
                pygame.image.load("img/goblin5.png"),
                pygame.image.load("img/goblin6.png")]

mute_img = pygame.image.load("img/mute.png")
ufo_img = pygame.image.load("img/ufo.png")
start_img = pygame.image.load("img/start-bgd.png")

# Sounds
SHOT = pygame.mixer.Sound("sounds/shot.ogg")
HIT = pygame.mixer.Sound("sounds/hit.ogg")
THEME = pygame.mixer.Sound("sounds/take_a_chance.ogg")

# Texts

if controllerConnected:
    control_text = {
        "start game": "START",
        "pause game": "BACK",
        "directional": "left analog stick",
        "resume game": "START",
        "restart game": "START",
        "fire": "A",
        "sound toggle": "X",
        "get help": "Y",
        "dismiss help": "BACK"
    }
else:
    control_text = {
        "start game": "SPACE",
        "pause game": "'p'",
        "directional": "arrow keyk",
        "restart game": "'r'",
        "resume game": "SPACE",
        "fire": "SPACE",
        "sound toggle": "'s'",
        "get help": "'h'",
        "dismiss help": "SPACE"
    }

help_texts = [FONT_XL.render("HELP", True, ORANGE),
              FONT_XS.render(("You can move the fairy left and right on the screen using the " +
                              control_text["directional"] + "."), True, ORANGE),
              FONT_XS.render("", True, ORANGE),
              FONT_XS.render("", True, ORANGE),
              FONT_XS.render(("The goal of the game is to shoot as many goblins as you can without " +
                              "dying. To shoot goblins, press "+ control_text["fire"] + "."), True, ORANGE),
              FONT_XS.render(("For each shot you make, you will lose one point. You can only " +
                              "have five bullets on-screen at any time."), True, ORANGE),
              FONT_XS.render("", True, ORANGE),
              FONT_XS.render(("Sounds can be toggled on or off by pressing " + control_text['sound toggle'] + ". " +
                              "While sounds are disabled, a mute icon will be displayed."), True, ORANGE),
              FONT_XS.render("", True, ORANGE),
              FONT_XS.render(("To pause the game, press " + control_text["pause game"] + ". You " +
                              "can resume the game by pressing " + control_text["resume game"] + "."), True, ORANGE),
              FONT_XS.render("", True, ORANGE),
              FONT_XS.render(("You also need to watch out, as the goblins will be throwing bombs " +
                              "at you from above. However, your shield will"), True, ORANGE),
              FONT_XS.render(("protect you from their bombs for a certain number of hits. " +
                              "Keep an eye on the shield bar in the top-right."), True, ORANGE),
              FONT_XS.render("", True, ORANGE),
              FONT_XS.render(("As the levels progress, the speed of the goblins will increase. " +
                              "If the goblins hit the bottom of the"), True, ORANGE),
              FONT_XS.render(("screen, the game is over. Be sure to hit them all" +
                              "quickly before they move too close!"), True, ORANGE),
              FONT_XS.render("", True, ORANGE),
              FONT_SM.render("Press " + control_text["dismiss help"] + " to dismiss this screen.", True, ORANGE)]

pause_texts = [FONT_MD.render("GAME PAUSED", True, ORANGE),
               FONT_SM.render(("Press " + control_text['resume game'] + " to resume."), True, ORANGE)]

start_texts = [FONT_MD.render(TITLE, True, YELLOW),
               FONT_SM.render(("Press " + control_text["start game"] + " to start."), True, YELLOW),
               FONT_XS.render(("Press " + control_text["get help"] + " to get help."), True, YELLOW)]

end_texts = [FONT_XL.render("GAME OVER!", True, RED),
             FONT_MD.render(("Press " + control_text["restart game"] + " to restart"), True, RED)]
