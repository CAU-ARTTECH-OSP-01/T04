### 모듈 불러오기 ###
import pygame, sys, random, time
from pygame.locals import *

### 프로그램 기본 세팅 ###
pygame.init()
pygame.display.set_caption("통학러 푸앙이")
screen = pygame.display.set_mode((405,650))
clock = pygame.time.Clock()

### 이미지, 사운드 파일, 폰트 세팅 ###
ginkgo_image = pygame.image.load("images/Ginkgo.png").convert()

### 변수 세팅 : 변수 선언 ###
last_ginkgo_spawn_time = 0

### 클래스 세팅 : 클래스 생성 ###
class Ginkgo:                                       # 은행 열매 클래스 
    def __init__(self):
        self.x = random.randint(20,630)             # 은행열매 픽셀 20
        self.y = -60
        self.dy = random.randint(1,2)               # y 방향 가속 설정
        self.dx = random.choice((-1,1))*self.dy     # x 방향 가속 설정

    def move (self):
        self.y += self.dx
        self.dy += 0.1
        self.y += self.dy

    def draw(self):
        screen.blit(ginkgo_image,(self.x,self.y))   # 은행열매 이미지 스크린으로 전송 

    def bounce(self):           # 벽에 부딪혔을 때 튕겨나오도록 하는 부분 
        if self.x < 0 or self.x > 405:
            self.dx *= -1

    def off_screen(self):       # 화면에서 사라진 인스턴스 삭제 
        return self.y > 650

### 인스턴스 세팅 : 인스턴스 생성 ###
ginkgos = []

### 게임 메인 루프 ###
while 1:
    clock.tick(60)                      # 스크린 프레임 레이트 설정 (60fps)           
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()                  # QUIT 버튼 클릭 여부 감지 
    if time.time() - last_ginkgo_spawn_time > 0.5:  # 은행열매 장애물 생성 속도 조절 (작을 수록 생성속도 up)
        ginkgos.append(Ginkgo())
        last_ginkgo_spawn_time = time.time()

    screen.fill((255,255,255))

    i = 0
    while i < len(ginkgos):
        ginkgos[i].move()
        ginkgos[i].bounce()
        ginkgos[i].draw()
        if ginkgos[i].off_screen():
            del ginkgos[i]
            i -= 1
        i += 1

    pygame.display.update()             # 스크린 업데이트 (게임 메인 루프 제일 하단에 *반드시* 위치해야함)
        
