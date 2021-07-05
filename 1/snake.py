import pygame
import random
import time
pygame.init()

size = [600, 400]
display = pygame.display.set_mode(size)
pygame.display.set_caption('Snake')

green = (0, 255, 0)
red = (255, 0, 0)
white = (255, 255, 255)

block_size = 10
snake_list = []
snake_len = 1

x1 = 300
y1 = 300
delta = [0, 0]

game_over = False
clock = pygame.time.Clock()
FPS = 30


foodx = round(random.randrange(0, size[0] - block_size) / 10.0) * 10.0
foody = round(random.randrange(0, size[1] - block_size) / 10.0) * 10.0

point_style = pygame.font.SysFont(None, 20)
style = pygame.font.SysFont(None, 50)

def print_point():
    value = point_style.render("Point: " + str(snake_len - 1), True, white)
    display.blit(value, [5, 5])

def snake_print():
    for element in snake_list:
        pygame.draw.rect(display, green, (element[0], element[1], block_size, block_size))
    pygame.draw.rect(display, red, (x1, y1, block_size, block_size))

def key_down(event):
    if event.key == pygame.K_LEFT:
        delta = [-block_size, 0]
    if event.key == pygame.K_RIGHT:
        delta = [block_size, 0]
    if event.key == pygame.K_UP:
        delta = [0, -block_size]
    if event.key == pygame.K_DOWN:
        delta = [0, block_size]
    return delta


while game_over == False:
    clock.tick(FPS)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            delta = key_down(event)

    if x1 >= size[0] or x1 < 0 or y1 >= size[1] or y1 < 0:
        game_over = True


    display.fill((0, 0, 0))

    x1 += delta[0]
    y1 += delta[1]

    pygame.draw.rect(display, white, (foodx, foody, block_size, block_size))


    snake_list.append([x1, y1])
    if len(snake_list) > snake_len:
        del snake_list[0]

    snake_print()
    print_point()


    if x1 == foodx and y1 == foody:
        snake_len += 1
        foodx = round(random.randrange(0, size[0] - block_size) / 10.0) * 10.0
        foody = round(random.randrange(0, size[1] - block_size) / 10.0) * 10.0


    pygame.display.update()

mes = style.render("Игра закончена!", True, white)
display.blit(mes, (size[0] / 3, size[1] / 3))
pygame.display.update()
time.sleep(2)
quit()