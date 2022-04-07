import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))
Grey = (130, 130, 130)
Black = (0, 0, 0)
Yellow = (225, 225, 0)
Red = (237, 28, 28)


pygame.draw.rect(screen, Grey, (0, 0, 400, 400))
pygame.draw.circle(screen, Black, (200, 200), 51) # Начальный круг
pygame.draw.circle(screen, Yellow, (200, 200), 50)
pygame.draw.circle(screen, Black, (177, 188), 12)
pygame.draw.circle(screen, Red, (177, 188), 11)
pygame.draw.circle(screen, Black, (220, 188), 9)
pygame.draw.circle(screen, Red, (220, 188), 8)
pygame.draw.circle(screen, Black, (220, 188), 3)
pygame.draw.circle(screen, Black, (177, 188), 5)
pygame.draw.rect(screen, Black, (170, 220, 45, 10))
polygon(screen, Black, [(193, 182), (145, 163), (145, 160), (193, 179)]) #Левая бровь
polygon(screen, Black, [(210, 182), (245, 167), (245, 163), (210, 179)]) #Правая бровь




pygame.display.update()
clock = pygame.time.Clock()
finished = False
while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

