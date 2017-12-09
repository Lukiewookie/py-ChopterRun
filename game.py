#!usr/bin/python2

import pygame, random

from chopter import Chopter

pygame.init()

GREEN = (20, 255, 140)
GREY = (210, 210, 210)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
PURPLE = (255, 0, 255)

SCREENWIDTH = 600
SCREENHEIGHT = 800

screen = pygame.display.set_mode((SCREENWIDTH,SCREENHEIGHT))
pygame.display.set_caption("Car Racing")

# This will be a list that will contain all the sprites we intend to use in our game.
all_sprites_list = pygame.sprite.Group()

player = Chopter(RED, 20, 30)
player.rect.x = 200
player.rect.y = 300

# Add the car to the list of objects
all_sprites_list.add(player)

# Allowing the user to close the window...
playing = True
clock = pygame.time.Clock()

while playing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:  # Pressing the x Key will quit the game
                playing = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.move_left(5)
    if keys[pygame.K_RIGHT]:
        player.move_right(5)
    if keys[pygame.K_UP]:
        player.move_up(4)
    if keys[pygame.K_DOWN]:
        player.move_down(6)

    all_sprites_list.update()
    screen.fill(GREEN)

    # Now let's draw all the sprites in one go. (For now we only have 1 sprite!)
    all_sprites_list.draw(screen)

    # Refresh Screen
    pygame.display.flip()

    # Number of frames per second e.g. 60
    clock.tick(60)

pygame.quit() 