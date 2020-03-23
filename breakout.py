import pygame  # import the pygame library and initialise the game engine(init)

from paddle import Paddle       # import the Paddle Class
from ball import Ball           # import the Ball Class
from brick import Brick         # import the Brick Class

pygame.init()

# define colors
WHITE = (255, 255, 255)
DARKBLUE = (66, 133, 244)
BROWN = (187, 150, 19)
RED = (219, 68, 55)
ORANGE = (255, 100, 0)
GREEN = (15, 157, 88)
YELLOW = (244, 160, 0)

# global variables
score = 0
lives = 5

# open game window
size = (800, 600)
screen = pygame.display.set_mode(size)

background = pygame.image.load('images/background.jpg')

# set the icon and title of the game window
pygame.display.set_caption("Breakout by LB")
icon = pygame.image.load('images/icon.png')
pygame.display.set_icon(icon)

# mouse disappear when over our window game
pygame.mouse.set_visible(0)

all_sprites_list = pygame.sprite.Group()     # list with all sprites we need(use)

# create the Paddle
paddle = Paddle(BROWN, 100, 20)              # paddle = new Paddle start draw point  x and y
paddle.rect.x = 350
paddle.rect.y = 560

# create the ball
ball = Ball(WHITE, 10, 10)
ball.rect.x = 345
ball.rect.y = 260

all_bricks = pygame.sprite.Group()

# bricks
# for x in range(7):  # column
#     for y in range(8):  # row
#         brick = Brick(RED, 80, 20)
#         brick.rect.x = 60 + x * 100
#         brick.rect.y = 50 + y * 30
#         all_sprites_list.add(brick)
#         all_bricks.add(brick)

for i in range(9):
    brick = Brick(DARKBLUE, 80, 20)
    brick.rect.x = 40 + i * 80
    brick.rect.y = 60
    all_sprites_list.add(brick)
    all_bricks.add(brick)
for i in range(9):
    brick = Brick(RED, 80, 20)
    brick.rect.x = 40 + i * 80
    brick.rect.y = 80
    all_sprites_list.add(brick)
    all_bricks.add(brick)
for i in range(9):
    brick = Brick(YELLOW, 80, 20)
    brick.rect.x = 40 + i * 80
    brick.rect.y = 100
    all_sprites_list.add(brick)
    all_bricks.add(brick)
for i in range(9):
    brick = Brick(DARKBLUE, 80, 20)
    brick.rect.x = 40 + i * 80
    brick.rect.y = 120
    all_sprites_list.add(brick)
    all_bricks.add(brick)
for i in range(9):
    brick = Brick(GREEN, 80, 20)
    brick.rect.x = 40 + i * 80
    brick.rect.y = 140
    all_sprites_list.add(brick)
    all_bricks.add(brick)
for i in range(9):
    brick = Brick(RED, 80, 20)
    brick.rect.x = 40 + i * 80
    brick.rect.y = 160
    all_sprites_list.add(brick)
    all_bricks.add(brick)
for i in range(9):
    brick = Brick(GREEN, 80, 20)
    brick.rect.x = 40 + i * 80
    brick.rect.y = 180
    all_sprites_list.add(brick)
    all_bricks.add(brick)
for i in range(9):
    brick = Brick(ORANGE, 80, 20)
    brick.rect.x = 40 + i * 80
    brick.rect.y = 200
    all_sprites_list.add(brick)
    all_bricks.add(brick)

all_sprites_list.add(paddle)  # add the paddle to the list of sprites
all_sprites_list.add(ball)  # add the ball to the list of sprites

# game will be on till exit (loop)
carryOn = True

# screen update - refresh per sec
clock = pygame.time.Clock()

# MAIN PROGRAM (loop)
while carryOn:
    # main event (loop)
    for event in pygame.event.get():  # do something
        if event.type == pygame.QUIT:  # if exit game close X
            carryOn = False  # exit game (finish loop)

    # moving the paddle by arrow keys left or right when button is pressed
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        paddle.moveLeft(20)  # by ... pixels
    if keys[pygame.K_RIGHT]:
        paddle.moveRight(20)

    # game logic
    all_sprites_list.update()

    # check if the ball is bouncing against any of the 4 walls:
    if ball.rect.x >= 790:
        ball.velocity[0] = -ball.velocity[0]    # * -1 ??
    if ball.rect.x <= 0:
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.y > 590:                       #if position ball is less than 590 y lives -1 and reset posiotion of ball to x and y posiotion
        ball.velocity[1] = -ball.velocity[1]
        lives -= 1
        pygame.time.wait(200)
        ball.rect.x = 345
        ball.rect.y = 260
        if lives == 0:
            # display Game Over !!! Message for 3 seconds
            font = pygame.font.Font(None, 74)
            text = font.render("GAME OVER !!!", 1, WHITE)
            screen.blit(text, (250, 300))
            pygame.display.flip()
            pygame.time.wait(3000)

            carryOn = False  # stop the game

    if ball.rect.y < 40:
        ball.velocity[1] = -ball.velocity[1]

    # bouncing/collisions between the ball and the paddles
    if pygame.sprite.collide_mask(ball, paddle):  # collision/detection between two sprites,
        ball.rect.x -= ball.velocity[0]
        ball.rect.y -= ball.velocity[1]
        ball.bounce2()

        # ball.rect.y -= ball.velocity[1]
        # ball.bounce()

    brick_collision_list = pygame.sprite.spritecollide(ball, all_bricks, False)
    for brick in brick_collision_list:
        ball.bounce()
        score += 1
        brick.kill()
        if len(all_bricks) == 0:
            # display WIN WIN WIN !!!  message for 3 sec
            font = pygame.font.Font(None, 74)
            text = font.render("WIN WIN WIN !!!", 1, WHITE)
            screen.blit(text, (200, 300))
            pygame.display.flip()
            pygame.time.wait(3000)

            carryOn = False                                         # stop the game

    # draw
    # Background Image
    screen.blit(background, (0, 0))
    # screen.fill(DARKBLUE)
    pygame.draw.line(screen, WHITE, [0, 38], [800, 38], 3)          # draw line color ... from x,y to x,y , stroke weight

    # score and number of lives on top screen
    font = pygame.font.Font(None, 34)                               # create a Font object
    text = font.render("Score: " + str(score), 1, WHITE)            # draw text "", edges(smooth), color
    screen.blit(text, (20, 10))                                     # draw text on screen position x and y
    text = font.render("Lives: " + str(lives), 1, WHITE)
    screen.blit(text, (650, 10))

    all_sprites_list.draw(screen)                                   # draw sprites

    # update screen (whai is in draw function)(loop)
    pygame.display.flip()

    # limit 60 frame per sec
    clock.tick(60)

# if we exit game stop engine (loop)
pygame.quit()