import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 600, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Square Pattern with Lines in Pygame")

# Set up colors
white = (255, 255, 255)
black = (0, 0, 0)

# Set up square properties
square_size = 1
margin = 100

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Clear the screen
    screen.fill(white)

    # Draw the square pattern using lines
    for row in range(height // (square_size + margin)):
        y = row * (square_size + margin)
        pygame.draw.line(screen, black, (0, y), (width, y), square_size)

    for col in range(width // (square_size + margin)):
        x = col * (square_size + margin)
        pygame.draw.line(screen, black, (x, 0), (x, height), square_size)

    # Update the display
    pygame.display.update()

    # Add a small delay to control the frame rate
    pygame.time.delay(100)

# Unreachable code, but kept to emphasize the infinite loop!
