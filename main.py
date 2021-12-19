### 모듈 불러오기 ###
import pygame, sys, random, time
from pygame.locals import *

### 프로그램 기본 세팅 ###
pygame.init()
pygame.display.set_caption("통학러 푸앙이")
screen = pygame.display.set_mode((405,650))
clock = pygame.time.Clock()

### 이미지, 사운드 파일, 폰트 세팅 ###
puang_idle = pygame.image.load("images/puang.png")
puang_walk = pygame.image.load("images/puang_side.png")
puang_left = pygame.transform.flip(puang_walk, True, False)
puang_right = puang_walk

main = pygame.image.load("images/main(1).png")
game_start = pygame.image.load("images/game_start.png")
Round1_background = pygame.image.load("images/round1_background.png")
Round2_background = pygame.image.load("images/round2_background.png")
Round3_background = pygame.image.load("images/round3_background.png")
Round1_start = pygame.image.load("images/round1_start.png")
Round2_start = pygame.image.load("images/round2_start.png")
Round3_start = pygame.image.load("images/round3_start.png")
Round1_OVER = pygame.image.load("images/round1_end.png")
Round2_OVER = pygame.image.load("images/round2_end.png")
Round3_OVER = pygame.image.load("images/round3_end.png")
ending = pygame.image.load("images/ending.png")



ginkgo_image = pygame.image.load("images/obstacle/round01/ginkgo.png")
animal_images = ['animal-1.png', 'animal-2.png', 'animal-3.png', 'animal-4.png', 'animal-5.png', \
                 'animal-6.png', 'animal-7.png', 'animal-8.png', 'animal-9.png', 'animal-10.png']
people_images = ['people-1.png', 'people-2.png', 'people-3.png', 'people-4.png', 'people-5.png', \
                 'people-6.png', 'people-7.png', 'people-8.png', 'people-9.png', 'people-10.png', 'people-11.png', 'people-12.png']

font = pygame.font.Font(None, 50)


### 변수 세팅 : 변수 선언 ###
time_last = 0
time_now = 0
menu = "main"
last_spawn_time = 0
start_time = time.time()
DIR2 = "images/obstacle/round02/"
DIR3 = "images/obstacle/round03/"


### 클래스 세팅 : 클래스 생성 ###
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

    def hit_by(self, obstacle):
        return pygame.Rect((self.x, self.y),(72, 90)).collidepoint(obstacle.x, obstacle.y)

class Ginkgo:                                       # 은행 열매 클래스 
    def __init__(self):
        self.x = random.randint(50,355)           
        self.y = -60
        self.dy = random.randint(1,2)               # y 방향 가속 설정

    def move (self):
        self.dy += 0.1
        self.y += self.dy

    def draw(self):
        screen.blit(ginkgo_image, (self.x, self.y))

    def off_screen(self):       # 화면에서 사라진 인스턴스 삭제 
        return self.y > 650

class Animal:
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
    
    def draw(self):
        animal_image = pygame.image.load(DIR2 + animal_images[self.num])
        screen.blit(animal_image, (self.x, self.y))

    def bounce(self):       
        if self.x < 0 or self.x > 355:
            self.dx *= -1
        if self.y == self.p:
            self.dx *= -1

    def off_screen(self):    
        return self.y > 650

class People:
    def __init__(self):
        self.num = random.randint(0,11)
        self.x = random.randint(66,339)           
        self.y = -60
        self.dy = random.randint(2,3)             
        self.dx = random.choice((-1,1))*self.dy
        self.p = random.randint(250, 400)

    def move (self):
        self.x += self.dx
        self.y += self.dy

    def bounce(self):           
        if self.x < 0 or self.x > 339:
            self.dx *= -1
        if self.y == self.p:
            self.dx *= -1
                    
    def draw(self):
        people_image = pygame.image.load(DIR3 + people_images[self.num])
        screen.blit(people_image, (self.x, self.y))

    def off_screen(self):    
        return self.y > 650


### 인스턴스 세팅 : 인스턴스 생성 ###
puang = Puang()
ginkgos = []
animals = []
peoples = []


