### 모듈 불러오기 ###
import pygame, sys, random, time
from pygame.locals import *
import image
from image import *

### 프로그램 기본 세팅 ###
pygame.init()
pygame.display.set_caption("통학러 푸앙이")
screen = pygame.display.set_mode((405,650))
clock = pygame.time.Clock()

### 이미지, 사운드 파일, 폰트 세팅 ###
puang_left = pygame.transform.flip(puang_walk, True, False)
puang_right = puang_walk

ginkgo_image = pygame.image.load("images/obstacle/round01/ginkgo.png")

font = pygame.font.SysFont("PFStardust", 50, True) # pygame.font.SysFont(font name, size, bold = False, italic = False)
#text = font.render("Game Start!", False, (0,0,0)) # render(Text, antialias, color, background = None)
#screen.blit(text,(100,100))

### 변수 세팅 : 변수 선언 ###
time_last = 0
time_now = 0
menu = "main"
last_spawn_time = 0
start_time = time.time()


### 클래스 세팅 : 클래스 생성 ###
class Ginkgo:                                       # 은행 열매 클래스 
    def __init__(self):
        self.x = random.randint(20,630)             # 은행열매 픽셀 20
        self.y = -60
        self.dy = random.randint(1,2)               # y 방향 가속 설정
        

    def move (self):
        self.dy += 0.1
        self.y += self.dy

    def draw(self):
        screen.blit(ginkgo_image, (self.x, self.y))

    def off_screen(self):       # 화면에서 사라진 인스턴스 삭제 
        return self.y > 650

class Puang: # ** 푸앙이 이미지 크기에 맞춰 초기위치, 한계좌표, 충돌인식값 조절 **
    def __init__(self):
        self.x = 155    # 푸앙이 초기 위치가 화면 중앙이 되도록 설정
        self.y = 540
    def move(self):
        if pressed_keys[K_LEFT] and self.x > 0:
            self.x -= 5
        if pressed_keys[K_RIGHT] and self.x < 310:  # 푸앙이 이미지 크기에 따라 푸앙이 x 한계 좌표 조절 *
            self.x += 5
    def draw(self):
        if pressed_keys[K_LEFT]:
            screen.blit(puang_left, (self.x, 540))
        elif pressed_keys[K_RIGHT]:
            screen.blit(puang_right, (self.x, 540))
        else:
            screen.blit(puang_idle, (self.x, 540))

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

    if time.time() - start_time > 60:
        menu = "round2_start"
    
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
            menu = "game_start"

    if menu == "game_start":
        screen.fill((0, 0, 0))
        text = font.render("Game Start!", False, (255,255,255))
        screen.blit(text,(50,50))
        
        time_now = pygame.time.get_ticks()
        if time_now - time_last > 500:
            time_last = pygame.time.get_ticks()
            menu = "round1_start"
        
        
    if menu == "round1_start":
        screen.fill((0, 0, 0))
        text = font.render("Round 1", False, (255,255,255))
        screen.blit(text,(50,50))
        
        time_now = pygame.time.get_ticks()
        if time_now - time_last > 500:
            time_last = pygame.time.get_ticks()
            menu = "round1_game"

    if menu == "round1_game":
        if time.time() - last_spawn_time > 0.5:       # 은행열매 장애물 생성 속도 조절(0.5초마다 생성)
            ginkgos.append(Ginkgo())
            last_spawn_time = time.time()

        screen.fill((255, 255, 255))
        screen.blit(Round1_background, (0,0))
        
        puang.move()
        puang.draw()
        
        i = 0
        while i < len(ginkgos):
            ginkgos[i].move()
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
                buttonrect_end= pygame.Rect((txt_x, txt_y), txt.get_size())
                pygame.draw.rect(screen, (255,0,0), buttonrect_end)
                screen.blit(txt, (txt_x, txt_y))
           
                while 1:
                    for event in pygame.event.get():
                        if event.type == QUIT:
                            sys.exit()
                    if pygame.mouse.get_pressed()[0] and buttonrect_end.collidepoint(pygame.mouse.get_pos()):
                        menu = "round1_start"
                        time_last = 0
                        time_now = 0
                        last_spawn_time = 0
                        puang = Puang() 
                        ginkgos.clear()
                        break

                    pygame.display.update()

        pygame.draw.rect(screen, (234,234,234), [300, 0, 100, 60])
        screen.blit(font.render(str(int((pygame.time.get_ticks())/1000)), True, (0, 0, 0)), (325, 15))
    
    pygame.display.update()             # 스크린 업데이트(게임 루프 제일 하단에 *반드시* 위치해야 함)