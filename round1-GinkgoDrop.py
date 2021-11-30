### 모듈 불러오기 ###
import pygame, sys, random, time
from pygame.locals import *

### 프로그램 기본 세팅 ###
pygame.init()
pygame.display.set_caption("통학러 푸앙이")
screen = pygame.display.set_mode((405, 650))   # 스크린 사이즈 405*650 (대략 10:16 비율)
clock = pygame.time.Clock()

### 이미지, 사운드 파일, 폰트 세팅 ###
puang_image = pygame.image.load("images/puang.png")
puang_image = pygame.transform.scale(puang_image, (95, 105))    # 푸앙이 이미지 사이즈 조절
ginkgo_image = pygame.image.load("images/ginkgo.png")               # 주의사항) png파일에 convert() 사용시 원치않는 이미지 배경이 생김
ginkgo_image = pygame.transform.scale(ginkgo_image, (50, 50))       # 은행열매 이미지 사이즈 조절
main = pygame.image.load("images/rough_images/main.png")
main = pygame.transform.scale(main, (405, 650))
intro01 = pygame.image.load("images/rough_images/intro01.png")
intro01 = pygame.transform.scale(intro01, (405, 650))
intro02 = pygame.image.load("images/rough_images/intro02.png")
intro02 = pygame.transform.scale(intro02, (405, 650))
intro03 = pygame.image.load("images/rough_images/intro03.png")
intro03 = pygame.transform.scale(intro03, (405, 650))
intro04 = pygame.image.load("images/rough_images/intro04.png")
intro04 = pygame.transform.scale(intro04, (405, 650))
intro05 = pygame.image.load("images/rough_images/intro05.png")
intro05 = pygame.transform.scale(intro05, (405, 650))
intro06 = pygame.image.load("images/rough_images/intro06.png")
intro06 = pygame.transform.scale(intro06, (405, 650))
game_start = pygame.image.load("images/rough_images/game_start.png")
game_start = pygame.transform.scale(game_start, (405, 650))
Round1_start = pygame.image.load("images/rough_images/round1_start.png")
Round1_start = pygame.transform.scale(Round1_start, (405, 650))
Round1_background = pygame.image.load("images/rough_images/round1_background.png")
Round1_background = pygame.transform.scale(Round1_background, (405, 650))
Round1_OVER = pygame.image.load("images/rough_images/round1_end.png")
Round1_OVER = pygame.transform.scale(Round1_OVER, (405, 650))

font = pygame.font.Font(None, 50)



### 변수 세팅 : 변수 선언 ###
time_last = 0
time_now = 0
menu = "main"
last_ginkgo_spawn_time = 0

### 클래스 세팅 : 클래스 생성 ###
class Ginkgo:                               # 은행열매 장애물
    def __init__(self):
        self.radius = 10
        self.x = random.randint(0+self.radius, 405-self.radius)     
        self.y = -60
        self.dy = random.randint(1, 2)              # x 방향 가속 설정
        self.dx = random.choice((-1, 1))*self.dy    # y 방향 가속 설정
    def move(self):
        self.y += self.dx 
        self.dy += 0.1
        self.y += self.dy
    def draw(self):
        screen.blit(ginkgo_image, (self.x, self.y))
    def bounce(self):           # 벽에 부딪혔을 때 튕겨나오도록 하는 부분
        if self.x < 0 or self.x > 405:
            self.dx *= -1
    def off_screen(self):       # 화면에서 사라진 인스턴스 삭제
        return self.y > 650

class Puang:
    def __init__(self):
        self.x = 155    # 푸앙이 초기 위치가 화면 중앙이 되도록 설정
        self.y = 540
    def move(self):
        if pressed_keys[K_LEFT] and self.x > 0:
            self.x -= 5
        if pressed_keys[K_RIGHT] and self.x < 310:  # 푸앙이 이미지 크기에 따라 푸앙이 x 한계 좌표 조절 *
            self.x += 5
    def draw(self):
        screen.blit(puang_image, (self.x, 540))     # 푸앙이 이미지 크기에 따라 푸앙이 y좌표 조절 *
    def hit_by(self, ginkgo):
        return pygame.Rect((self.x, self.y),(95, 105)).collidepoint(ginkgo.x, ginkgo.y)



### 인스턴스 세팅 : 인스턴스 생성 ###
ginkgos = []
puang = Puang()


