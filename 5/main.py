import pygame
pygame.init()

from ball import create_ball
from telega import Telega



pygame.time.set_timer(pygame.USEREVENT, 2000)

size = [900, 570]
display = pygame.display.set_mode(size)

clock = pygame.time.Clock()
FPS = 60

background = pygame.image.load("images/back1.jpg").convert()


score = 0
score_back = pygame.image.load("images/score_fon.png").convert_alpha()
font = pygame.font.SysFont('arial', 30)

telega = Telega(size)
balls = pygame.sprite.Group()


def check_collision():
    global score
    for ball in balls:
        if telega.rect.collidepoint(ball.rect.center):
            score += ball.score
            ball.kill()



def draw():
    display.blit(background, (0, 0))
    balls.draw(display)
    display.blit(score_back, (0, 0))
    score_text = font.render(str(score), True, (100, 140, 15))
    display.blit(score_text, (20, 10))
    telega.draw(display)
    pygame.display.update()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.USEREVENT:
            create_ball(size[0], balls)

    draw()

    balls.update(size[1])
    telega.update(size)
    check_collision()

    clock.tick(FPS)