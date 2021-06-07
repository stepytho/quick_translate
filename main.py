import pygame
import sys
from pygame.locals import *
from random import *

#鸟类
class Bird(pygame.sprite.Sprite):
    def __init__(self, image, position, speed):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load(image).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = position
        self.speed = speed
        self.mask = pygame.mask.from_surface(self.image)

    def move(self):
        self.rect = self.rect.move(self.speed)


#洞洞波类
class Dongdongbo(pygame.sprite.Sprite):
    def __init__(self, image, position, speed):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load(image).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = position
        self.speed = speed
        

    def move(self):
        self.rect = self.rect.move(self.speed)


pygame.init()

#设置窗口
size = width, height = 1200, 500
clock = pygame.time.Clock()

#指定窗口
screen = pygame.display.set_mode(size)

#设置窗口标题
pygame.display.set_caption("桃白白的旅行")

#加载图片
dongdongbo_image = r'C:\Users\Administrator\temp\桃白白的旅行\桃白白\洞洞波加长版.png'
flytao = pygame.image.load(r'C:\Users\Administrator\temp\桃白白的旅行\桃白白\驭柱飞行（小）.png').convert_alpha()
flytao_f = pygame.image.load(r'C:\Users\Administrator\temp\桃白白的旅行\桃白白\发射（小）.png').convert_alpha()
bg = pygame.image.load(r"C:\Users\Administrator\temp\桃白白的旅行\背景\树林长.jpg").convert()

#关键开关
DB = False
FB = True
ZFB = False

#鸟类生成     
babird_image = r"C:\Users\Administrator\temp\桃白白的旅行\鸟与其他\八哥(小).png"
bluebird_image = r"C:\Users\Administrator\temp\桃白白的旅行\鸟与其他\蓝色鸟(小).png"
redbird_image = r"C:\Users\Administrator\temp\桃白白的旅行\鸟与其他\红鸟(小).png"

#八哥鸟
babirds = []
bagroup = pygame.sprite.Group()

#红鸟
redbirds = []
redgroup = pygame.sprite.Group()
#蓝鸟
bluebirds = []
bluegroup = pygame.sprite.Group()

#鸟叫配置
ba_sound = pygame.mixer.Sound(r"C:\Users\Administrator\temp\桃白白的旅行\音乐\八哥 (单).wav")       
ba_sound.set_volume(0.2)
red_sound = pygame.mixer.Sound(r"C:\Users\Administrator\temp\桃白白的旅行\音乐\红鸟(两声).wav")    
red_sound.set_volume(0.2)
blue_sound = pygame.mixer.Sound(r"C:\Users\Administrator\temp\桃白白的旅行\音乐\蓝鸟叫(两声).wav")
blue_sound.set_volume(0.2)
clock = pygame.time.Clock()


#音乐音效的设置
#背景音
pygame.mixer.init()
pygame.mixer.music.load(r'C:\Users\Administrator\temp\桃白白的旅行\音乐\时髦的龟仙人 (cut).wav')
pygame.mixer.music.set_volume(0.05)
pygame.mixer.music.play()

#音效
flashbo = pygame.mixer.Sound(r'C:\Users\Administrator\temp\桃白白的旅行\音乐\冲击波.wav')
flashbo.set_volume(0.4)


#定义移动速度
speed = [0, 0]
bg_speed = [-5, 0]

#获取图形的位置矩形flytao.get_rect()
position = pygame.Rect(100, 100, 100, 116)
DBposition = position.left+80, position.top+7
bg1_position = pygame.Rect(0, 0, 2400, 562)
bg2_position = pygame.Rect(2400, 0, 2400, 562)

#洞洞波类实例

dongdongbo = Dongdongbo(dongdongbo_image, DBposition, speed)


while True:

#时间控制
    q = clock.get_time()    
#背景音乐循环
    music_time = pygame.mixer.music.get_pos()
    #print(music_time)
    
    if music_time > 26810:
        print("------音乐循环------")
        pygame.mixer.music.play()

    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
            
#按键下的控制
        elif event.type == KEYDOWN:
            if event.key == K_LEFT:
                speed = [-20, 0]
                #dongdongbo.speed = speed
                print('检测到：左键')
            elif event.key == K_RIGHT:
                speed = [20, 0]
                #dongdongbo.speed = speed
                print('检测到：右键')
            elif event.key == K_UP:
                speed = [0, -20]
                #dongdongbo.speed = speed
                print('检测到：上键')
            elif event.key == K_DOWN:
                speed = [0, 20]
                
                print('检测到：下键')
            
#退出    
            elif event.key == K_ESCAPE:
                print('检测到：退出键')
                sys.exit()
            else:
                speed = [0, 0]
                dongdongbo.speed = speed

