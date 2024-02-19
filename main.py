import pygame, sys
from game import Game
import time
import asyncio,threading
import math

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 800
CELL_SIZE = 4

pygame.init()

font = pygame.font.Font(None, 30)

def UPDATE():
	global updateTime
	while True:
		updateStart = time.time()
		game.update()
		game.update_mouse_pos()
		updateTime = time.time()-updateStart

def DRAW():
	window.fill(0x000000)
	drawStart = time.time()
	game.draw(window)
	curTime = time.time()-drawStart
	window.blit(font.render(f'Draw FPS: {(clock.get_fps()):.2f}', True, pygame.Color('white')), (10, 45))
	window.blit(font.render(f'Update FPS: {inf if updateTime == 0 else (1/updateTime):.2f}', True, pygame.Color('white')), (10, 10))
	pygame.display.update()

window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Game of Life")

game = Game(WINDOW_WIDTH, WINDOW_HEIGHT, CELL_SIZE)

async def main():
    await asyncio.gather(DRAW(), UPDATE())

inf= math.inf

clock = pygame.Clock()

frameRate = 60

UPDATE_THREAD = threading.Thread(target=UPDATE)

# Start the threads
UPDATE_THREAD.start()

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
				game.current_grid.fill_zeros()
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

	DRAW()


	clock.tick(60)
	