### 게임 메인 루프 ###
while 1:
    clock.tick(60)                      # 스크린 프레임 레이트 설정 (60fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()                  # QUIT 버튼 클릭 여부 감지
    pressed_keys = pygame.key.get_pressed()
    
    if menu == "main":
        screen.blit(main, (0,0))
        txt = font.render("Start Game", True, (255,255,255))
        txt_x = 120
        txt_y = 526
        buttonrect = pygame.Rect((txt_x, txt_y), txt.get_size())
        pygame.draw.rect(screen, (255,0,0), buttonrect)
        screen.blit(txt, (txt_x, txt_y))
    if pygame.mouse.get_pressed()[0] and buttonrect.collidepoint(pygame.mouse.get_pos()):
        time_last = pygame.time.get_ticks()
        menu = "intro01"
    if menu == "intro01":
        time_now = pygame.time.get_ticks()
        screen.blit(intro01,(0,0))
    if time_now - time_last > 500:
        time_last = pygame.time.get_ticks()
        menu = "intro02"
    if menu == "intro02":
        time_now = pygame.time.get_ticks()
        screen.blit(intro02,(0,0))
    if time_now - time_last > 500:
        time_last = pygame.time.get_ticks()
        menu = "intro03"
    if menu == "intro03":
        time_now = pygame.time.get_ticks()
        screen.blit(intro03,(0,0))
    if time_now - time_last > 500:
        time_last = pygame.time.get_ticks()
        menu = "intro04"  
    if menu == "intro04":
        time_now = pygame.time.get_ticks()
        screen.blit(intro04,(0,0))
    if time_now - time_last > 500:
        time_last = pygame.time.get_ticks()
        menu = "intro05"
    if menu == "intro05":
        time_now = pygame.time.get_ticks()
        screen.blit(intro05,(0,0))
    if time_now - time_last > 500:
        time_last = pygame.time.get_ticks()
        menu = "intro06"
    if menu == "intro06":
        time_now = pygame.time.get_ticks()
        screen.blit(intro06,(0,0))
    if time_now - time_last > 500:
        time_last = pygame.time.get_ticks()
        menu = "game_start"
    if menu == "game_start":
        time_now = pygame.time.get_ticks()
        screen.blit(game_start,(0,0))
    if time_now - time_last > 500:
        time_last = pygame.time.get_ticks()
        menu = "round1_start"
     
        
    if menu == "round1_start":
        time_now = pygame.time.get_ticks()
        screen.blit(Round1_start,(0,0))
    if time_now - time_last > 500:
        time_last = pygame.time.get_ticks()
        menu = "round1_game"

    if menu == "round1_game":
        if time.time() - last_ginkgo_spawn_time > 0.5:       # 은행열매 장애물 생성 속도 조절(0.5초마다 생성)
            ginkgos.append(Ginkgo())
            last_ginkgo_spawn_time = time.time()

        screen.fill((255, 255, 255))
        screen.blit(Round1_background, (0,0))
        
        puang.move()
        puang.draw()
        
        i = 0
        while i < len(ginkgos):
            ginkgos[i].move()
            ginkgos[i].bounce()
            ginkgos[i].draw()
            if ginkgos[i].off_screen():
                del ginkgos[i]
                i -= 1
            i += 1

        for ginkgo in ginkgos:
            if puang.hit_by(ginkgo):
                screen.blit(Round1_OVER, (0,0))
                txt = font.render("Back to the Game", True, (255,255,255))
                txt_x = 55
                txt_y = 528
                buttonrect = pygame.Rect((txt_x, txt_y), txt.get_size())
                pygame.draw.rect(screen, (255,0,0), buttonrect)
                screen.blit(txt, (txt_x, txt_y))
            # 아무 조작이 없어도 게임이 재시작됨.
            #if pygame.mouse.get_pressed()[0] and buttonrect.collidepoint(pygame.mouse.get_pos()):
            #    menu = "round1_start"
           
                while 1:
                    for event in pygame.event.get():
                        if event.type == QUIT:
                            sys.exit()
                    pygame.display.update()

        pygame.draw.rect(screen, (234,234,234), [300, 0, 100, 60])
        screen.blit(font.render(str(int((pygame.time.get_ticks())/1000)), True, (0, 0, 0)), (325, 15))
    pygame.display.update()             # 스크린 업데이트(게임 루프 제일 하단에 *반드시* 위치해야 함)
