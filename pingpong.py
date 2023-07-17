from pygame import *
from random import randint 

WEIGHT = 600
HEIGHT = 500
FPS = 60 



run = True

font.init()
font_text = font.Font(None,36)
lose1 = font_text.render('PLAYER 1 LOSE',True,(100,0,0))
lose2 = font_text.render('PLAYER 2 LOSE',True,(100,0,0))


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



class Ball(GameSprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed,speed_y):
        super().__init__(player_image, player_x, player_y, size_x, size_y, player_speed)
        self.speed_y = speed_y
    def update(self):
        self.rect.x += self.speed
        self.rect.y += self.speed_y
        if self.rect.y >= HEIGHT - 50 or self.rect.y <= 0:
            self.speed_y *= -1
        if sprite.collide_rect(rocketka1,ball) or sprite.collide_rect(rocketka2, ball):
            self.speed *= -1
            
        


rocketka1 = Player('racket.png', 30, 200, 50, 150, 4)
rocketka2 = Player('racket.png', 520, 200, 50, 150, 4)
ball = Ball('tenis_ball.png', 200, 200, 50, 50, 2,2)

finish = False

while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
        elif e.type == MOUSEBUTTONDOWN and e.button == 1:
            color = True
        elif e.type == MOUSEBUTTONUP and e.button == 1:
            color = False
    if color:
        background = generate_color()
    if not finish:
        window.fill(background)
        rocketka1.reset()
        rocketka1.update_1()
        rocketka2.reset()
        rocketka2.update_2()
        ball.reset()
        ball.update()
        if ball.rect.x <= 50:
            finish = True
            window.blit(lose1, (200,250))
        if ball.rect.x >= WEIGHT-50:
            finish = True
            window.blit(lose2, (200,250))
    else:
        finish = False
        ball = Ball('tenis_ball.png', 200, 200, 50, 50, 2,2)
        ball.reset()
        ball.update()
        time.delay(3000)
    display.update()
    clock.tick(FPS)