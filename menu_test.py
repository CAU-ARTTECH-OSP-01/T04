import pygame, sys, time, random
from pygame.locals import *
pygame.init()
clock = pygame.time.Clock()
pygame.display.set_caption("Fly Catcher")
screen = pygame.display.set_mode((1000,600))
fly_image = pygame.image.load("images/ginkgo.png")
homescreen_image = pygame.image.load("images/rough_images/main.png")

font = pygame.font.Font(None, 50)

class Fly:
    def __init__(self):
        self.x = random.randint(0, screen.get_width() - fly_image.get_width())
        self.y = random.randint(0, screen.get_height() - fly_image.get_height())
        self.dir = random.randint(0,359)
        self.spawn_time = time.time()

    def draw(self):
        if time.time() > self.spawn_time + 1.4 and time.time() < self.spawn_time + 3.4:
            rotated = pygame.transform.rotate(fly_image, self.dir)
            screen.blit(rotated,(self.x, self.y))

menu = "start"
fly = Fly()

while 1:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
    pressed_keys = pygame.key.get_pressed()

    if menu == "start":
        screen.blit(homescreen_image, (0,0))
        txt = font.render("Play", True, (255,255,255))
        txt_x = 705
        txt_y = 435
        buttonrect = pygame.Rect((txt_x, txt_y), txt.get_size())
        pygame.draw.rect(screen, (200, 50,0), buttonrect)
        screen.blit(txt, (txt_x, txt_y))
    if pygame.mouse.get_pressed()[0] and buttonrect.collidepoint(pygame.mouse.get_pos()):
        menu = "game"

    if menu == "game":

        if time.time() > fly.spawn_time + 4.4:
            fly = Fly()
        screen.fill((255,255,255))
        fly.draw()


    pygame.display.update()