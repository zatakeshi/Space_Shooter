"""

 Scrolling parallax starfield effect by ZaTakeshi
   - Based on Parallax Starfield Simulation by Leonel Machava

 Spaceship graphics by Carlos Alface on OpenGameArt.org

 Laser weapon graphics by Rawdanitsu on OpenGameArt.org
 
"""

import pygame
from random import randint, choice
from classes import *

#Initialise and system vars
pygame.init()
clock = pygame.time.Clock()
SCREENWIDTH = 1024
SCREENHEIGHT = 768
screen = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
pygame.display.set_caption("Space Shooter")
WHITE = (240, 240, 240)
LIGHTGREY = (140, 140, 140)
DARKGREY = (90, 90, 90)
DARK = (40, 40, 40)
BLACK = (0, 0, 0)
LASERSIZE = 30
exitGame = False
shooting = False

#Starfield
NUMSTARS = 200
starList = []

#Controls
keys = {'left':False, 'right':False, 'up':False, 'down':False}

#Player sprite details
PLAYERHEIGHT = int(145 / 2)
PLAYERWIDTH = int(106 / 2)
movePixels = 1
playerMoveSpeed = 3
playerShip = Ship(WHITE, PLAYERWIDTH, PLAYERHEIGHT)
weapons = {'laser': True}

#Sprite list
playerSprite = pygame.sprite.Group()
playerSprite.add(playerShip)
weapons = pygame.sprite.Group()

#Populate the list of stars
for i in range(NUMSTARS):
    starList.append(Star())

while not exitGame:
    screen.fill(BLACK)

    #Get current Pos of player's ship
    xPos = playerShip.rect.x
    yPos = playerShip.rect.y
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
             exitGame = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                shooting = True
                laser = Laser(WHITE, 12, 21, xPos + 21, yPos)
                weapons.add(laser)
            if event.key == pygame.K_UP:
                keys['up'] = True
            if event.key == pygame.K_DOWN:
                keys['down'] = True
            if event.key == pygame.K_LEFT:
                keys['left'] = True
            if event.key == pygame.K_RIGHT:
                keys['right'] = True

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                keys['up'] = False
            if event.key == pygame.K_DOWN:
                keys['down'] = False
            if event.key == pygame.K_LEFT:
                keys['left'] = False
            if event.key == pygame.K_RIGHT:
                keys['right'] = False

    if keys['left']:
        if playerShip.rect.x > playerShip.rect.width * .2:
            playerShip.moveLeft(playerMoveSpeed)
            for Star in starList:
                Star.moveLeft()
                
    if keys['right']:
        if playerShip.rect.x < SCREENWIDTH - playerShip.rect.width * 1.2:
            playerShip.moveRight(playerMoveSpeed)
            for Star in starList:
                Star.moveRight()
            
    if keys['up']:
        playerShip.moveUp(playerMoveSpeed)
        
    if keys['down']:
        playerShip.moveDown(playerMoveSpeed)

    for Star in starList:
        Star.streakDown()
        screen.fill(Star.colour, (Star.xPos, Star.yPos, Star.size, Star.size))

    for laser in weapons:
        laser.rect.y -= 5
        if laser.rect.y < 5:
            weapons.remove(laser)
            shooting = False
       
    weapons.draw(screen)
    playerSprite.draw(screen)
    pygame.display.flip()
    
    clock.tick(80)

pygame.quit()
