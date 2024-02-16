from grid import Grid

class Game:
	def __init__(self, width, height, cell_size):
		self.rows = height // cell_size
		self.columns = width // cell_size
		self.cell_size = cell_size
		self.current_grid = Grid(width, height, cell_size)
		self.current_grid.fill_random()
		self.next_grid = Grid(width, height, cell_size)

	def update_game_state(self):
		for row in range(self.rows):
			for column in range(self.columns):
				live_neighbors = self.count_live_neighbors(row, column)
				cell = self.current_grid.cells[row][column]
				if cell.is_alive:
					if live_neighbors < 2 or live_neighbors > 3:
						self.next_grid.cells[row][column].is_alive = False
					else:
						self.next_grid.cells[row][column].is_alive = True
				else:
					if live_neighbors == 3:
						self.next_grid.cells[row][column].is_alive = True

		for row in range(self.rows):
			for column in range(self.columns):
				self.current_grid.cells[row][column].is_alive = self.next_grid.cells[row][column].is_alive

	def count_live_neighbors(self, row, column):
		directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
		live_neighbors = 0
		max_row = self.rows
		max_column = self.columns
		
		for dx, dy in directions:
			# Calculate the neighbor's position with wrap-around
			nx = (row + dx) % max_row
			ny = (column + dy) % max_column
			
			# Directly add the boolean value of is_alive since True is treated as 1 and False as 0
			live_neighbors += self.current_grid.cells[nx][ny].is_alive
			
		return live_neighbors

	def draw(self, window):
		self.current_grid.draw(window)