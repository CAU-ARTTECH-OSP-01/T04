### 모듈 불러오기 ###
import pygame, sys, random
from pygame.locals import *

### 프로그램 기본 세팅 ###
pygame.init()

size = [365, 670]                        # 스크린 사이즈 405*650 (대략 10:16 비율)
screen = pygame.display.set_mode(size) 

title = "통학러 푸앙이"
pygame.display.set_caption(title)

clock = pygame.time.Clock()


### 이미지, 사운드 파일, 폰트 세팅 ###

first_image = pygame.image.load("D:\git\T04\source\start_bg.png").convert()

button_image = pygame.image.load("D:\git\T04\source\start_button.png").convert()


### 변수 세팅 : 변수 선언 ###

### 클래스 세팅 : 클래스 생성 ###
class BG :                              #이미지 생성
    def __init__(self) :
        self.x = 1
        self.y = 1
    def draw(self) :
        screen.blit(first_image,(self.x,self.y))

class Button :                              # 시작 버튼 이미지 생성
    def __init__(self) :
        self.x = 32
        self.y = 500
    def draw(self) :
        screen.blit(button_image,(self.x,self.y))

### 인스턴스 세팅 : 인스턴스 생성 ###

B_G = BG()
button = Button()

### 게임 메인 루프 ### 
while 1:
    clock.tick(60)                      # 스크린 프레임 레이트 설정 (60fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()                  # QUIT 버튼 클릭 여부 감지
    
    screen.fill((255,255,255))          #스크린색 White
    B_G.draw()                          #바탕 이미지 생성
    button.draw()                       #버튼 이미지 생성
    xpos = 50 
    
    pressed_keys = pygame.key.get_pressed()   #키보드 좌,우 감지
    if pressed_keys[K_RIGHT]:
        xpos += 1 
    if pressed_keys [K_LEFT]:
        xpos -= 1 
   
 

    






    pygame.display.update()             # 스크린 업데이트(게임 루프 제일 하단에 *반드시* 위치해야 함)
