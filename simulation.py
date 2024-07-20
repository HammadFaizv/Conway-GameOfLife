import copy
import pygame
import random

class Grid:
    def __init__(self, width, height, cell_size):
        self.rows = height // cell_size
        self.columns = width // cell_size
        self.cell_size = cell_size
        self.cells = [[0 for _ in range(self.columns)] for _ in range(self.rows)]

    def draw(self, window):
        # first create a grid
        for row in range(self.rows):
            for col in range(self.columns):
                # draw green if alive else draw grey
                color = (0, 170, 0) if self.cells[row][col] else (55, 55, 55)
                pygame.draw.rect(window, color, (col * self.cell_size, row * self.cell_size, self.cell_size-1, self.cell_size-1))

    def fill_random(self):
        for row in range(self.rows):
            for col in range(self.columns):
                self.cells[row][col] = random.choice([0, 1, 0, 0])


class Simulation:
    def __init__(self, width, height, cell_size):
        self.grid = Grid(width, height, cell_size)
        self.rows = height // cell_size
        self.columns = width // cell_size
        self.grid.fill_random()

    def draw(self, window):
        self.grid.draw(window)

    def count_live_neighbors(self, row, col):
        live_neighbors = 0

        neighbor_offsets = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

        for offset in neighbor_offsets:
            # toroidal grid
            new_row = (row + offset[0]) % self.rows
            new_col = (col + offset[1]) % self.columns
            if self.grid.cells[new_row][new_col] == 1:
                live_neighbors += 1

        return live_neighbors
    
    def toggle_cell(self, row, col):
        if col >= self.columns:
            return
        self.grid.cells[row][col] = 1 # set cell
    
    def update(self):
        new_cells = copy.deepcopy(self.grid.cells)

        for row in range(self.rows):
            for col in range(self.columns):
                live_neighbors = self.count_live_neighbors(row, col)
                alive = self.grid.cells[row][col]

                # apply rules
                if alive:
                    if live_neighbors < 2 or live_neighbors > 3:
                        new_cells[row][col] = 0
                else:
                    if live_neighbors == 3:
                        new_cells[row][col] = 1

        # copy values
        for row in range(self.rows):
            for col in range(self.columns):
                self.grid.cells[row][col] = new_cells[row][col]