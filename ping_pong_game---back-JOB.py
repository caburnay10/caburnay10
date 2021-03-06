# from turtle import Screen
import pygame
import sys
import math
import time


class MyBall(object):
    def __init__(self,x,y,width,height,sx,sy,colour):
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.sx=sx
        self.sy=sy
        self.colour=colour
    def render(self,screen):
        pygame.draw.ellipse(screen,self.colour,self.rect)
    @property
    def rect(self):
        return pygame.Rect(self.x,self.y,self.width,self.height)
    def update(self):
        self.x +=self.sx
        self.y += self.sy

class MyPaddle(object):
    def __init__(self,x,y,width,height,speed,colour):
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.sx=0
        self.speed=speed
        self.colour=colour
    def render(self,screen):
        pygame.draw.rect(screen,self.colour,self.rect)
    def update(self):
        self.x += self.sx
    def my_key_handler(self,event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.sx= -self.speed
            elif event.key == pygame.K_RIGHT:
                self.sx=self.speed
        elif event.key in (pygame.K_LEFT,pygame.K_RIGHT):
            self.sx=0
            
class PingPong(object):
    COLOURS={'White':(255,255,255),
             'Black':(0,0,0),
             'Goldenrod':(218,165,32)}
    count=0
    def __init__(self):
        pygame.mixer.pre_init(44100,16,2,4069)
        pygame.init()
        (WIDTH,HEIGHT)=(300,400)
        self.screen=pygame.display.set_mode((WIDTH,HEIGHT))
        pygame.display.set_caption('ping pong game')
        self.ball=MyBall(5,5,50,50,5,5,PingPong.COLOURS['White'])
        self.paddle=MyPaddle(WIDTH/2,HEIGHT-50,100,10,3,PingPong.COLOURS['White'])
        self.score = 0
        pygame.mixer.music.load("backgroundmusic.mp3")
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1)
        
    def playGame(self):
        clock = pygame.time.Clock()
        while True:
            clock.tick(50)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type in (pygame.KEYDOWN,pygame.KEYUP):
                    self.paddle.my_key_handler(event)
            self.my_collision_handler()
            self.draw_shape()
            
    def my_collision_handler(self):
        if self.ball.rect.colliderect(self.paddle.rect):
            self.ball.sy*=-1
            self.score+=1
        if self.ball.x + self.ball.width >=self.screen.get_width():
            self.ball.sx=-(math.fabs(self.ball.sx))
        elif self.ball.x <=0:
            self.ball.sx=math.fabs(self.ball.sx)
        
        if self.ball.y + self.ball.height >= self.screen.get_height():
            if PingPong.count==0:
                pygame.mixer.music.stop()
                pygame.mixer.music.load('loss.mp3')
                pygame.mixer.music.set_volume(1)
                pygame.mixer.music.play()
                PingPong.count+=1
            else:
                pygame.mixer.stop()
                
            time.sleep(5)
            pygame.quit()
            sys.exit()
            
        elif self.ball.y <= 0:
            self.ball.sy=math.fabs(self.ball.sy)
        if self.paddle.x + self.paddle.width >= self.screen.get_width():
            self.paddle.x = self.screen.get_width()-self.paddle.width
        elif self.paddle.x <=0:
            self.paddle.x = 0
    def draw_shape(self):
          self.screen.fill(PingPong.COLOURS['Black'])
          font = pygame.font.Font(None,48)
          score_text = font.render('Score:'+ str(self.score),True,PingPong.COLOURS['Goldenrod'])  
          self.screen.blit(score_text(0,0))
          self.ball.update()
          self.ball.render(self.screen)
          self.paddle.update()
          self.paddle.render(self.screen)
          pygame.display(screen)

if __name__ == '__main__':
    obj = PingPong()
    obj.playGame()
            
            