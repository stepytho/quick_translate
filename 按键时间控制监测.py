import pygame
import sys
from pygame.locals import *

pygame.init()
size = width, height = 400, 300
clock = pygame.time.Clock()

#指定窗口
screen = pygame.display.set_mode(size)

#设置窗口标题
pygame.display.set_caption("检测按空格的时间")

time_down = 0.0
time_elapsed = 0.0
key = 0
while True:
    
    for ev in pygame.event.get():
        if ev.type == QUIT:
            sys.exit()

        elif ev.type == KEYDOWN:
            if ev.key == K_SPACE:
                time_down = pygame.time.get_ticks()
        elif ev.type == KEYUP:
            if ev.key == K_SPACE:
                key += 1
                time_elapsed = (pygame.time.get_ticks() - time_down)/1000.0
                print("number: ", key, "duration: ", time_elapsed)
    
    clock.tick()
    pygame.display.update()