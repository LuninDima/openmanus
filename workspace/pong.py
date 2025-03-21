import pygame
import random

# Initialize Pygame
pygame.init()

# Set window dimensions
width = 600
height = 400
size = (width, height)

# Create the screen
screen = pygame.display.set_mode(size)

# Set window title
pygame.display.set_caption("Pong")

# Define colors
black = (0, 0, 0)
white = (255, 255, 255)

# Paddle properties
paddle_width = 10
paddle_height = 60
paddle_speed = 5
paddle1_x = 10
paddle1_y = height // 2 - paddle_height // 2
paddle2_x = width - paddle_width - 10
paddle2_y = height // 2 - paddle_height // 2

# Ball properties
ball_size = 10
ball_x = width // 2 - ball_size // 2
ball_y = height // 2 - ball_size // 2
ball_speed_x = 3
ball_speed_y = 3

# Randomize initial ball direction
if random.random() < 0.5:
    ball_speed_x *= -1
if random.random() < 0.5:
    ball_speed_y *= -1

# Scores
score1 = 0
score2 = 0

# Score limit
score_limit = 10

# Font
font = pygame.font.Font(None, 36)

# Game loop
running = True
clock = pygame.time.Clock()
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                paddle1_speed = -paddle_speed
            elif event.key == pygame.K_s:
                paddle1_speed = paddle_speed
            elif event.key == pygame.K_UP:
                paddle2_speed = -paddle_speed
            elif event.key == pygame.K_DOWN:
                paddle2_speed = paddle_speed
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w or event.key == pygame.K_s:
                paddle1_speed = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                paddle2_speed = 0

    # Paddle movement
    paddle1_y += paddle1_speed
    paddle2_y += paddle2_speed

    # Keep paddles within bounds
    if paddle1_y < 0:
        paddle1_y = 0
    if paddle1_y > height - paddle_height:
        paddle1_y = height - paddle_height
    if paddle2_y < 0:
        paddle2_y = 0
    if paddle2_y > height - paddle_height:
        paddle2_y = height - paddle_height

    # Ball movement
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # Bounce off top and bottom
    if ball_y <= 0 or ball_y >= height - ball_size:
        ball_speed_y *= -1

    # Bounce off paddles
    if paddle1_x <= ball_x <= paddle1_x + paddle_width and paddle1_y <= ball_y <= paddle1_y + paddle_height:
        ball_speed_x *= -1
        ball_speed_x *= 1.1  # Increase ball speed
    if paddle2_x <= ball_x <= paddle2_x + paddle_width and paddle2_y <= ball_y <= paddle2_y + paddle_height:
        ball_speed_x *= -1
        ball_speed_x *= 1.1  # Increase ball speed

    # Scoring
    if ball_x < 0:
        score2 += 1
        ball_x = width // 2 - ball_size // 2
        ball_y = height // 2 - ball_size // 2
        ball_speed_x = 3
        if random.random() < 0.5:
            ball_speed_x *= -1
        if random.random() < 0.5:
            ball_speed_y *= -1
    if ball_x > width - ball_size:
        score1 += 1
        ball_x = width // 2 - ball_size // 2
        ball_y = height // 2 - ball_size // 2
        ball_speed_x = 3
        if random.random() < 0.5:
            ball_speed_x *= -1
        if random.random() < 0.5:
            ball_speed_y *= -1

    # Check for game over
    if score1 >= score_limit or score2 >= score_limit:
        running = False
        winner = "Player 1" if score1 > score2 else "Player 2"

    # Clear the screen
    screen.fill(black)

    # Draw paddles
    pygame.draw.rect(screen, white, (paddle1_x, paddle1_y, paddle_width, paddle_height))
    pygame.draw.rect(screen, white, (paddle2_x, paddle2_y, paddle_width, paddle_height))

    # Draw ball
    pygame.draw.rect(screen, white, (ball_x, ball_y, ball_size, ball_size))

    # Display score
    text = font.render(f"{score1} - {score2}", True, white)
    screen.blit(text, (width // 2 - text.get_width() // 2, 10))

    # Update the display
    pygame.display.flip()

    # Limit frame rate
    clock.tick(60)

# Game over message
if not running:
    game_over_text = font.render(f"Game Over! {winner} wins!", True, white)
    screen.blit(game_over_text, (width // 2 - game_over_text.get_width() // 2, height // 2 - game_over_text.get_height() // 2))
    pygame.display.flip()
    pygame.time.wait(3000)  # Wait for 3 seconds

# Quit Pygame
pygame.quit()