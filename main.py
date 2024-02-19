import pygame, sys
from game import Game

WINDOW_WIDTH = 750
WINDOW_HEIGHT = 750
CELL_SIZE = 25
FPS = 12

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
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_RETURN:
				game.start()
				pygame.display.set_caption("Game of Life is Running")
			elif event.key == pygame.K_SPACE:
				game.run = False
				pygame.display.set_caption("Game of Life has Stopped")
			elif event.key == pygame.K_r:
				if not game.run:
					game.current_grid.fill_random()
			elif event.key == pygame.K_c:
				if not game.run:
					game.current_grid.fill_zeros()
					game.next_grid.fill_zeros()
			elif event.key == pygame.K_KP_PLUS:
				FPS*=1.5
			elif event.key == pygame.K_KP_MINUS and FPS > 2:
				FPS/=1.5

	if not game.run:
		game.GetClickedCell()

	game.update()

	#Drawing
	window.fill((29,29,29))
	game.draw(window)

	pygame.display.update()
	clock.tick(FPS)