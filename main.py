import pygame, sys
from game import Game

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 800
CELL_SIZE = 8

pygame.init()

window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Game of Life")

game = Game(WINDOW_WIDTH, WINDOW_HEIGHT, CELL_SIZE)

clock = pygame.time.Clock()

while True:

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()

	game.update()

	#Drawing
	window.fill(pygame.Color('black'))
	game.draw(window)

	pygame.display.update()
	clock.tick(10)