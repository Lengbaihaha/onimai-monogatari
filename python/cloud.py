import pygame
import getcwd
import random
import time
disappear=(0,0,0,0)
speedx=[-random.randint(1,5),-random.randint(1,5)]
speed1=[speedx[0],0]
speed2=[speedx[1],0]
class create:
    def __init__(l,bgc,self):
        global cloud1,cloud2,c1rect,c2rect
        cloud1=pygame.image.load(getcwd.Getcwd.get('cloud1.png'))
        c1rect=cloud1.get_rect()
        cloud2=pygame.image.load(getcwd.Getcwd.get('cloud2.png'))
        c2rect=cloud2.get_rect()
        c1rect.x=random.randint(0,1820)
        c1rect.y=random.randint(0,200)
        c2rect.x=random.randint(0,1820)
        c2rect.y=random.randint(0,200)
        self.blit(cloud1,c1rect)
        self.blit(cloud2,c2rect)
        if c1rect.y==c2rect.y:
            cloud2.fill(disappear)
            c2rect.x=random.randint(0,1820)
            c2rect.y=random.randint(50,260)+100
            self.blit(cloud2,c2rect)
        
        if abs(c1rect.x - c2rect.x)<=200:
            c2rect.x=random.randint(200,1820)-400
            c2rect.y=random.randint(50,260)
            self.blit(cloud2,c2rect)
class move:
    def __init__(l,self):
            global c1rect,cloud1
            c1rect=c1rect.move(speed1[0],speed1[1])
            self.blit(cloud1,c1rect)
            global c2rect,cloud2
            c2rect=c2rect.move(speed2[0],speed2[1])
            self.blit(cloud2,c2rect)
            if c1rect.right<=0:
                c1rect.x=1920
                c1rect.y=random.randint(0,200)
            if c2rect.right<=0:
                c2rect.x=1920
                c2rect.y=random.randint(0,200)
