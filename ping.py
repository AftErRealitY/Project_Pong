from pygame import *
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, width, height ):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(100,100))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.height = height
        self.width = width
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def update_l(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < 500:
            self.rect.y += self.speed
    def update_r(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < 500:
            self.rect.y += self.speed

win_width = 600
win_height = 500
back = (120, 219, 226)

window = display.set_mode((win_width,win_height))
display.set_caption('ПИНПОНГ')
window.fill(back)


finish = False
game = True
clock = time.Clock()
FPS = 60

player1 = Player('player1.png',30,250, 10, 50,100)
player2 = Player('player2.png',500,250, 10, 50,100)
ball = GameSprite('ball.png',300,250, 7, 50,50)

speed_x = 3
speed_y = 3

font.init()
font = font.Font(None, 40)
lose1 = font.render('PLAYER 1 ELEMINATED!', True, (255,0,0))
lose2 = font.render('PLAYER 2 ELEMINATED!', True, (255,0,0))
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.fill(back)
        player1.update_l()
        player2.update_r()
        ball.rect.x += speed_x
        ball.rect.y += speed_y

        if sprite.collide_rect(player1, ball) or sprite.collide_rect(player2, ball):
            speed_x *= -1
            speed_y *= 1

        if ball.rect.y >win_height - 55 or ball.rect.y <0:
            speed_y *= -1

        if ball.rect.x < 0:
            finish = True
            window.blit(lose1, (200,200))

        if ball.rect.x > win_width:
            finish = True
            window.blit(lose2, (200,200))
        player1.reset()
        player2.reset()
        ball.reset()

        clock.tick(FPS)
        display.update()