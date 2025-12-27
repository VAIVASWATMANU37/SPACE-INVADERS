import pygame
import random
import math
SW=800
SH=500
PSX=370
PSY=380
EYMN=50
EYMX=150
ESX=4
ESY=40
BSY=10
CD=27
pygame.init()
screen=pygame.display.set_mode((SW,SH))
pygame.display.set_caption("SPACE INVADERS")
BG=pygame.image.load('download.jpg')
PI=pygame.image.load('images.jpg')
PX=PSX
PY=PSY
PXC=0
EI=[]
EX=[]
EY=[]
EXC=[]
EYC=[]
EN=6
for i in range(EN):
    EI.append(pygame.image.load('asteroid.jpg'))
    EX.append(random.randint(0,SW-64))
    EY.append(random.randint(EYMN,EYMX))
    EXC.append(ESX)
    EYC.append(ESY)
BI=pygame.image.load('missile.jpg')
BX=0
BY=PSY
BXC=0
BYC=BSY
BST="READY"
SV=0
font=pygame.font.Font('freesansbold.ttf',32)
TX=10
TY=10
over_font=pygame.font.Font('freesansbold.ttf',64)
def show_score(x,y):
    score=font.render("SCORE : "+str(SV),True,(255,255,255))
    screen.blit(score,(x,y))
def game_over_text():
    over_text=over_font.render("GAME OVER",True,(255,255,255))
    screen.blit(over_text,(250,200))
def player(x,y):
    screen.blit(PI,(x,y))
def enemy(x,y,i):
    screen.blit(EI[i],(x,y))