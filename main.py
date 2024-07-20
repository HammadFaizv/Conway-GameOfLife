import pygame # pygame-ce
import sys

from simulation import Simulation

pygame.init()

GREY = (29, 29, 29)
WIN_WIDTH, WIN_HEIGHT = 800, 800
CELL_SIZE = 20
FPS = 10

window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption("Conway's Game of Life")

clock = pygame.time.Clock()
simulation = Simulation(WIN_WIDTH, WIN_HEIGHT, CELL_SIZE)
mouse_held = False

# loop
while True:

    # event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_held = True
        if event.type == pygame.MOUSEBUTTONUP:
            mouse_held = False

        if mouse_held:
            x, y = pygame.mouse.get_pos()
            simulation.toggle_cell(y // CELL_SIZE, x // CELL_SIZE)

    # update
    if not mouse_held:
        simulation.update()
    # draw
    window.fill(GREY)
    simulation.draw(window)
    pygame.display.update()
    clock.tick(FPS)