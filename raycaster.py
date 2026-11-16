import pygame, math
from settings import *
from ray import Ray

class RayCaster:
    def __init__(self, player, map):
        self.rays = []
        self.player = player
        self.map = map

    def castAllRays(self):
        self.rays = []
        rayAngle = self.player.rotationAngle - FOV / 2
        da = FOV / (NUM_RAYS - 1)
        for i in range(NUM_RAYS):
            ray = Ray(rayAngle, self.player, self.map)
            ray.cast()
            self.rays.append(ray)
            rayAngle += da

    def render(self, screen):
        i = 0
        for ray in self.rays:

            line_height = (WALL_HEIGHT / ray.distance) * (0.5 * WINDOW_WIDTH / math.tan(0.5 * FOV))
            draw_begin = (WINDOW_HEIGHT / 2) - (line_height / 2)
            draw_end = line_height

            pygame.draw.rect(screen, (ray.color, ray.color, ray.color), (i*RES, draw_begin, RES, draw_end))

            i += 1