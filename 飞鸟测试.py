import pygame
import sys
from pygame.locals import *
from random import *

class Bird(pygame.sprite.Sprite):
    def __init__(self, image, position, speed):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load(image).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = position
        self.speed = speed

def main():
    pygame.init()

    babird_image = r"C:\Users\Administrator\temp\桃白白的旅行\鸟与其他\八哥(小).png"
    bluebird_image = r"C:\Users\Administrator\temp\桃白白的旅行\鸟与其他\蓝色鸟(小).png"
    redbird_image = r"C:\Users\Administrator\temp\桃白白的旅行\鸟与其他\红鸟(小).png"
    bg_image = r"C:\Users\Administrator\temp\桃白白的旅行\背景\树林.jpg"

#窗口设置
    bg_size = width, height = 1200, 500
    screen = pygame.display.set_mode(bg_size)
    pygame.display.set_caption('桃白白的旅行——小鸟测试')

    bg = pygame.image.load(bg_image).convert()
    
#鸟类生成
      
#八哥鸟
    babirds = []
    for i in range(2):
        position = randint(width, width+1000), randint(0, height-300)
        speed = [-randint(3, 6), 0]
        babird = Bird(babird_image, position, speed)
        babirds.append(babird)
        
#红鸟
    redbirds = []
    for i in range(2):
        position = randint(width, width+1000), randint(0, height-300)
        speed = [-randint(5, 8), 0]
        redbird = Bird(redbird_image, position, speed)
        redbirds.append(redbird)

#蓝鸟
    bluebirds = []
    for i in range(2):
        position = randint(width, width+1000), randint(0, height-300)
        speed = [-randint(2, 5), 0]
        bluebird = Bird(bluebird_image, position, speed)
        bluebirds.append(bluebird)

#鸟叫配置
    ba_sound = pygame.mixer.Sound(r"C:\Users\Administrator\temp\桃白白的旅行\音乐\八哥 (单).wav")       
    ba_sound.set_volume(0.2)
    red_sound = pygame.mixer.Sound(r"C:\Users\Administrator\temp\桃白白的旅行\音乐\红鸟(两声).wav")    
    red_sound.set_volume(0.2)
    blue_sound = pygame.mixer.Sound(r"C:\Users\Administrator\temp\桃白白的旅行\音乐\蓝鸟叫(两声).wav")
    blue_sound.set_volume(0.2)
    clock = pygame.time.Clock()
    ZFB = False
    running = True
    while running:
        
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()

            if event.type == KEYDOWN:
                if event.key == K_f:
                    running = False

                if event.key == K_TAB:
                    print('生成飞鸟')
                    ZFB = True

                else:
                    None

            if event.type == KEYUP:
                if event.key == K_TAB:
                    print('停止生成飞鸟')        
                    ZFB = False                
#刷新背景
        screen.blit(bg, (0, 0))


#生成飞鸟
        if ZFB == True:
            print("生成飞鸟通道打开")
            for i in range(1):
                position = randint(width, width+1000), randint(0, height-300)
                speed = [-randint(3, 6), 0]
                babird = Bird(babird_image, position, speed)
                babirds.append(babird)
        else:
            None
#刷新各种鸟
#八哥鸟

        for each in babirds:
            each.rect = each.rect.move(each.speed)
            screen.blit(each.image, each.rect)
            if each.rect.left <= 1200 and each.rect.left >= 1190:
                ba_sound.play()
#红鸟
        for each in redbirds:
            each.rect = each.rect.move(each.speed)
            screen.blit(each.image, each.rect)
            if each.rect.left <= 1200 and each.rect.left >= 1180:
                red_sound.play()
#蓝鸟
        for each in bluebirds:
            each.rect = each.rect.move(each.speed)
            screen.blit(each.image, each.rect)
            if each.rect.left <= 1200 and each.rect.left >= 1180:
                blue_sound.play()
        
        
        
        pygame.display.flip()
        clock.tick(30)


if __name__ == "__main__":
    main()