import getcwd
import pygame
import time
global kdown
kdown=False
disappear=(0,0,0,0)
class create:
    def __init__(self):
        global back,front,left,left_run,right,right_run,back_run,back_run_flip,front_run,front_run_flip,brect,frect,lrect,lrrect,rrect,rrrect,brrect,frrect,brfrect,frfrect,c_pos
        c_pos=[925,520]
        back=pygame.image.load(getcwd.Getcwd.get('character_back.png'))
        front=pygame.image.load(getcwd.Getcwd.get('character_front.png'))
        
        left=pygame.image.load(getcwd.Getcwd.get('character_left.png'))
        left_run=pygame.image.load(getcwd.Getcwd.get('character_left_run.png'))
        
        right=pygame.transform.flip(left,True,False)
        right_run=pygame.transform.flip(left_run,True,False)
        
        back_run=pygame.image.load(getcwd.Getcwd.get('character_back_run.png'))
        back_run_flip=pygame.transform.flip(back_run,True,False)
        
        front_run=pygame.image.load(getcwd.Getcwd.get('character_front_run.png'))
        front_run_flip=pygame.transform.flip(front_run,True,False)

        back=pygame.transform.scale(back, (70, 80))
        front=pygame.transform.scale(front, (70, 80))

        left=pygame.transform.scale(left, (70, 80))
        left_run=pygame.transform.scale(left_run, (70, 80))

        right=pygame.transform.scale(right, (70, 80))
        right_run=pygame.transform.scale(right_run, (70, 80))

        back_run=pygame.transform.scale(back_run, (70, 80))
        back_run_flip=pygame.transform.scale(back_run_flip, (70, 80))
        
        front_run=pygame.transform.scale(front_run, (70, 80))
        front_run_flip=pygame.transform.scale(front_run_flip, (70, 80))
        
        brect=back.get_rect()
        frect=front.get_rect()
        
        lrect=left.get_rect()
        lrrect=left_run.get_rect()

        rrect=right.get_rect()
        rrrect=right_run.get_rect()
        
        brrect=back_run.get_rect()
        brfrect=back_run_flip.get_rect()
        
        frrect=front_run.get_rect()
        frfrect=front_run_flip.get_rect()
        



