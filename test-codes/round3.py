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

font = pygame.font.SysFont("PFStardust", 50, True) # pygame.font.SysFont(font name, size, bold = False, italic = False)
#text = font.render("Game Start!", False, (0,0,0)) # render(Text, antialias, color, background = None)
#screen.blit(text,(100,100))

### 변수 세팅 : 변수 선언 ###
time_last = 0
time_now = 0
menu = "main"
last_spawn_time = 0

DIR3 = "images/obstacle/round03/"


### 클래스 세팅 : 클래스 생성 ###
class People:
    people_images = ['people-1.png', 'people-2.png', 'people-3.png', 'people-4.png', 'people-5.png', \
                 'people-6.png', 'people-7.png', 'people-8.png', 'people-9.png', 'people-10.png', 'people-11.png', 'people-12.png']
    def __init__(self):
        self.num = random.randint(0,11)
        self.x = random.randint(20,630)             # 은행열매 픽셀 20
        self.y = -60
        self.dy = random.randint(2,3)*2              
        self.dx = random.choice((-1,1))*self.dy
        self.p = random.randint(250, 400)

    def move (self):
        self.x += self.dx
        self.y += self.dy

    def bounce(self):           # 벽에 부딪혔을 때 튕겨나오도록 하는 부분
        if self.x < 0 or self.x > 405:
            self.dx *= -1
        if self.y == self.p:
            self.dx *= -1
                    

    def draw(self):
        people_image = pygame.image.load(DIR3 + self.people_images[self.num])
        screen.blit(people_image, (self.x, self.y))

    def off_screen(self):    
        return self.y > 650
    


class Puang: # ** 푸앙이 이미지 크기에 맞춰 초기위치, 한계좌표, 충돌인식값 조절 **
    def __init__(self):
        self.x = 155    # 푸앙이 초기 위치가 화면 중앙이 되도록 설정
        self.y = 540
    def move(self):
        if pressed_keys[K_LEFT] and self.x > 0:
            self.x -= 10
        if pressed_keys[K_RIGHT] and self.x < 310:  # 푸앙이 이미지 크기에 따라 푸앙이 x 한계 좌표 조절 *
            self.x += 10
    def draw(self):
        if pressed_keys[K_LEFT]:
            screen.blit(puang_left, (self.x, 540))
        elif pressed_keys[K_RIGHT]:
            screen.blit(puang_right, (self.x, 540))
        else:
            screen.blit(puang_idle, (self.x, 540))

    def hit_by(self, people):
        return pygame.Rect((self.x, self.y),(95, 105)).collidepoint(people.x, people.y)



### 인스턴스 세팅 : 인스턴스 생성 ###
peoples = []
puang = Puang()

### 게임 메인 루프 ###
while 1:
    clock.tick(30)                      # 스크린 프레임 레이트 설정 (60fps)           
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
            menu = "game_start"

    if menu == "game_start":
        screen.fill((0, 0, 0))
        text = font.render("Game Start!", False, (255,255,255))
        screen.blit(text,(50,50))
        
        time_now = pygame.time.get_ticks()
        if time_now - time_last > 500:
            time_last = pygame.time.get_ticks()
            menu = "round3_start"
        
        
    if menu == "round3_start":
        screen.fill((0, 0, 0))
        text = font.render("Round 3", False, (255,255,255))
        screen.blit(text,(50,50))
        
        time_now = pygame.time.get_ticks()
        if time_now - time_last > 500:
            time_last = pygame.time.get_ticks()
            menu = "round3_game"

    if menu == "round3_game":
        if time.time() - last_spawn_time > 0.8:       # 장애물 생성 속도 조절(0.8초마다 생성)
            peoples.append(People())
            last_spawn_time = time.time()

        screen.fill((255, 255, 255))
        screen.blit(Round3_background, (0,0))
        
        puang.move()
        puang.draw()
        
        i = 0
        while i < len(peoples):
            peoples[i].move()
            peoples[i].bounce()
            peoples[i].draw()
            if peoples[i].off_screen():
                del peoples[i]
                i -= 1
            i += 1

        for people in peoples:
            if puang.hit_by(people):
                screen.blit(Round3_OVER, (0,0))
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
                        menu = "main"
                        time_last = 0
                        time_now = 0
                        last_ginkgo_spawn_time = 0
                        puang = Puang() 
                        peoples.clear()
                        break
                    pygame.display.update()

        pygame.draw.rect(screen, (234,234,234), [300, 0, 100, 60])
        screen.blit(font.render(str(int((pygame.time.get_ticks())/1000)), True, (0, 0, 0)), (325, 15))
    pygame.display.update()             # 스크린 업데이트(게임 루프 제일 하단에 *반드시* 위치해야 함)