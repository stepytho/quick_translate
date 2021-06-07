import pygame
import sys

pygame.init()


size = width, height = 1000, 600

bg = (0, 255, 255)
clock = pygame.time.Clock()


#指定窗口
screen = pygame.display.set_mode(size)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            
            sys.exit()
            print('检测到退出键')


    screen.fill(bg)

    pygame.display.flip()