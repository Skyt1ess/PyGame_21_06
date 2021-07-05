import pygame
import random
import time

pygame.init()

size = [600, 400]
display = pygame.display.set_mode(size)

green = (0, 255, 0)
red = (255, 0, 0)
white = (255, 255, 255)

x = 300
y = 200
speed = 5

clock = pygame.time.Clock()

startDraw = False

x = None

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    pressed = pygame.mouse.get_pressed()
    if pressed[0]:
        pos = pygame.mouse.get_pos()

        if x is None:
            x = pos

        pygame.draw.line(display, red, (x[0], x[1]), (pos[0], pos[1]), 2)
        x = pos
        pygame.display.update()

    else:
        x = None

    clock.tick(20)