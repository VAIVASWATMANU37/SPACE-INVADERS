import pygame
import random
import math
SW = 800
SH = 500
PSX = 370
PSY = 380
EYMN = 50
EYMX = 150
ESX = 4
ESY = 40
BSY = 10
CD = 27
pygame.init()
screen = pygame.display.set_mode((SW, SH))
pygame.display.set_caption("SPACE INVADERS")
BG = pygame.transform.scale(pygame.image.load('download.jpg'), (SW, SH))
PI = pygame.transform.scale(pygame.image.load('images-removebg-preview.png'), (64, 64))
PX = PSX
PY = PSY
PXC = 0
EI = []
EX = []
EY = []
EXC = []
EYC = []
EN = 6
enemy_img = pygame.image.load('asteroid-removebg-preview.png')
for i in range(EN):
    EI.append(pygame.transform.scale(enemy_img, (64, 64)))
    EX.append(random.randint(0, SW - 64))
    EY.append(random.randint(EYMN, EYMX))
    EXC.append(ESX)
    EYC.append(ESY)
BI = pygame.transform.scale(pygame.image.load('missile-removebg-preview.png'), (32, 32))
BX = 0
BY = PSY
BXC = 0
BYC = BSY
BST = "READY"
SV = 0
font = pygame.font.Font('freesansbold.ttf', 21)
TX = 10
TY = 10
over_font = pygame.font.Font('freesansbold.ttf', 64)
def show_score(x, y):
    score = font.render("SCORE : " + str(SV), True, (255, 255, 255))
    screen.blit(score, (x, y))
def game_over_text():
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (250, 200))
def player(x, y):
    screen.blit(PI, (x, y))
def enemy(x, y, i):
    screen.blit(EI[i], (x, y))
def fire_bullet(x, y):
    global BST
    BST = "FIRE"
    screen.blit(BI, (x + 16, y + 10))
def is_collision(ex, ey, bx, by):
    distance = math.sqrt((math.pow(ex - bx, 2)) + (math.pow(ey - by, 2)))
    return distance < CD
running = True
while running:
    screen.fill((0, 0, 0))
    screen.blit(BG, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                PXC = -5
            if event.key == pygame.K_RIGHT:
                PXC = 5
            if event.key == pygame.K_SPACE:
                if BST == "READY":
                    BX = PX
                    fire_bullet(BX, BY)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                PXC = 0
    PX += PXC
    if PX <= 0:
        PX = 0
    elif PX >= SW - 64:
        PX = SW - 64
    for i in range(EN):
        if EY[i] > 340:
            for j in range(EN):
                EY[j] = 2000
            game_over_text()
            break
        EX[i] += EXC[i]
        if EX[i] <= 0:
            EXC[i] = ESX
            EY[i] += EYC[i]
        elif EX[i] >= SW - 64:
            EXC[i] = -ESX
            EY[i] += EYC[i]
        collision = is_collision(EX[i], EY[i], BX, BY)
        if collision:
            BY = PSY
            BST = "READY"
            SV += 1
            EX[i] = random.randint(0, SW - 64)
            EY[i] = random.randint(EYMN, EYMX)
        enemy(EX[i], EY[i], i)
    if BST == "FIRE":
        fire_bullet(BX, BY)
        BY -= BYC
    if BY <= 0:
        BY = PSY
        BST = "READY"
    player(PX, PY)
    show_score(TX, TY)
    pygame.display.update()