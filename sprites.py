from assets import *
import random

class SimpleSprite:
    '''
    Pygame has its own Sprite class, but we'll use a simplified
    version here to get a feel for how the class works.
    '''
    
    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.img = img
        self.w = img.get_width()
        self.h = img.get_height()

        self.vx = 0
        self.vy = 0

        self.alive = True

    def move(self):
        self.x += self.vx
        self.y += self.vy

    def kill(self):
        self.alive = False

    def get_rect(self):
        return [self.x, self.y, self.w, self.h]

    def intersects(self, other):
        rect1 = self.get_rect()
        rect2 = other.get_rect()

        return not (rect1[0] +  rect1[2] <= rect2[0] or
                    rect1[0] >= rect2[0] +  rect2[2] or
                    rect1[1] +  rect1[3] <= rect2[1] or
                    rect1[1] >= rect2[1] +  rect2[3])

    def draw(self, screen):
        screen.blit(self.img, [self.x, self.y])

    def update(self):
        pass


class Ground(SimpleSprite):
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def draw(self, screen):
        pygame.draw.rect(screen, GREY, [self.x, self.y, self.w, self.h])


class Fairy(SimpleSprite):

    def __init__(self, x, y):
        super().__init__(x, y, fairy_img)
        
        self.alive = True
        self.shield = 100

    def shoot(self, bullets, vy):
        x = self.x + self.w / 2 - bullet_img.get_width() / 2
        y = self.y

        b = Bullet(x, y, vy)
        bullets.append(b)

    def apply_damage(self, amount):
        self.shield -= amount

    def check_screen_edges(self):
        if self.x < 0:
            self.x = 0
        elif self.x + self.w > 1000:
            self.x = 1000 - self.w

    def check_shield(self):
        if self.shield <= 0:
            self.kill()

    def update(self):
        self.move()
        self.check_screen_edges()
        self.check_shield()


class Goblin(SimpleSprite):

    def __init__(self, x, y, vx):
        super().__init__(x, y, random.choice(goblin_img))
        
        self.vx = vx
        self.value = 10

    def reverse_and_drop(self, dy):
        self.vx *= -1
        self.y += dy

    def drop_bomb(self, bombs, vy):
        x = self.x + self.w / 2 - bomb_img.get_width() / 2
        y = self.y + self.h - bomb_img.get_height()

        b = Bomb(x, y, vy)
        bombs.append(b)

    def update(self):
        self.move()

    
class Bullet(SimpleSprite):

    def __init__(self, x, y, vy):
        super().__init__(x, y, bullet_img)

        self.vy = vy

    def update(self):
        self.move()


class Bomb(SimpleSprite):

    def __init__(self, x, y, vy):
        super().__init__(x, y, bomb_img)
        
        self.vy = vy
        self.damage = 20

    def update(self):
        self.move()
