import pygame, sys
from game import Game

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 800
CELL_SIZE = 8

pygame.init()
pygame.font.init()  # Initialize the font module

window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Game of Life")

game = Game(WINDOW_WIDTH, WINDOW_HEIGHT, CELL_SIZE)

# Create a Font object (you can choose another font and size)
font = pygame.font.SysFont('Arial', 20)

clock = pygame.time.Clock()

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()

	game.update_game_state()

	#Drawing
	window.fill(pygame.Color('black'))
	game.draw(window)

	 # Calculate and render FPS
	fps = clock.get_fps()  # Get the current FPS
	fps_text = font.render(f'FPS: {fps:.2f}', True, pygame.Color('green'))
	
	# Calculate the size of the text for the background rectangle
	fps_rect = fps_text.get_rect(topleft=(10, 10))
	
	# Draw a black rectangle behind the FPS text
	pygame.draw.rect(window, pygame.Color('black'), fps_rect)
	
	# Blit the FPS text onto the window
	window.blit(fps_text, (10, 10))  # Position the FPS text at the top left corner

	pygame.display.update()
	clock.tick(12)
