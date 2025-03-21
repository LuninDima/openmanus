import pygame

# Initialize Pygame
pygame.init()

# Set window dimensions
width = 800
height = 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("2D Shooter Game")

# Game loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    # Game logic (currently empty)

    # Drawing
    screen.fill((0, 0, 0))  # Fill the screen with black
    pygame.display.flip()  # Update the display

# Quit Pygame
pygame.quit()