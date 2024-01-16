import pygame as pg
from pygame.locals import *

pg.init()
screen = pg.display.set_mode((800, 500))
sprite1 = pg.image.load("megaman1.png")
sprite2 = pg. image.load("megaman2.png")
sprite_control = sprite1
background = pg. image.load("background2.jpg")

position_x = 300
position_y = 300
position_sprite_x = 0
position_sprite_y = 0
sprite_width = 80

game_loop = False

jumping = False
Y_GRAVITY = 30
JUMP_HEIGHT = 60
Y_VELOCITY = JUMP_HEIGHT


while not game_loop:
    screen.blit(background, (0, 0), (0, 0, 800, 500))
    screen.blit(sprite_control, (position_x, position_y), (position_sprite_x, position_sprite_y, sprite_width, 90))

    pg.display.flip()
    clock = pg.time.Clock().tick(15)
    screen.fill(0)

    # Animation
    if sprite_control == sprite1:
        if position_sprite_y == 100:
            position_sprite_x += 90
            if position_sprite_x > 300:
                position_sprite_x = 0
    else:
        position_sprite_x -= 90
        if position_sprite_x <= 100:
            position_sprite_x = 400

    # Controls
    for e in pg.event.get():
        if e.type == pg.QUIT or e.type == KEYDOWN and e.type == K_ESCAPE:
            game_loop = True

    keys = pg.key.get_pressed()

    if keys[K_RIGHT]:
        sprite_control = sprite1
        sprite_width = 100
        position_x += 15
        position_sprite_y += 100
        if position_sprite_y >= 100:
            position_sprite_y = 100

    elif keys[K_LEFT]:
        sprite_control = sprite2
        sprite_width = 80
        position_x -= 15
        position_sprite_y += 100
        if position_sprite_y >= 100:
            position_sprite_y = 100

    elif position_sprite_x >= 0 and sprite_control == sprite1:
        position_sprite_x = 0
        position_sprite_y = 0
        sprite_width = 80

    elif position_sprite_x <= 400:
        position_sprite_y = 0
        position_sprite_x = 400

    if keys[K_SPACE]:
        jumping = True
        if sprite_control == sprite1:
            position_sprite_y = 190
        else:
            position_sprite_y = 190
            position_sprite_x = 390
            sprite_width = 90
    if jumping:
        position_y -= Y_VELOCITY
        Y_VELOCITY -= Y_GRAVITY
        if Y_VELOCITY < -JUMP_HEIGHT:
            jumping = False
            Y_VELOCITY = JUMP_HEIGHT