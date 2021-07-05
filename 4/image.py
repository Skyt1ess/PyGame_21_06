import pygame
pygame.init()


print(pygame.image.get_extended())

size = [600, 400]
display = pygame.display.set_mode(size)

clock = pygame.time.Clock()
FPS = 60


car_surf = pygame.image.load("images/car.bmp").convert()
car_surf = pygame.transform.scale(car_surf, (40, 60))
car_surf.set_colorkey((255, 255, 255))
car_rect = car_surf.get_rect(center=(size[0] / 2, size[1] / 2))

finish_surf = pygame.image.load("images/finish.png").convert_alpha()
finish_surf = pygame.transform.scale(finish_surf, (120, 60))

background = pygame.image.load("images/sand.jpg").convert()
background = pygame.transform.scale(background, size)


car_up = car_surf
car_down = pygame.transform.flip(car_surf, False, True)

car_left = pygame.transform.rotate(car_surf, 90)
car_right = pygame.transform.flip(car_left, True, False)

car_leftup = pygame.transform.rotate(car_surf, 45)
car_leftdown = pygame.transform.rotate(car_surf, 135)
car_rightup = pygame.transform.rotate(car_surf, -45)
car_rightdown = pygame.transform.rotate(car_surf, -135)

car = car_up
speed = 5
game = True

f_new = pygame.font.Font("20930.ttf", 24)
win_text = f_new.render("Вы победили", True, (255, 0, 0))
win_pos = win_text.get_rect(center=(size[0] / 2, size[1] / 2))

def check_win():
    return car_rect.colliderect(finish_surf.get_rect())

while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
            pygame.quit()



    key = pygame.key.get_pressed()
    if key[pygame.K_w] and key[pygame.K_d]:
        car = car_rightup
        car_rect = car.get_rect(y=car_rect.y - speed, x=car_rect.x + speed)
    elif key[pygame.K_w] and key[pygame.K_a]:
        car = car_leftup
        car_rect = car.get_rect(y=car_rect.y - speed, x=car_rect.x - speed)
    elif key[pygame.K_s] and key[pygame.K_d]:
        car = car_rightdown
        car_rect = car.get_rect(y=car_rect.y + speed, x=car_rect.x + speed)
    elif key[pygame.K_s] and key[pygame.K_a]:
        car = car_leftdown
        car_rect = car.get_rect(y=car_rect.y + speed, x=car_rect.x - speed)
    elif key[pygame.K_w]:
        car = car_up
        car_rect = car.get_rect(y=car_rect.y - speed, x=car_rect.x)
    elif key[pygame.K_s]:
        car = car_down
        car_rect = car.get_rect(y=car_rect.y + speed, x=car_rect.x)
    elif key[pygame.K_a]:
        car = car_left
        car_rect = car.get_rect(x=car_rect.x - speed, y=car_rect.y)
    elif key[pygame.K_d]:
        car = car_right
        car_rect = car.get_rect(x=car_rect.x + speed, y=car_rect.y)

    if car_rect.right > size[0]:
        car_rect.right = size[0]
    if car_rect.left < 0:
        car_rect.left = 0
    if car_rect.bottom > size[1]:
        car_rect.bottom = size[1]
    if car_rect.top < 0:
        car_rect.top = 0

    display.blit(background, (0, 0))
    display.blit(finish_surf, (0, 0))

    display.blit(car, car_rect)
    pygame.draw.rect(display, (0, 0, 0), car_rect, 1)

    if check_win():
        game = False
        display.blit(win_text, win_pos)
        pygame.display.update()
        pygame.time.wait(2000)


    pygame.display.update()
    clock.tick(FPS)