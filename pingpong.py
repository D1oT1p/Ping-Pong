from pygame import *
from random import randint 

WEIGHT = 600
HEIGHT = 500
FPS = 60 



run = True




def generate_color():
    return (randint(0,255),randint(0,255),randint(0,255))

background = generate_color()
window = display.set_mode((WEIGHT,HEIGHT))
display.set_caption('PING-PONG')
clock = time.Clock()

color = False



class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
 
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_1(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 350:
            self.rect.y += self.speed
    def update_2(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 350:
            self.rect.y += self.speed 

rocketka1 = Player('racket.png', 30, 200, 50, 150, 4)
rocketka2 = Player('racket.png', 520, 200, 50, 150, 4)
ball = GameSprite('tenis_ball.png', 200, 200, 50, 50, 4)

while run:
    window.fill(background)
    rocketka1.reset()
    rocketka1.update_1()
    rocketka2.reset()
    rocketka2.update_2()
    ball.reset()
    display.update()
    clock.tick(FPS)
    for e in event.get():
        if e.type == QUIT:
            run = False
        elif e.type == MOUSEBUTTONDOWN and e.button == 1:
            color = True
        elif e.type == MOUSEBUTTONUP and e.button == 1:
            color = False
    if color:
        background = generate_color()