import math, pygame
from settings import *

def normalizeAngle(angle):
    angle = angle % (2 * math.pi)
    if angle <= 0:
        angle = (2 * math.pi) + angle
    return angle 


class Ray:
    def __init__(self, angle, player, map):
        self.rayAngle = normalizeAngle(angle)
        self.player = player 
        self.map = map 

        self.is_facing_down = self.rayAngle > 0 and self.rayAngle < math.pi
        self.is_facing_up = not self.is_facing_down
        self.is_facing_right = self.rayAngle < 0.5 * math.pi or self.rayAngle > 1.5 * math.pi
        self.is_facing_left = not self.is_facing_right

        self.wall_hit_x = 0
        self.wall_hit_y = 0

        self.distance = 0

    def cast(self):
        found_horizontal_wall = False
        horizontal_hit_x = 0
        horizontal_hit_y = 0

        first_intersection_x = None
        first_intersection_y = None

        if self.is_facing_up:
            first_intersection_y = int(self.player.y / TILESIZE) * TILESIZE - 0.01
        else:
            first_intersection_y = int(self.player.y / TILESIZE) * TILESIZE + TILESIZE

        first_intersection_x = self.player.x + (first_intersection_y - self.player.y) / math.tan(self.rayAngle)
        next_horizontal_x = first_intersection_x
        next_horizontal_y = first_intersection_y

        ya = TILESIZE if self.is_facing_down else -TILESIZE
        xa = ya / math.tan(self.rayAngle)

        while 0 <= next_horizontal_x <= WINDOW_WIDTH and 0 <= next_horizontal_y <= WINDOW_HEIGHT:
            if self.map.has_wall_at(next_horizontal_x, next_horizontal_y):
                found_horizontal_wall = True
                horizontal_hit_x = next_horizontal_x
                horizontal_hit_y = next_horizontal_y
                break 
            next_horizontal_x += xa 
            next_horizontal_y += ya

        self.wall_hit_x = horizontal_hit_x
        self.wall_hit_y = horizontal_hit_y

        found_vertical_wall = False 
        vertical_hit_x = 0
        vertical_hit_y = 0 

        if self.is_facing_right:
            first_intersection_x = int(self.player.x / TILESIZE) * TILESIZE + TILESIZE
        else:
            first_intersection_x = int(self.player.x / TILESIZE) * TILESIZE - 0.01

        first_intersection_y = self.player.y + (first_intersection_x - self.player.x) * math.tan(self.rayAngle)

        next_vertical_x = first_intersection_x
        next_vertical_y = first_intersection_y

        xa = TILESIZE if self.is_facing_right else -TILESIZE
        ya = xa * math.tan(self.rayAngle)
        while 0 <= next_vertical_x <= WINDOW_WIDTH and 0 <= next_vertical_y <= WINDOW_HEIGHT:
            if self.map.has_wall_at(next_vertical_x, next_vertical_y):
                found_vertical_wall = True 
                vertical_hit_x = next_vertical_x
                vertical_hit_y = next_vertical_y
                break
            next_vertical_x += xa 
            next_vertical_y += ya 

        horizontal_distance = math.dist((self.player.x, self.player.y), (horizontal_hit_x, horizontal_hit_y)) if found_horizontal_wall else math.inf
        vertical_distance = math.dist((self.player.x, self.player.y), (vertical_hit_x, vertical_hit_y)) if found_vertical_wall else math.inf

        if horizontal_distance < vertical_distance:
            self.wall_hit_x = horizontal_hit_x
            self.wall_hit_y = horizontal_hit_y
            self.color = 160
        else:
            self.wall_hit_x = vertical_hit_x
            self.wall_hit_y = vertical_hit_y
            self.color = 255
        self.distance = min(horizontal_distance, vertical_distance) * math.cos(self.player.rotationAngle - self.rayAngle)
        self.color *= (LIGHT_LEVEL / self.distance)
        if self.color > 255:
            self.color = 255
        
        
    def render(self, screen):
        pygame.draw.line(screen, (255, 0, 0),
                         (self.player.x, self.player.y),
                         (self.wall_hit_x, self.wall_hit_y))
        
