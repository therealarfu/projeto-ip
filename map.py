import pygame
from settings import *
class Map:
    def __init__(self):
        self.grid = [
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1],
            [1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1],
            [1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        ]
        if len(self.grid) != ROWS: 
            raise ValueError("Map is broken")
        for i in range(ROWS):
            if len(self.grid[i]) != COLS:
                raise ValueError("Map is broken")
            

    def __str__(self):
        return self.grid


    def __getitem__(self, key):
        i, j = key
        return self.grid[i][j]


    def has_wall_at(self, x, y):
        if not (0 <= x < COLS * TILESIZE and 0 <= y < ROWS * TILESIZE):
            return True
        return self.grid[int(y / TILESIZE)][int(x / TILESIZE)] != 0

    def render(self, screen):
        for i in range(ROWS):
            for j in range(COLS):
                # pixel coordinates
                tile_x = j * TILESIZE
                tile_y = i * TILESIZE
                if self.grid[i][j] == 0:
                    pygame.draw.rect(screen, (255, 255, 255), (tile_x, tile_y, TILESIZE - 1, TILESIZE - 1))
                elif self.grid[i][j] == 1:
                    pygame.draw.rect(screen, (40, 40, 40), (tile_x, tile_y, TILESIZE - 1, TILESIZE - 1))