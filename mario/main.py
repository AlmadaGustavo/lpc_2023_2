import pygame as pg
from pygame.locals import *

pg.init()
screen = pg.display.set_mode((800, 500))
sprite = pg.image.load("img.png")
background = pg.image.load("background.png")

x_sprite = 400
y_sprite = 0
mario_x = 0
mario_y = 401
close = False
jumping = False
Y_GRAVITY = 5
JUMP_HEIGHT = 20
Y_VELOCITY = JUMP_HEIGHT

while not close:
    screen.blit(background, (0, 0), (0, 0, 800, 500))
    screen.blit(sprite, (mario_x, mario_y), (x_sprite, y_sprite, 50, 36))
    pg.display.flip()
    clock = pg.time.Clock().tick(10)
    screen.fill(0)

    # Controls
    for e in pg.event.get():
        if e.type == pg.QUIT or e.type == KEYDOWN and e.type == K_ESCAPE:
            close = True
    key = pg.key.get_pressed()
    if key[K_RIGHT]:
        mario_x += 15
        x_sprite += 60
        if x_sprite > 600:
            x_sprite = 480
    elif key[K_LEFT]:
        mario_x -= 15
        x_sprite -= 60
        if x_sprite < 115:
            x_sprite = 290

    elif x_sprite >= 400:
        x_sprite = 400
    elif x_sprite <= 350:
        x_sprite = 350

    if key[K_SPACE]:
        jumping = True
        if x_sprite >= 400:
            x_sprite = 710
        else:
            x_sprite = 50
    if jumping:
        mario_y -= Y_VELOCITY
        Y_VELOCITY -= Y_GRAVITY
        if Y_VELOCITY < -JUMP_HEIGHT:
            jumping = False
            Y_VELOCITY = JUMP_HEIGHT