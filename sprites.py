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

    def get_rect(self):
        return [self.x, self.y, self.w, self.h]

    def intersects(self, other):
        rect1 = self.get_rect()
        rect2 = other.get_rect()
        
        left1 = rect1[0]
        right1 = rect1[0] + rect1[2]
        top1 = rect1[1]
        bottom1 = rect1[1] + rect1[3]

        left2 = rect2[0]
        right2 = rect2[0] + rect2[2]
        top2 = rect2[1]
        bottom2 = rect2[1] + rect2[3]

        return not (right1 <= left2 or
                    left1 >= right2  or
                    bottom1 <= top2 or
                    top1 >= bottom2)

    def draw(self, screen):
        screen.blit(self.img, [self.x, self.y])
    

class Cannon(SimpleSprite):
    def __init__(self, x, y):
        super().__init__(x, y, cannon_img)
        
        self.alive = True
        self.shot_limit = 3
        self.start_x = x
        self.start_y = y

    def reset(self):
        self.x = self.start_x
        self.y = self.start_y

    def move(self, vx):
        self.x += vx

    def shoot(self, bullets, vy):
        x = self.x + self.w / 2 - bullet_img.get_width() / 2
        y = self.y

        b = Bullet(x, y, vy)
        bullets.append(b)
            
    def check_screen_edges(self):
        pass
    
    def process_aliens(self, bombs):
        pass

    def process_bombs(self, bombs):
        pass
    
    def update(self):
        self.check_screen_edges()


class Alien(SimpleSprite):
    def __init__(self, x, y, vx):
        super().__init__(x, y, alien_img)
        
        self.vx = vx
        self.alive = True

    def move(self):
        self.x += self.vx
        
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

    def update(self, bullets):
        self.move()

    
class Bullet(SimpleSprite):
    def __init__(self, x, y, vy):
        super().__init__(x, y, bullet_img)

        self.vx = 0
        self.vy = vy
        self.alive = True

    def move(self):
        self.y += self.vy

    def kill(self):
        self.alive = False

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
        
        self.vx = 0
        self.vy = vy
        self.alive = True

    def move(self):
        self.y += self.vy

    def update(self):
        self.move()
