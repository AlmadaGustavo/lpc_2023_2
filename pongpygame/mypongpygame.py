# Jucimar Jr
# 2022

import pygame


pygame.init()

COLOR_BLACK = (0, 0, 0)
COLOR_WHITE = (255, 255, 255)

SCORE_MAX = 3

size = (1280, 720)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("MyPong - PyGame Edition - 2022-12-12")

# score text
score_font = pygame.font.Font('assets/PressStart2P.ttf', 44)
score_text = score_font.render('00 x 00', True, COLOR_WHITE, COLOR_BLACK)
score_text_rect = score_text.get_rect()
score_text_rect.center = (680, 50)

# victory text
victory_font = pygame.font.Font('assets/PressStart2P.ttf', 100)
victory_text = victory_font .render('VICTORY', True, COLOR_WHITE, COLOR_BLACK)
victory_text_rect = score_text.get_rect()
victory_text_rect.center = (450, 350)

# sound effects
bounce_sound_effect = pygame.mixer.Sound('assets/bounce.wav')
scoring_sound_effect = pygame.mixer.Sound('assets/258020__kodack__arcade-bleep-sound.wav')

# player 1
player_1 = pygame.image.load("assets/player.png")
player_1_y = 300
player_1_move_up = False
player_1_move_down = False

# player 2 - robot
player_2 = pygame.image.load("assets/player.png")
player_2_y = 300
ai_speed = 5

# division of the paddle
height_paddle = 150
paddle_part_height = height_paddle / 15

# ball
ball = pygame.image.load("assets/ball.png")
ball_x = 640
ball_y = 360
ball_dx = 5
ball_dy = 5
speed_limit = 20

def ball_start():
    global ball_x, ball_y, ball_dx, ball_dy
    ball_x = 640
    ball_y = 360
    ball_dx = 5
    ball_dy = 5
    ball_dx *= -1
    ball_dy *= -1
    scoring_sound_effect.play()
def speed_of_ball(ball_s):
    global speed_limit
    if abs(ball_s) < speed_limit:
        ball_s *= -1.11
    else:
        if ball_s > 0:
            ball_s = -speed_limit
        else:
            ball_s = speed_limit
    return ball_s




# score
score_1 = 0
score_2 = 0

# game loop
game_loop = True
game_clock = pygame.time.Clock()


while game_loop:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_loop = False

        #  keystroke events
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player_1_move_up = True
            if event.key == pygame.K_DOWN:
                player_1_move_down = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                player_1_move_up = False
            if event.key == pygame.K_DOWN:
                player_1_move_down = False

    # checking the victory condition
    if score_1 < SCORE_MAX and score_2 < SCORE_MAX:

        # clear screen
        screen.fill(COLOR_BLACK)

        # ball collision with the wall
        if ball_y > 700:
            ball_dy *= -1
            bounce_sound_effect.play()
        elif ball_y <= 0:
            ball_dy *= -1
            bounce_sound_effect.play()

        # ball collision with the player 1 's paddle
        # hitting in horizontal
        if 80 - abs(speed_of_ball(ball_dx)) < ball_x < 100:
            for i in range(15):
                if player_1_y + i * paddle_part_height < ball_y + 20 < player_1_y + (i + 1) * paddle_part_height:
                    if i == 7:
                        ball_dy = 0
                    else:
                        ball_dy = i - 7
                    ball_dx = speed_of_ball(ball_dx)
                    bounce_sound_effect.play()
                    break

        # hitting in vertical
        if 30 < ball_x < 80 - abs(speed_of_ball(ball_dx)):
            if player_1_move_up and player_1_y < ball_y <= player_1_y + 20 + speed_of_ball(ball_dy):
                ball_y -= (ball_dy + 15)
                ball_dy = speed_of_ball(ball_dy)
                bounce_sound_effect.play()
            elif player_1_move_down and player_1_y + 150 >= ball_y + 20 >= player_1_y + 130 - speed_of_ball(ball_dy):
                ball_y += (ball_dy + 15)
                ball_dy = speed_of_ball(ball_dy)
                bounce_sound_effect.play()
        elif 20 < ball_x < 100:
            if player_1_y + 30 == ball_y + 25 or player_1_y + 155 == ball_y:
                ball_dy = speed_of_ball(ball_dy)
                bounce_sound_effect.play()

        # ball collision with the player 2 's paddle
        if 1210 > ball_x > 1160:
            if player_2_y < ball_y + 25 and ball_dx > 0:
                if player_2_y + 150 > ball_y:
                    ball_dx *= -1
                    bounce_sound_effect.play()

        # scoring points
        if ball_x < -50:
            ball_start()
            score_2 += 1
        elif ball_x > 1320:
            ball_start()
            score_1 += 1


        # ball movement
        ball_x = ball_x + ball_dx
        ball_y = ball_y + ball_dy


        # player 1 up movement
        if player_1_move_up:
            player_1_y -= 5
        else:
            player_1_y += 0

        # player 1 down movement
        if player_1_move_down:
            player_1_y += 5
        else:
            player_1_y += 0

        # player 1 collides with upper wall
        if player_1_y <= 0:
            player_1_y = 0

        # player 1 collides with lower wall
        elif player_1_y >= 570:
            player_1_y = 570

        # player 2 ai movement
        if ball_dx > 0 and ball_x > 640:
            if player_2_y + 75 < ball_y:
                player_2_y += ai_speed
            elif player_2_y + 75 > ball_y:
                player_2_y -= ai_speed

        # player 2 "Artificial Intelligence"

        if player_2_y <= 0:
            player_2_y = 0
        elif player_2_y >= 570:
            player_2_y = 570

        # update score hud
        score_text = score_font.render(str(score_1) + ' x ' + str(score_2), True, COLOR_WHITE, COLOR_BLACK)

        # drawing objects
        screen.blit(ball, (ball_x, ball_y))
        screen.blit(player_1, (50, player_1_y))
        screen.blit(player_2, (1180, player_2_y))
        screen.blit(score_text, score_text_rect)
    else:
        # drawing victory
        screen.fill(COLOR_BLACK)
        screen.blit(score_text, score_text_rect)
        screen.blit(victory_text, victory_text_rect)

    # update screen
    pygame.display.flip()
    game_clock.tick(60)

pygame.quit()