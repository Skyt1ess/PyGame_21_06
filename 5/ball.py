import pygame
from random import randint

balls_data = [{'image': "images/ball_bear.png", 'score': 100},
              {'image': "images/ball_fox.png", 'score': 150},
              {'image': "images/ball_hed.png", 'score': 200}]


class Ball(pygame.sprite.Sprite):
    def __init__(self, x, speed, data, group):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(data['image']).convert_alpha()
        self.rect = self.image.get_rect(center=(x,0))
        self.speed = speed
        self.score = data['score']
        self.add(group)


    def update(self, y):
        if self.rect.bottom >= y:
            self.kill()
        else:
            self.rect.y += self.speed


def create_ball(display_x, group):
    index = randint(0, len(balls_data) - 1)
    x = randint(20, display_x - 20)
    speed = randint(1, 4)

    return Ball(x, speed, balls_data[index], group)



