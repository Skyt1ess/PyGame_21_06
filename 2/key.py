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

left = right = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        x -= speed
    elif keys[pygame.K_RIGHT]:
        x += speed

    display.fill(white)

    pygame.draw.rect(display, red, (x, y, 20, 20))
    pygame.display.update()

    clock.tick(20)