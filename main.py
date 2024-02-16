import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 600, 400
BALL_RADIUS = 15
PADDLE_WIDTH, PADDLE_HEIGHT = 10, 60
FPS = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("pong game")

# Initialize ball position and velocity
ball_x = WIDTH // 2
ball_y = HEIGHT // 2
ball_speed_x = random.choice([-0.5, 0.5])
ball_speed_y = random.choice([-0.5, 0.5])

# Initialize paddle positions
left_paddle_y = (HEIGHT - PADDLE_HEIGHT) // 2
right_paddle_y = (HEIGHT - PADDLE_HEIGHT) // 2

# Game loop
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Move paddles
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and left_paddle_y > 0:
        left_paddle_y -= 5
    if keys[pygame.K_s] and left_paddle_y < HEIGHT - PADDLE_HEIGHT:
        left_paddle_y += 5
    if keys[pygame.K_UP] and right_paddle_y > 0:
        right_paddle_y -= 5
    if keys[pygame.K_DOWN] and right_paddle_y < HEIGHT - PADDLE_HEIGHT:
        right_paddle_y += 5

    # Move the ball
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # Bounce off the top and bottom walls
    if ball_y - BALL_RADIUS <= 0 or ball_y + BALL_RADIUS >= HEIGHT:
        ball_speed_y = -ball_speed_y

    # Bounce off the paddles
    if (
        (ball_x - BALL_RADIUS <= PADDLE_WIDTH and left_paddle_y <= ball_y <= left_paddle_y + PADDLE_HEIGHT) or
        (ball_x + BALL_RADIUS >= WIDTH - PADDLE_WIDTH and right_paddle_y <= ball_y <= right_paddle_y + PADDLE_HEIGHT)
    ):
        ball_speed_x = -ball_speed_x

    # Check if the ball missed the paddle
    if ball_x - BALL_RADIUS <= 0 or ball_x + BALL_RADIUS >= WIDTH:
        # Reset the ball position
        ball_x = WIDTH // 2
        ball_y = HEIGHT // 2
        ball_speed_x = random.choice([-0.5, 0.5])
        ball_speed_y = random.choice([-0.5, 0.5])

    # Clear the screen
    screen.fill(BLACK)

    # Draw the paddles
    pygame.draw.rect(screen, WHITE, (0, left_paddle_y, PADDLE_WIDTH, PADDLE_HEIGHT))
    pygame.draw.rect(screen, WHITE, (WIDTH - PADDLE_WIDTH, right_paddle_y, PADDLE_WIDTH, PADDLE_HEIGHT))

    # Draw the ball
    pygame.draw.circle(screen, WHITE, (int(ball_x), int(ball_y)), BALL_RADIUS)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
   
