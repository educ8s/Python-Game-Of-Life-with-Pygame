import pygame
import random

class Grid:
    def __init__(self, width, height, cell_size):
        self.width = width
        self.height = height
        self.cell_size = cell_size
        self.columns = width // cell_size
        self.rows = height // cell_size
        # Initialize the grid with False (dead cells)
        self.cells = [[False for _ in range(self.columns)] for _ in range(self.rows)]

    def draw(self, screen):
        for y in range(self.rows):
            for x in range(self.columns):
                color = (0, 255, 0) if self.cells[y][x] else (50, 50, 55)
                pygame.draw.rect(screen, color, (x * self.cell_size, y * self.cell_size, self.cell_size - 1, self.cell_size - 1))

    def fill_random(self):
        for y in range(self.rows):
            for x in range(self.columns):
                self.cells[y][x] = random.choice([True, False, False, False, False, False])

    def fill_zeros(self):
        # Reset the grid to all dead cells
        self.cells = [[False for _ in range(self.columns)] for _ in range(self.rows)]
