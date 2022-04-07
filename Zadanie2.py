import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((1000, 1000))
Grey = (130, 130, 130)
Black = (0, 0, 0)
Yellow = (225, 225, 0)
Red = (237, 28, 28)
Black_Grey=(26,26,26)
White=(255,255,255)
WHite_grey=(204,197,190)
Oblako=(41,42,51)
Blue = (8, 96, 168)
size=1000


def pryamoug(clour, x, y, x1, y1, x2, y2, x3, y3):
    polygon(screen, clour, [(x, y), (x1, y1), (x2, y2), (x3, y3)])


def Fon(colour, x, y, a, b):
    rect(screen, colour, (x, y, a, b))


Fon(Grey, 0, 0, 1000, 450)
Fon(Black, 0, 450, 1000, 1000)
circle(screen,White,(900,100), 70)
ellipse(screen,Oblako,(100,80,650,90))
ellipse(screen,WHite_grey,(400,40,650,90))
ellipse(screen,WHite_grey,(700,150,650,90))
ellipse(screen,Oblako,(550,200,900,90))




def house():
    pryamoug((40, 34, 11), 60, 200, 600, 200, 600, 700, 60, 700)


house()
def chert (N,colour,x,y,x1,y2,sum):
    h= 0

    for i in range(N):
        pryamoug(colour, x + h, y, x1 + h - 10, y, x1 + h - 10, y2, x + h, y2)
        h += sum
        pryamoug(colour, x + h, y, x1 + h - 10, y, x1 + h - 10, y2, x + h, y2)
        h += sum+110
chert(4,(72, 62, 55),100, 250, 160, 470,10)
chert(5,Black_Grey,90,420,130,510,2)
pryamoug(Black_Grey, 0, 475,630,475,630,515,0,515)
pryamoug(Black_Grey, 30, 400,610,400,610,420,30,420)
pryamoug(Black_Grey, 610,420,620,420,620,475,610,475)
pryamoug(Black_Grey, 10, 420,30,420,30,475,10,475)
chert(2,(43,17,0),150,550,250,620,10)
pryamoug(Yellow, 430, 550,530,550, 530,620,430,620)
pryamoug(Black,0,200,60,160,600,160,660,200)

def Ghost(sc, body_color, eyes_color, eyeballs_color, eyeballs_color_2, coord_x, coord_y, ghost_size, font_color):
    circle(sc, body_color, (coord_x, coord_y), 50*ghost_size)  # голова
    circle(sc, eyes_color, (coord_x-25*ghost_size, coord_y-10*ghost_size), 10*ghost_size)  # глаза
    circle(sc, eyes_color, (coord_x+15*ghost_size, coord_y-10*ghost_size), 10*ghost_size)
    circle(sc, eyeballs_color, (coord_x - 28*ghost_size, coord_y - 10*ghost_size), 5*ghost_size)  # зрачки (черные)
    circle(sc, eyeballs_color, (coord_x + 12*ghost_size, coord_y - 10*ghost_size), 5*ghost_size)

    k = 4*ghost_size  # зрачки (белые)
    for i in range(5):
        circle(sc, eyeballs_color_2, (coord_x - (28-k)*ghost_size, coord_y - (10+k)*ghost_size), 3*ghost_size)
        circle(sc, eyeballs_color_2, (coord_x + (12+k)*ghost_size, coord_y - (10+k)*ghost_size), 3*ghost_size)
        k+=1*ghost_size

    polygon(sc,body_color, [(coord_x-40*ghost_size, coord_y+10*ghost_size), (coord_x+50*ghost_size, coord_y+20*ghost_size), (coord_x+150*ghost_size, coord_y+190*ghost_size),
                            (coord_x-160*ghost_size, coord_y+190*ghost_size)])  # туловище

    # "волнистость" туловища
    k_x = 4 * ghost_size
    k_y = 4 * ghost_size
    for i in range(19):
        circle(sc, body_color, (coord_x + (50 * ghost_size) + k_x, coord_y + (40 * ghost_size) + k_y), 30 * ghost_size)
        k_x+=4*ghost_size
        k_y+=8*ghost_size

    circle(sc, font_color, (coord_x+85*ghost_size, coord_y+210*ghost_size), 30 * ghost_size)
    circle(sc, body_color, (coord_x + 30 * ghost_size, coord_y + 190 * ghost_size), 30 * ghost_size)
    circle(sc, font_color, (coord_x - 25 * ghost_size, coord_y + 210 * ghost_size), 30 * ghost_size)
    circle(sc, body_color, (coord_x - 80 * ghost_size, coord_y + 190 * ghost_size), 30 * ghost_size)
    circle(sc, font_color, (coord_x - 135 * ghost_size, coord_y + 210 * ghost_size), 30 * ghost_size)

Ghost(screen, Grey, Blue, Black, White, 0.8*size, 0.6*size, 0.7, Black)  # последние 4 координаты x и y, размер, и цвет фона, на котором должен быть призрак



pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
