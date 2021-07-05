import pygame
pygame.init()

size = [600, 400]


display = pygame.display.set_mode(size)
clock = pygame.time.Clock()
FPS = 30

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)

player = pygame.Surface((40, 50))
player.fill(red)


ground = size[1] - 100

player_rect = player.get_rect(bottom=ground, centerx=size[0]/2)

jump_force = 20
move_y = jump_force + 1
speedx = 5

display.fill(white)
pygame.draw.rect(display, black, (0, ground, size[0], size[1] - ground))
rect_update = pygame.Rect(player_rect.x - speedx, 0,
                          player_rect.width + speedx * 2, ground)
pygame.display.update()


while True:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and ground == player_rect.bottom:
                move_y = -jump_force

    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT]:
        player_rect.x -= speedx
        rect_update.x -= speedx
    if key[pygame.K_RIGHT]:
        player_rect.x += speedx
        rect_update.x += speedx




    if move_y <= jump_force:
        if player_rect.bottom + move_y >= ground:
            player_rect.bottom = ground
            move_y = jump_force + 1
        else:
            player_rect.bottom += move_y
            move_y += 1
    # -20, -19 ... -1, 0, 1, 2, 3 .. 20
    #display.blit(display, rect_update)

    pygame.draw.rect(display, white, rect_update)
    display.blit(player, player_rect)


    pygame.display.update(rect_update)
