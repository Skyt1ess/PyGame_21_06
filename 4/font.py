import pygame
pygame.init()

size = [600, 400]
display = pygame.display.set_mode(size)

print(pygame.font.get_fonts())


white = (255, 255, 255)
red = (255, 0, 0)
yellow = (240, 230, 175)


f_new = pygame.font.Font('20930.ttf', 24)
f_new.set_underline(True)
f_new.set_bold(True)


text_new = f_new.render('PyGame Шрифты', True, yellow, red)
pos_new = text_new.get_rect(centerx=size[0] / 2, y=size[1] / 2 + 50)

display.fill(white)
display.blit(text_new, pos_new)

pygame.display.update()


clock = pygame.time.Clock()
FPS = 30


check = True
move = False

while check:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            check = False
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            pygame.mouse.get_rel()

    if move:
        button = pygame.mouse.get_pressed()
        if button[0]:
            rel = pygame.mouse.get_rel()
            pos_new.move_ip(rel)
            display.fill(white)
            display.blit(text_new, pos_new)
            move = True
        else:
            move = False


    if pygame.mouse.get_focused() and pos_new.collidepoint(pygame.mouse.get_pos()):
        button = pygame.mouse.get_pressed()
        if button[0] :
            move = True


    pygame.display.update()
    clock.tick(FPS)
