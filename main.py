import pygame
from settings import *
from map import Map
from player import Player
from raycaster import RayCaster

player = Player(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)
map = Map()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()
raycaster = RayCaster(player, map)

while True:
    dt = clock.tick(FPS) / 1000
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    player.update(dt)
    raycaster.castAllRays()

    screen.fill((0, 0, 0))
    raycaster.render(screen)
    pygame.display.update()