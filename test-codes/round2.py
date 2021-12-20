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
menu = "round2_start"
last_spawn_time = 0

DIR2 = "images/obstacle/round02/"



### 클래스 세팅 : 클래스 생성 ###
class Animal:
    animal_images = ['animal-1.png', 'animal-2.png', 'animal-3.png', 'animal-4.png', 'animal-5.png', \
                 'animal-6.png', 'animal-7.png', 'animal-8.png', 'animal-9.png', 'animal-10.png']
    def __init__(self):
        self.num = random.randint(0,9)
        self.x = random.randint(140,300)    
        self.y = 180
        self.dy = random.randint(2,3)              
        self.dx = random.choice((-1,1))*self.dy/2
        self.p = random.randint(250, 400)

    def move (self):
        if self.y > 200:
            self.x += self.dx
            self.y += self.dy
        else:
            self.y += self.dy *2

        #self.dy += 0.1
        
        
    

    def draw(self):
        animal_image = pygame.image.load(DIR2 + self.animal_images[self.num])
        screen.blit(animal_image, (self.x, self.y))

    def bounce(self):       
        if self.x < 0 or self.x > 405:
            self.dx *= -1
        if self.y == self.p:
            self.dx *= -1

    def off_screen(self):    
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

    def hit_by(self, animal):
        return pygame.Rect((self.x, self.y),(95, 105)).collidepoint(animal.x, animal.y)



### 인스턴스 세팅 : 인스턴스 생성 ###
animals = []
puang = Puang()

### 게임 메인 루프 ###
while 1:
    clock.tick(60)                      # 스크린 프레임 레이트 설정 (60fps)           
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()                  # QUIT 버튼 클릭 여부 감지
    pressed_keys = pygame.key.get_pressed()   
        
    if menu == "round2_start":
        screen.fill((0, 0, 0))
        text = font.render("Round 2", False, (255,255,255))
        screen.blit(text,(50,50))
        
        time_now = pygame.time.get_ticks()
        if time_now - time_last > 500:
            time_last = pygame.time.get_ticks()
            menu = "round2_game"

    if menu == "round2_game":
        if time.time() - last_spawn_time > 0.8:       # 장애물 생성 속도 조절(0.8초마다 생성)
            animals.append(Animal())
            last_spawn_time = time.time()

        screen.fill((255, 255, 255))
        screen.blit(Round2_background, (0,0))
        
        puang.move()
        puang.draw()
        
        i = 0
        while i < len(animals):
            animals[i].move()
            animals[i].bounce()
            animals[i].draw()
            if animals[i].off_screen():
                del animals[i]
                i -= 1
            i += 1

        for animal in animals:
            if puang.hit_by(animal):
                screen.blit(Round2_OVER, (0,0))
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
                        menu = "round2_start"
                        time_last = 0
                        time_now = 0
                        last_spawn_time = 0
                        puang = Puang() 
                        animals.clear()
                        break

                    pygame.display.update()

        pygame.draw.rect(screen, (234,234,234), [300, 0, 100, 60])
        screen.blit(font.render(str(int((pygame.time.get_ticks())/1000)), True, (0, 0, 0)), (325, 15))
    pygame.display.update()             # 스크린 업데이트(게임 루프 제일 하단에 *반드시* 위치해야 함)