import pygame
import random
from load_images import *
from settings import *


class Player(pygame.sprite.Sprite):
    def __init__(self, filename, x= 450, y=500): 
        pygame.sprite.Sprite.__init__(self)
        self.image = filename
        self.rect = self.image.get_rect()
        self.pos = vec(x, y)
        self.vel = vec(0,0)
        self.acc = vec(0,0)

    def update(self):
        self.acc = vec(0, 5)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.image = doraeleft
            self.acc.x = -player_acc
        if keys[pygame.K_RIGHT]:
            self.image = dorae
            self.acc.x = player_acc
        if keys[pygame.K_DOWN]:
            self.vel.y += 5

        self.acc.x += self.vel.x * player_friction
        self.vel += self.acc
        self.pos += self.vel + self.acc
        self.rect.midbottom = self.pos
        if self.pos.x > display_width:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = display_width

        self.rect.midbottom = self.pos


class Block(pygame.sprite.Sprite):
    def __init__(self, color = red, x =100, y=100):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface( (100, 20) )
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def set_image(self, filename=None):
        self.image = filename

    def update(self, speed):
        block_y = (450, 520, 620, 720, 820, 930)
        if self.rect.y <= 10:
            self.rect.y = 650 
        self.rect.y -= speed


class Boundaries(pygame.sprite.Sprite):
    def __init__(self, filename, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = filename
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class FallingObjects(pygame.sprite.Sprite):
    def __init__(self, filename):
        pygame.sprite.Sprite.__init__(self)
        self.image = filename
        self.rect = self.image.get_rect()
        self.set_position()
        
    def set_position(self):
        self.y_start = (0, 5, 10, 12, 15, 20)
        self.x_start = (10, 50, 80, 100, 150, 200, 240, 270, 300, 350, 400, 450, 500, 530, 560)
        self.speeds = (3, 4, 5, 6)
        
        self.y_speed = self.random_y_speed()
        
        self.rect.x = self.randomX()
        self.rect.y = self.randomY()
        
    def update(self):
        self.rect.y += self.y_speed
        if self.rect.y > display_height - 30:
            self.rect.y = self.randomY()
            self.rect.x = self.randomX()
            self.y_speed = self.random_y_speed()
            
    def randomX(self):
        return random.choice(self.x_start)

    def randomY(self):
        return random.choice(self.y_start)

    def random_y_speed(self):
        return random.choice(self.speeds)
