from pygame import *
from random import randint

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
#Ball = GameSprite("ball.jpg", 350, 450, 3)
#font1 = font.SysFont("Arial", 36)
#font2 = font.SysFont("Arial", 60)
clock = time.Clock()
FPS = 60
game = True 

while game:
            
    for e in event.get():
        if e.type == QUIT:
            game =False
                   
    window.blit(background, (0,0))
    RacketL.reset()
    RacketL.update_L()
    RacketR.reset()
    RacketR.update_R()
    #Ball.reset()
    #aBall.update()

#text_schet = font1.render(
#"Счёт:" + str(score), 1, (255, 255, 255)Это не это нужно поменять        
                                
#if sprite.spritecollide(ship, monsters, False) or lost >= 3:
#text_lose = font2.render(
       
        
                  
    
    clock.tick(FPS)
    display.update()