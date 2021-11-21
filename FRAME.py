### 모듈 불러오기 ###
import pygame, sys, random
from pygame.locals import *

### 프로그램 기본 세팅 ###
pygame.init()
pygame.display.set_caption("통학러 푸앙이")
screen = pygame.display.set_mode((405, 650))   # 스크린 사이즈 405*650 (대략 10:16 비율)
clock = pygame.time.Clock()

### 이미지, 사운드 파일, 폰트 세팅 ###


### 변수 세팅 : 변수 선언 ###


### 클래스 세팅 : 클래스 생성 ###


### 인스턴스 세팅 : 인스턴스 생성 ###



### 게임 메인 루프 ###
while 1:
    clock.tick(60)                      # 스크린 프레임 레이트 설정 (60fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()                  # QUIT 버튼 클릭 여부 감지
 






    pygame.display.update()             # 스크린 업데이트(게임 루프 제일 하단에 *반드시* 위치해야 함)
