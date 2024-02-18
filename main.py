import pygame, sys
from game import Game

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 800
CELL_SIZE = 4

pygame.init()

font = pygame.font.Font(None, 30)


window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Game of Life")

game = Game(WINDOW_WIDTH, WINDOW_HEIGHT, CELL_SIZE)

clock = pygame.time.Clock()

frameRate = 60

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
				frameRate*=1.5
			elif event.key == pygame.K_KP_MINUS and frameRate > 2:
				frameRate/=1.5
			elif event.key == pygame.K_0:
				if pygame.key.get_pressed()[pygame.K_UP]:
					game.make_preset(0,0)
				elif pygame.key.get_pressed()[pygame.K_RIGHT]:
					game.make_preset(0,1)
				elif pygame.key.get_pressed()[pygame.K_DOWN]:
					game.make_preset(0,2)
				elif pygame.key.get_pressed()[pygame.K_LEFT]:
					game.make_preset(0,3)
				else:
					game.make_preset(0,0)
			elif event.key == pygame.K_1:
				game.make_preset(1,0)

	if not game.run:
		game.GetClickedCell()

	game.update()
	game.update_mouse_pos()
	#Drawing
	window.fill("black")
	game.draw(window)

	fps = clock.get_fps()
	fps_text = font.render(f'FPS: {fps:.2f}', True, pygame.Color('white'))
	window.blit(fps_text, (10, 10))

	pygame.display.update()
	clock.tick(frameRate)