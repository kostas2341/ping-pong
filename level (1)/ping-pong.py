from typing import Any
from pygame import*

class GameSprite(sprite.Sprite):
    # конструктор класу
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed, ):
        # викликаємо конструктор класу (Sprite):
        sprite.Sprite.__init__(self)
 
        # кожен спрайт повинен зберігати властивість image - зображення
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed

        # кожен спрайт повинен зберігати властивість rect - прямокутник, в який він вписаний
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    # метод, що малює героя у вікні
    def reset(self):
        win.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    # метод для керування спрайтом стрілками клавіатури
    def update(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed

    def update_1(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 80:
            self.rect.y += self.speed



win_width = 1000
win_height = 800

imgplayer_1 = "blue.png"
background = transform.scale(image.load("back.png"), (win_width, win_height))  

win = display.set_mode((win_width, win_height))

player_1 = Player(imgplayer_1, 5, win_height - 80, 65, 65, 4)
player_2 = Player(imgplayer_1, 925, win_height - 80, 65, 65, 4)
ball = GameSprite("ball.png", 150, 150, 65, 65, 0)

font.init()
font1 = font.Font(None, 80)
lose_1 = font1.render("Грвець 2 переміг", True, (255, 255, 255))
lose = font1.render("Грвець 1 переміг", True, (255, 255, 255))

speed_x = 3
speed_y = 3

clock = time.Clock() 
FPS = 60

run = True
finish = False

while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
        
    if finish != True:
        win.blit(background,(0, 0))
        player_1.reset()
        player_1.update()
        
        player_2.reset()
        player_2.update_1()

        ball.reset()
        

        ball.rect.x += speed_x
        ball.rect.y += speed_y

        if ball.rect.y > win_height-65 or ball.rect.y < 0:
            speed_y *= -1
        if sprite.collide_rect(player_1, ball) or sprite.collide_rect(player_2, ball):
            speed_x *= -1

        if ball.rect.x <0:
            win.blit(lose, (200, 200))
        
        if ball.rect.x >1000:
            win.blit(lose_1, (200, 200))
        display.update()
    clock.tick(FPS)