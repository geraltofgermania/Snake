import pygame
import random

pygame.init()

print("made with love for Quan")

root = pygame.display.set_mode((600,600))
pygame.display.set_caption("SNAKE")

# colors
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
LEMON = (255,247,204)
pygame.mixer.init()
# audio
sigma_sound = 'sigmagrindset.mp3'
yummy = pygame.mixer.Sound('Snake\Snake\Recording.mp3')
yummy.set_volume(1)
#pygame.mixer.init()
pygame.mixer.music.load("Snake\Snake\sigmagrindset.mp3")
pygame.mixer.music.set_volume(0.3)
pygame.mixer.music.play(-1)


# game vars
game_over = False
clock = pygame.time.Clock()
snake_block = 40
snake_speed = 8
snake_change_x = 0
snake_change_y = 0
BUTTON_USED = True

# snake initial pos
x1 = 280
y1 = 280

snake_body = []
snake_length = 1

# food variables
food_x = random.randrange(0,600,40)
food_y = random.randrange(0,600,40)

while not game_over:
    
    # resent button status
    BUTTON_USED = True

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        # key strokes
        if event.type == pygame.KEYDOWN:
            # close game with scape keyu
            if event.key == pygame.K_ESCAPE:
                game_over = True
            # directions
            if event.key == pygame.K_UP and BUTTON_USED:
                if snake_length >= 2 and snake_change_y == 40:
                    break
                BUTTON_USED = False
                snake_change_x = 0
                snake_change_y = -40
            if event.key == pygame.K_DOWN and BUTTON_USED:
                if snake_length >= 2 and snake_change_y == -40:
                    break
                BUTTON_USED = False
                snake_change_x = 0
                snake_change_y = 40
            if event.key == pygame.K_LEFT and BUTTON_USED:
                if snake_length >= 2 and snake_change_x == 40:
                    break
                BUTTON_USED = False
                snake_change_x = -40
                snake_change_y = 0
            if event.key == pygame.K_RIGHT and BUTTON_USED:
                if snake_length >= 2 and snake_change_x == -40:
                    break
                BUTTON_USED = False
                snake_change_x = 40
                snake_change_y = 0
    # check for collision with food
    if x1 == food_x and y1 == food_y:
        snake_length += 1
        food_x = random.randrange(0,600,40)
        food_y = random.randrange(0,600,40)
        pygame.mixer.Sound.play(yummy)

    # check for impact with self
    for i in snake_body[:-1]:

        if i == snake_head:
            x1 = 280
            y1 = 280
            snake_change_x = 0
            snake_change_y = 0
            snake_head =[]
            snake_body = []
            snake_length = 1
            food_x = random.randrange(0,600,40)
            food_y = random.randrange(0,600,40)
            BUTTON_USED = True

    # check impact with borders
    if x1 < 0 or y1 < 0 or x1 > 560 or y1 > 560:
        x1 = 280
        y1 = 280
        snake_change_x = 0
        snake_change_y = 0
        snake_head =[]
        snake_body = []
        snake_length = 1
        food_x = random.randrange(0,600,40)
        food_y = random.randrange(0,600,40)
        BUTTON_USED = True

    # clear the screen
    root.fill(BLACK)

    # move the snake
    x1 += snake_change_x
    y1 += snake_change_y
    # wait for a bit
    snake_head = []
    snake_head.append(x1)
    snake_head.append(y1)
    snake_body.append(snake_head)
    # keep proper size
    if len(snake_body) > snake_length:
        del snake_body[0]
    #draw snake head
    pygame.draw.rect(root, LEMON, (x1, y1, snake_block, snake_block))
    # draw snake body
    for block in snake_body:
        pygame.draw.rect(root, RED, (block[0], block[1], snake_block, snake_block), 20)

    # draw food
    pygame.draw.rect(root, GREEN, (food_x, food_y, snake_block, snake_block), 20)

    # bottom of loop
    pygame.display.update()
    clock.tick(snake_speed)

# Snake\Snake\Recording.mp3