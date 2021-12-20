import pygame, sys, time
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((300,100))

font = pygame.font.Font(None, 50)

passed_time = time.time()
start_tick = pygame.time.get_ticks()

class Timer:
    def __init__(self):
        self.round_tick = 3
        self.game_min = 0
        self.game_clock = "9 : 2" + str(int(self.game_min/100))
        self.passed_time = time.time()
        pygame.draw.rect(screen, (234,234,234), [295, 0, 110, 60])  
        screen.blit(font.render(self.game_clock, True, (255,255,255)), (25, 30))
    def draw(self):
        if time.time() - self.passed_time > self.round_tick:
            pygame.draw.rect(screen, (234,234,234), [295, 0, 110, 60])  
            screen.blit(font.render(self.game_clock, True, (255,255,255)), (25, 30))
            self.game_min += 1
            self.game_clock = "9 : 2" + str(int(self.game_min/100))

timer = Timer()

while 1:
    time_now = time.time()
    for event in pygame.event.get():       
        if event.type == QUIT:              
            sys.exit()
    screen.fill((0,0,0))
    pygame.draw.rect(screen, (234,234,234), [295, 0, 110, 60])  
    screen.blit(font.render(timer.game_clock, True, (255,255,255)), (25, 30))

    timer.draw()

    ticks = time_now - passed_time
    
          # 배경을 지워주지 않으면 쓴 글자 위에 계속해서 시간이 표시된다. -> 반드시 시간을 표시하기 전에 이미 쓴 시간을 한 번 지워줘야 함
    screen.blit(font.render(str(int(pygame.time.get_ticks()/1000)), True, (255, 255, 255)), (200, 30))     # 흘러간 시간(초) 카운팅
    screen.blit(font.render(str(10 - int(ticks)), True, (255, 255, 255)), (200, 60))     # 흘러간 시간(초) 카운팅

    pygame.display.update()

