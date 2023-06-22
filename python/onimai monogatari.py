import getcwd
import pygame
import sys
import os
import cloud
import characters
size=width,height=1920,1080
bgc=(118,215,234)
def intialize ():
    pygame.init()
    global screen
    screen=pygame.display.set_mode(size)
    pygame.display.set_caption("onimai monogatari")
    icon=pygame.image.load(getcwd.Getcwd.get('icon.jpg'))
    pygame.display.set_icon(icon)

def main ():
    cloud.create(bgc,screen)
    characters.create()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        screen.fill(bgc)
        cloud.move(screen)
        pygame.display.update()
        
intialize()
main()
