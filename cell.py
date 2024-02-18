import pygame

class Cell:
    def __init__(self, x, y, size, is_alive=False):
        self.x = x
        self.y = y
        self.size = size - 1
        self.is_alive = is_alive

    def draw(self, screen):
        color = (50, 50, 55) if not self.is_alive else (255, 255, 255)
        pygame.draw.rect(screen, color, (self.x, self.y, self.size, self.size))