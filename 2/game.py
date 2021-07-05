import pygame
import random
pygame.init()

size = [500, 600]
display = pygame.display.set_mode(size)
pygame.display.set_caption('key')

green = (0, 255, 0)
red = (255, 0, 0)
white = (255, 255, 255)
laguna = (7, 235, 250)


clock = pygame.time.Clock()
FPS = 30

game = True
score = 0
timer = 0
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, player):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10, 10))
        self.image.fill(laguna)
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x

        if player:
            self.speedy = -10
        else:
            self.speedy = 10

    def update(self):
        self.rect.y += self.speedy
        if self.rect.bottom < 0:
            all_sprites.remove(self)
            bullets.remove(self)
            self.kill()
        if self.rect.top > size[1]:
            all_sprites.remove(self)
            bullets.remove(self)
            self.kill()


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((30, 40))
        self.image.fill(green)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, size[0] - self.rect.width)
        self.rect.y = random.randrange(0, 15)
        self.speedx = random.randrange(-2, 3)
        self.speedy = random.randrange(1, 4)

    def update(self):
        self.rect.y += self.speedy
        self.rect.x += self.speedx
        if self.rect.x < 0:
            self.rect.x = 0
            self.speedx = random.randrange(1, 3)
        if self.rect.right > size[0]:
            self.rect.right = size[0]
            self.speedx = random.randrange(-2, 0)

        if self.rect.top > size[1]:
            self.rect.x = random.randrange(0, size[0] - self.rect.width)
            self.rect.y = random.randrange(0, 15)
            self.speedx = random.randrange(-2, 3)
            self.speedy = random.randrange(1, 4)

        if self.rect.colliderect(player):
            global game
            game = False

        global timer
        if timer == 10:
            bullet = Bullet(self.rect.centerx, self.rect.bottom + 10, False)
            all_sprites.add(bullet)
            bullets.add(bullet)



class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 40))
        self.image.fill(red)
        self.rect = self.image.get_rect()
        self.rect.centerx = size[0] / 2
        self.rect.bottom = size[1] - 10
        self.speedx = 0

    def update(self):
        self.rect.x += self.speedx
        self.speedx = 0

        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            self.speedx = -10
        if key[pygame.K_RIGHT]:
            self.speedx = 10

        if self.rect.left < 5:
            self.rect.left = 5
        if self.rect.right > size[0] - 5:
            self.rect.right = size[0] - 5

    def shoot(self):
        bullet = Bullet(self.rect.centerx, self.rect.top, True)
        all_sprites.add(bullet)
        bullets.add(bullet)

all_sprites= pygame.sprite.Group()
enemys = pygame.sprite.Group()
bullets = pygame.sprite.Group()


player = Player()
all_sprites.add(player)

for i in range(5):
    enemy = Enemy()
    all_sprites.add(enemy)
    enemys.add(enemy)

def check():
    global score
    global game
    for bullet in bullets:
        if bullet.rect.colliderect(player):
            game = False
        for enemy in enemys:
            if enemy.rect.colliderect(bullet):
                score += 1
                all_sprites.remove(enemy)
                all_sprites.remove(bullet)
                bullets.remove(bullet)
                enemys.remove(enemy)
                enemy.kill()
                bullet.kill()

                new_enemy = Enemy()
                all_sprites.add(new_enemy)
                enemys.add(new_enemy)

def print_score():
    style = pygame.font.SysFont(None, 50)
    text = style.render("Score: " + str(score), True, red)
    display.blit(text, (5, 5))

while game:
    clock.tick(FPS)
    timer += 1
    if timer > 100:
        timer = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.shoot()

    display.fill(white)
    all_sprites.update()
    check()
    print_score()
    all_sprites.draw(display)

    pygame.display.update()
