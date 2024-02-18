import pygame, random 
from cell import Cell

class Grid:
	def __init__(self, width, height, cell_size):
		self.width = width
		self.height = height
		self.cell_size = cell_size
		self.columns = width // cell_size
		self.rows = height // cell_size
		self.cells = [[Cell(x * cell_size, y * cell_size, cell_size) for x in range(self.columns)] for y in range(self.rows)]

	def draw(self, screen):
		for row in self.cells:
			for cell in row:
				cell.draw(screen)

	def fill_random(self):
		for row in self.cells:
			for cell in row:
				cell.is_alive = random.choice([True, False, False, False, False, False])

	def fill_zeros(self):
		self.cells = [[Cell(x * self.cell_size, y * self.cell_size, self.cell_size) for x in range(self.columns)] for y in range(self.rows)]