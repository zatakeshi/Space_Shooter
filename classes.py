import pygame
from random import randint, choice

#CONSTS
WHITE = (240, 240, 240)
LIGHTGREY = (140, 140, 140)
DARKGREY = (90, 90, 90)
DARK = (40, 40, 40)
BLACK = (0, 0, 0)
SCREENWIDTH = 1024
SCREENHEIGHT = 768

class Ship(pygame.sprite.Sprite):
    def __init__ (self, colour, width, height):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface([width, height])
        self.image = pygame.image.load("graphics/PlayerShip/Player_1.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect()

        #Start at bottom-middle of screen
        self.rect.x = SCREENWIDTH / 2 - self.rect.width / 2
        self.rect.y = SCREENHEIGHT - self.rect.height * 1.5

    def moveLeft(self, pixels):
        self.rect.x -= pixels
            
    def moveRight(self, pixels):
        self.rect.x += pixels

    def moveUp(self, pixels):
        if(self.rect.y > self.rect.height):
            self.rect.y -= pixels

    def moveDown(self, pixels):
        if(self.rect.y < SCREENHEIGHT - self.rect.height * 1.2):
            self.rect.y += pixels

class Laser(pygame.sprite.Sprite):
    def __init__ (self, colour, width, height, xPos, yPos):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface([width, height])
        self.image = pygame.image.load("graphics/weapons/Laser_1.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect()

        self.rect.x = xPos
        self.rect.y = yPos

class Star():
    def __init__(self):

        self.speed = choice([1, 2, 3, 4])
        self.colour = (240, 230, randint(220, 240))
        self.size = choice([1, 2])
        
        #Offscreen stars appear when scrolling.
        self.xPos = randint(-SCREENWIDTH / 2, SCREENWIDTH * 1.5)
        self.yPos = randint(-SCREENHEIGHT, 0)

        if self.speed == 1:
            self.size = choice([2, 3, 4])
            self.colour = (randint(30, 45), randint(30, 45), randint(30, 45))
                           
        elif self.speed == 2:
            self.size = choice([2, 3, 4])
            self.colour = (randint(80, 95), randint(80, 95), randint(80, 95))
        elif self.speed == 3:
            self.size = choice([1, 2, 3])
            self.colour = (randint(140, 240), 140, 140)

    #Streak down the screen until bottom, then reinit
    def streakDown(self):
        if self.yPos < SCREENHEIGHT:
            self.yPos += self.speed
        else:
            self.__init__()
    
    def moveLeft(self):
        self.xPos += self.speed * .5
    def moveRight(self):
        self.xPos -= self.speed * .5


class powerUp():
    def __init__(self):
        self.timer = 0
        self.SIZE = 20
        self.type = choice([1, 2, 5, 8])
        self.image = pygame.Surface([self.SIZE, self.SIZE])
        self.image = pygame.image.load("graphics/Extras/bonus-01s.png").convert_alpha()
        self.rect.x = randint(0, SCREENWIDTH)
        self.rect.y = randint(0, SCREENHEIGHT / 2)

        if self.type == 1:
            pass
        
        elif self.type == 2:
            self.image = pygame.image.load("graphics/Extras/bonus-02s.png").convert_alpha()
            
        elif self.type == 5:
            self.image = pygame.image.load("graphics/Extras/bonus-05s.png").convert_alpha()
            
        else:
            self.image = pygame.image.load("graphics/Extras/bonus-08s.png").convert_alpha()

