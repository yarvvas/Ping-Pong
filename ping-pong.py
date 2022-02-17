from pygame import *
from random import randint
font.init()
win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))

display.set_caption("Пинг-Понг")
img_back = "fon.jpg"
background = transform.scale(image.load(img_back), (win_width, win_height))

class GameSprite(sprite.Sprite):
    
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
       # каждый спрайт должен хранить свойство image - изображение
        self.image = image.load(player_image) #transform.scale(image.load(player_image), (50, 100))
        self.speed = player_speed
       # каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
    def update(self):
        self.rect.y += self.speed
        self.rect.x += self.speed
        
        #if self.rect.y >= 450:
            #self.rect.y =  -self.rect.y
 
class Ball(GameSprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        
       # каждый спрайт должен хранить свойство image - изображение
        self.image = transform.scale(image.load(player_image), (50, 50))
        self.speed = player_speed
       # каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
class Player(GameSprite):
    def update_L(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y >15:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 375:
            self.rect.y += self.speed
    def update_R(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y >15:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 375:
            self.rect.y += self.speed

RacketL = Player("racket.jpg", 20, 350, 10)
RacketR = Player("racket.jpg", 600, 350, 10)
Ball = Ball("ball2.png", 350, 450, 3)
font1 = font.SysFont(None, 60)

lose1 = font1.render(
"Player 1 lose", 1, (255, 25, 25))        
lose2 = font1.render(
"Player 2 lose", 1, (255,25, 25))                               
#if sprite.spritecollide(ship, monsters, False) or lost >= 3:
#text_lose = font2.render(
clock = time.Clock()
FPS = 60
game = True 
finish = False
speed_x = 3
speed_y = 3
schetL = 0
schetR = 0
score = font1.render(
    "Счёт:"+str(schetL)+"-"+str(schetR), 1, (255, 255, 255))
while game:
            
    for e in event.get():
        if e.type == QUIT:
            game =False
                   
    window.blit(background, (0,0))
    RacketL.reset()
    RacketL.update_L()
    RacketR.reset()
    RacketR.update_R()
    Ball.reset()
    if finish != True:
        Ball.rect.x+= speed_x
        Ball.rect.y+=speed_y
    if Ball.rect.y > win_height-50 or Ball.rect.y <1:
        speed_y*=-1
    if sprite.collide_rect(RacketL, Ball):
        speed_x *=-1
        schetL+=1
    if sprite.collide_rect(RacketR, Ball):
        speed_x *=-1
        schetR+=1
    if Ball.rect.x<0 and finish != True:
        schetR+=1
        window.blit(lose1, (250, 250))
        finish = True
    if Ball.rect.x<0 and finish == True:       
        window.blit(lose1, (250, 250))
        
    if Ball.rect.x>win_width and finish != True:
        schetL+=1
        window.blit(lose2, (250, 250))
        finish = True
    if Ball.rect.x>win_width and finish == True:       
        window.blit(lose2, (250, 250))
    score = font1.render(
        "Счёт:"+str(schetL)+"-"+str(schetR), 1, (255, 255, 255))
    window.blit(score, (250,30))
        
                  
    
    clock.tick(FPS)
    display.update()