#背景音控制(R键重播背景音)
            if event.key == K_r:
                print('重播背景音乐')
                pygame.mixer.music.play()
            
            DBposition = position.left+80, position.top+7
            dongdongbo.rect.left, dongdongbo.rect.top = DBposition
            dongdongbo.speed = speed
            position = position.move(speed)
            dongdongbo.move()
#特效
            if event.key == K_SPACE:
                print('洞洞波放')
                DB = True
                flashbo.play()
                
                if FB == True:
                    print("叫声开")
                    #ba_sound.play()
                else:
                    print("叫声关")

            if event.key == K_f: 
                print("飞鸟来")
                FB = True 

            if event.key == K_g:
                print('飞鸟去')
                FB = False
#造飞鸟控制            
            if event.key == K_TAB:
                print('生成飞鸟')
                ZFB = True
#按键起的控制
        elif event.type == KEYUP:
            if event.key == K_SPACE:
                print('洞洞波收')
                DB = False
            if event.key == K_TAB:
                print('停止生成飞鸟')        
                ZFB = False

               
    #填充背景，背景循环
    bg1_position = bg1_position.move(bg_speed)
    bg2_position = bg2_position.move(bg_speed)
    #print(bg1_position)
    #print(bg2_position)
    if bg1_position.left == -2400:
        bg1_position.left = 2400
    if bg2_position.left == -2400:
        bg2_position.left = 2400
    
    screen.blit(bg, bg1_position)
    screen.blit(bg, bg2_position)
    #更新人物图像
    screen.blit(flytao, position)
    
    #洞洞波特效
    if DB == True:
        screen.blit(bg, bg1_position)
        screen.blit(bg, bg2_position)
        screen.blit(dongdongbo.image, dongdongbo.rect)
        screen.blit(flytao_f, position)
    else:
        screen.blit(bg, bg1_position)
        screen.blit(bg, bg2_position)
        screen.blit(flytao, position)

#生产飞鸟
    if ZFB == True:
        print('生成飞鸟通道打开')
        #八哥
        for i in range(1):
            bird_position = randint(width, width+1000), randint(0, height-300)
            speed = [-randint(3, 6), 0]
            babird = Bird(babird_image, bird_position, speed)
            babirds.append(babird)
            bagroup.add(babird)
        #红鸟
        for i in range(2):
            bird_position = randint(width, width+1000), randint(0, height-300)
            speed = [-randint(5, 8), 0]
            redbird = Bird(redbird_image, bird_position, speed)
            redbirds.append(redbird)
            redgroup.add(redbird)
        #蓝鸟
        for i in range(1):
            bird_position = randint(width, width+1000), randint(0, height-300)
            speed = [-randint(2, 5), 0]
            bluebird = Bird(bluebird_image, bird_position, speed)
            bluebirds.append(bluebird)
            bluegroup.add(bluebird)
        ZFB = False


#刷新各种鸟
    if FB == True:

#八哥鸟
        for each in babirds:
            each.move()
            screen.blit(each.image, each.rect)
            if each.rect.left <= 1200 and each.rect.left >= 1190:
                pass
                #ba_sound.play()
        for each in bagroup:
            bagroup.remove(each)

            if pygame.sprite.collide_rect(each, dongdongbo):
                each.speed[0] = each.speed[0]-1
                each.speed[1] = 10
                print('有一只鸟落地了，位置是：', each.rect)
                ba_sound.play()

            bagroup.add(each)
#红鸟
        for each in redbirds:
            each.move()
            screen.blit(each.image, each.rect)
            if each.rect.left <= 1200 and each.rect.left >= 1180:
                pass
                #red_sound.play()
        for each in redgroup:
            redgroup.remove(each)

            if pygame.sprite.collide_rect(each, dongdongbo):
                each.speed[0] = each.speed[0]-1
                each.speed[1] = 10
                print('有一只鸟落地了，位置是：', each.rect)
                red_sound.play()
            
            redgroup.add(each)
        
#蓝鸟
        for each in bluebirds:
            each.move()
            screen.blit(each.image, each.rect)
            if each.rect.left <= 1200 and each.rect.left >= 1180:
                pass
                #blue_sound.play()

        for each in bluegroup:
            bluegroup.remove(each)

            if pygame.sprite.collide_rect(each, dongdongbo):
                each.speed[0] = each.speed[0]-1
                each.speed[1] = 10
                print('有一只鸟落地了，位置是：', each.rect)
                blue_sound.play()
            
            bluegroup.add(each)
        
    else:
        None
    
    #更新界面(让内存的数据显示)
    pygame.display.flip()
    #延迟10毫秒
    pygame.time.delay(5)
    #控制速度（帧率）
    clock.tick(100)