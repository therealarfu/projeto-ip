import pygame
import math
from settings import *

class Player:
    def __init__(self, x, y):
        self.x = x 
        self.y = y
        self.radius = 3
        self.rotationAngle = math.radians(45)
        self.turnDirection = 0
        self.walkDirection = 0
        self.moveSpeed = 200
        self.rotationSpeed = math.radians(200)

    def update(self, dt):
        keys = pygame.key.get_pressed()
        self.turnDirection = 0
        self.walkDirection = 0

        if keys[pygame.K_RIGHT]:
            self.turnDirection = 1
        if keys[pygame.K_LEFT]:
            self.turnDirection = -1
        if keys[pygame.K_UP]:
            self.walkDirection = 1
        if keys[pygame.K_DOWN]:
            self.walkDirection = -1

        moveStep = self.moveSpeed * self.walkDirection * dt
        self.rotationAngle += self.turnDirection * self.rotationSpeed * dt
        self.x += math.cos(self.rotationAngle) * moveStep 
        self.y += math.sin(self.rotationAngle) * moveStep 

    def render(self, screen):
        pygame.draw.circle(screen, (255, 0, 0), (self.x, self.y), self.radius)
        pygame.draw.line(screen, (0, 0, 255), (self.x, self.y), 
                         (self.x + 100 * math.cos(self.rotationAngle), 
                          self.y + 100 * math.sin(self.rotationAngle)))