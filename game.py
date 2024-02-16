from grid import Grid

class Game:
	def __init__(self, width, height, cell_size):
		self.rows = height // cell_size
		self.columns = width // cell_size
		self.cell_size = cell_size
		self.current_grid = Grid(width, height, cell_size)
		self.current_grid.fill_random()
		self.next_grid = Grid(width, height, cell_size)
		self.draw_current = True  # Flag to determine which grid to draw


	def update(self):
		for row in range(self.rows):
			for column in range(self.columns):
				live_neighbors = self.count_live_neighbors(row, column, self.current_grid)
				cell = self.current_grid.cells[row][column]
				if cell.is_alive:
					if live_neighbors < 2 or live_neighbors > 3:
						self.next_grid.cells[row][column].is_alive = False
				else:
					if live_neighbors == 3:
						self.next_grid.cells[row][column].is_alive = True

		for row in range(self.rows):
			for column in range(self.columns):
				self.current_grid.cells[row][column].is_alive = self.next_grid.cells[row][column].is_alive

	def count_live_neighbors(self, row, column, grid):
		directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
		live_neighbors = 0
		max_row = self.rows
		max_column = self.columns
		
		for dx, dy in directions:
			nx = (row + dx) % max_row
			ny = (column + dy) % max_column
			live_neighbors += grid.cells[nx][ny].is_alive
			
		return live_neighbors

	def draw(self, window):
		self.current_grid.draw(window)