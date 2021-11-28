import pygame, sys, time
from pygame.locals import *
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((100,100))

font = pygame.font.Font(None, 50)

while 1:
    clock.tick(60)
    for event in pygame.event.get():       
        if event.type == QUIT:              
            sys.exit()

    screen.fill((0,0,0))        # 배경을 지워주지 않으면 쓴 글자 위에 계속해서 시간이 표시된다. -> 반드시 시간을 표시하기 전에 이미 쓴 시간을 한 번 지워줘야 함
    screen.blit(font.render(str(int((pygame.time.get_ticks())/1000)), True, (255, 255, 255)), (25, 30))     # 흘러간 시간(초) 카운팅
    pygame.display.update()

