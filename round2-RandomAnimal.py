### 모듈 불러오기 ###
import pygame, sys, random, time
from pygame.locals import *

### 프로그램 기본 세팅 ###
pygame.init()
pygame.display.set_caption("통학러 푸앙이")
screen = pygame.display.set_mode((405, 650))   # 스크린 사이즈 405*650 (대략 10:16 비율)
clock = pygame.time.Clock()
last_animal_spawn_time = 0
GAME_OVER = pygame.load("images/gameover.png").convert() #게임오버 이미지

### 이미지, 사운드 파일, 폰트 세팅 ###
animal_image = pygame.image.load("images/animal.png").convert() #동물 이미지
animal_image.set_colorkey((0, 0, 0))

### 변수 세팅 : 변수 선언 ###


### 클래스 세팅 : 클래스 생성 ###
class Animal:
    def __init__(self):
        self.x = random.randint(0,570)
        self.y = -100
        
    def draw(self):
        screen.blit(animal_image,(self.x,self.y))

    def off_screen(self):
        return self.y > 640

animal = Animal()

class puang:
    def __init__(self):
        self.x = 320
        
    def move(self):
        if pressed_keys[K_LEFT] and self.x > 0:
            self.x -= 3
        if pressed_keys[K_RIGHT] and self.x < 540:
            self.x += 3
            
    def draw(self):
        screen.blit(puang_image,(self.x,591))

    def hit_by(self,animal):
        return (
            animal.y > 585 and
            animal.x > self.x - 55 and
            animal.x < self.x +85
            )

puang = Puang()

### 인스턴스 세팅 : 인스턴스 생성 ###
animals = []


### 게임 메인 루프 ###
while 1:
    clock.tick(60)                      # 스크린 프레임 레이트 설정 (60fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()                  # QUIT 버튼 클릭 여부 감지

    if time.time() - last_animal_spawn_time > 0.5:
        animals.append(Animal())
        last_animal_spawn_time = time.time()
    screen.fill((0, 0, 0))
    puang.move()
    puang.draw()

    i = 0
    while i < len(animals):
        animals[i].move()
        animals[i].draw()

        if animals[i].off_screen():
            del animals[i]
            i -= 1
        i += 1

    screen.blit(font.render("Score: "+str(score),True,(255,255,255)),(5,5))

    for animal in animals:
        if puang.hit_by(animal):
            screen.blit(GAME_OVER,(170,200))
            while 1:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        sys.exit() 
                pygame.display.update()


    pygame.display.update()             # 스크린 업데이트(게임 루프 제일 하단에 *반드시* 위치해야 함)


