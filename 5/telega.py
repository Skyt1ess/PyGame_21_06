import pygame

class Telega(pygame.sprite.Sprite):
    def __init__(self, size):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("images/telega.png").convert_alpha()
        self.rect = self.image.get_rect(centerx=size[0]/2, bottom=size[1])
        self.speed = 5

    def update(self, size):
        key = pygame.key.get_pressed()

        if key[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if key[pygame.K_RIGHT]:
            self.rect.x += self.speed

        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > size[0]:
            self.rect.right = size[0]

    def draw(self, display):
        display.blit(self.image, self.rect)