### 게임 메인 루프 ###
while 1:
    clock.tick(60)                      # 스크린 프레임 레이트 설정 (60fps)           
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()                  # QUIT 버튼 클릭 여부 감지
    pressed_keys = pygame.key.get_pressed()
    
    if menu == "main":
        screen.fill((255, 255, 255))
        screen.blit(main, (0,0))
        buttonrect = pygame.Rect(230, 540, 150, 44)
        pygame.draw.rect(screen, (0,0,0), buttonrect, 1)
        if pygame.mouse.get_pressed()[0] and buttonrect.collidepoint(pygame.mouse.get_pos()):
            time_last = pygame.time.get_ticks()
            menu = "game_start"

    if menu == "game_start":
        screen.blit(game_start, (0,0))
        
        time_now = pygame.time.get_ticks()
        if time_now - time_last > 500:
            time_last = pygame.time.get_ticks()
            menu = "round1_start"
        
        
    if menu == "round1_start":
        screen.blit(Round1_start, (0,0))
        
        time_now = pygame.time.get_ticks()
        if time_now - time_last > 500:
            time_last = pygame.time.get_ticks()
            menu = "round1_game"

    if menu == "round1_game":
        time_now = pygame.time.get_ticks()
        if time.time() - last_spawn_time > 0.5:       # 1라운드 장애물 생성 속도 조절(0.5초마다 생성)
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
                buttonrect = pygame.Rect(71,565,263,57)
                pygame.draw.rect(screen, (0,0,0), buttonrect, 1)
           
                while 1:
                    for event in pygame.event.get():
                        if event.type == QUIT:
                            sys.exit()
                    if pygame.mouse.get_pressed()[0] and buttonrect.collidepoint(pygame.mouse.get_pos()):
                        menu = "round1_start"
                        time_last = 0
                        time_now = 0
                        last_spawn_time = 0
                        puang = Puang() 
                        ginkgos.clear()
                        break

                    pygame.display.update()
    
    if time_now - time_last > 10000:
        time_last = pygame.time.get_ticks()
        last_spawn_time = 0
        puang = Puang() 
        ginkgos.clear()
        menu = "round2_start"

    if menu == "round2_start":
        screen.blit(Round2_start, (0,0))
        
        time_now = pygame.time.get_ticks()
        if time_now - time_last > 500:
            time_last = pygame.time.get_ticks()
            menu = "round2_game"

    if menu == "round2_game":
        time_now = pygame.time.get_ticks()
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
                buttonrect = pygame.Rect(71,565,263,57)
                pygame.draw.rect(screen, (0,0,0), buttonrect, 1)
           
                while 1:
                    for event in pygame.event.get():
                        if event.type == QUIT:
                            sys.exit()
                    if pygame.mouse.get_pressed()[0] and buttonrect.collidepoint(pygame.mouse.get_pos()):
                        menu = "round2_start"
                        time_last = 0
                        time_now = 0
                        last_spawn_time = 0
                        puang = Puang() 
                        animals.clear()
                        break

                    pygame.display.update()
    
    if time_now - time_last > 10000:    
        time_last = pygame.time.get_ticks()
        last_spawn_time = 0
        puang = Puang() 
        animals.clear()
        menu = "round3_start"

    if menu == "round3_start":
        screen.blit(Round2_start, (0,0))
        
        time_now = pygame.time.get_ticks()
        if time_now - time_last > 500:
            time_last = pygame.time.get_ticks()
            menu = "round3_game"

    if menu == "round3_game":
        time_now = pygame.time.get_ticks()
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
                buttonrect = pygame.Rect(71,565,263,57)
                pygame.draw.rect(screen, (0,0,0), buttonrect, 1)
           
                while 1:
                    for event in pygame.event.get():
                        if event.type == QUIT:
                            sys.exit()
                    if pygame.mouse.get_pressed()[0] and buttonrect.collidepoint(pygame.mouse.get_pos()):
                        menu = "round3_start"
                        time_last = 0
                        time_now = 0
                        last_spawn_time = 0
                        puang = Puang() 
                        peoples.clear()
                        break
                    pygame.display.update()
    
    if time_now - time_last > 10000:    
        time_last = pygame.time.get_ticks()
        clock.tick(60) 
        last_spawn_time = 0
        puang = Puang() 
        peoples.clear()
        menu = "outro"

    if menu == "outro":
        screen.blit(ending,(0,0)) 
        buttonrect = pygame.Rect(71,510,263,57)
        pygame.draw.rect(screen, (0,0,0), buttonrect, 1)
        while 1:
            for event in pygame.event.get():
                if event.type == QUIT:
                    sys.exit()
            if pygame.mouse.get_pressed()[0] and buttonrect.collidepoint(pygame.mouse.get_pos()):
                menu = "main"
                time_last = pygame.time.get_ticks()
                pygame.time.delay(500)
                break
                
            pygame.display.update()

    
    pygame.display.update()             # 스크린 업데이트(게임 루프 제일 하단에 *반드시* 위치해야 함)
