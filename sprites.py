from assets import *

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
    

class Cannon(SimpleSprite):

    def __init__(self, x, y):
        super().__init__(x, y, cannon_img)
        
        self.alive = True
        self.shield = 100

    def move(self, vx):
        self.x += vx

    def shoot(self, bullets, vy):
        x = self.x + self.w / 2 - bullet_img.get_width() / 2
        y = self.y

        b = Bullet(x, y, vy)
        bullets.append(b)

    def check_screen_edges(self):
        if self.x < 0:
            self.x = 0
        elif self.x + self.w > 1000:
            self.x = 1000 - self.w

    def check_power(self):
        if self.shield <= 0:
            self.kill()

    def update(self):
        self.check_screen_edges()
        self.check_power()


class Alien(SimpleSprite):

    def __init__(self, x, y, vx):
        super().__init__(x, y, alien_img)
        
        self.vx = vx

    def reverse_and_drop(self, dy):
        self.vx *= -1
        self.y += dy

    def kill(self):
        self.alive = False

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

    def check_screen_edges(self):
        if self.y + self.h < 0:
            self.alive = False

    def process_enemies(self, enemies):
        for e in enemies:
            if self.intersects(e):
                e.kill()
                self.kill()

    def update(self, enemies):
        self.move()
        self.process_enemies(enemies)
        self.check_screen_edges()


class Bomb(SimpleSprite):

    def __init__(self, x, y, vy):
        super().__init__(x, y, bomb_img)
        
        self.vy = vy
        self.damage = 20

    def move(self):
        self.y += self.vy

    def process_cannon(self, cannon):
        if self.intersects(cannon):
            cannon.shield -= self.damage
            self.kill()

    def check_ground(self, ground):
        if self.y > ground.y:
            self.kill()

    def update(self, cannon, ground):
        self.move()
        self.process_cannon(cannon)
        self.check_ground(ground)
