import random
import pygame
import sys
from pygame.locals import *
pygame.init()
countx=-100
county=0
xx,y=0,0
movex=0
movey=0
white=(255,255,255)
screen=pygame.display.set_mode((800,500),0,32)
grass=pygame.image.load("grass.png").convert_alpha()
dirt=pygame.image.load("dirt.png").convert_alpha()
rock=pygame.image.load("rock.png").convert_alpha()
char=pygame.image.load("char.png").convert_alpha()
mouseimg=pygame.image.load("mouse.png").convert_alpha()
char=pygame.transform.scale(char, (50,100))
clock = pygame.time.Clock()
#pygame.mixer.init()
while True:
    while True:
        clock.tick(1)
        print("Welcome to terrain generator!")
        print("""Menu
)--(
1)Generate new Terrain
2)View Old Terrain
3)Exit""")
        enter=input(">").lower()
        if enter=="1" or enter=="2" or enter=="3":
            break
        else:
            print("Invalid option!")
    if enter=="1":
        count=0
        file=open("terrain.txt","w")
        file.write("")
        file.close()
        while True:
            z=random.randint(0,5)
            file=open("terrain.txt","a")
            file.write(str(z)+"\n")
            file.close()
            count+=1
            if count>=48:
                break
        print("New Terrain Generated!!")
        print()
    elif enter=="2":
        screen.fill(white)
        #pygame.mixer.music.load("maintheme.mp3")
        #pygame.mixer.music.play(loops=-1)
        while True:
            clock.tick(24)
            mouse=pygame.mouse.get_pos()
            mousex=mouse[0]
            mousey=mouse[1]
            for event in pygame.event.get():
                if event.type==QUIT:
                    pygame.quit()
                    sys.exit
                if event.type==KEYDOWN:
                    if event.key==K_w:
                        movey=-5
                    if event.key==K_s:
                        movey=+5
                    if event.key==K_a:
                        movex=-5
                    if event.key==K_d:
                        movex=+5
                if event.type==KEYUP:
                    if event.key==K_w:
                        movey=0
                    elif event.key==K_s:
                        movey=0
                    if event.key==K_a:
                        movex=0
                    elif event.key==K_d:
                        movex=0
            file=open("terrain.txt","r")
            data=file.readlines()
            file.close()
            for x in range(len(data)):
                data[x]=data[x].strip("\n")
                data[x]=int(data[x])
            print(data)
            countx=0
            county=0
            for x in range(len(data)):
                if data[x]==5 or data[x]==4 or data[x]==3:
                    screen.blit(grass, (countx,county))
                    if countx>800:
                        county+=100
                        countx=-100
                    if county>500:
                        county=0
                    else:
                        countx+=100
                if data[x]==2 or data[x]==1:
                    screen.blit(dirt, (countx,county))
                    if countx>800:
                        county+=100
                        countx=-100
                    if county>500:
                        county=0
                    else:
                        countx+=100
                if data[x]==0:
                    screen.blit(rock, (countx,county))
                    if countx>800:
                        county+=100
                        countx=-100
                    if county>500:
                        county=0
                    else:
                        countx+=100
            xx+=movex
            y+=movey
            screen.blit(char, (xx,y))
            screen.blit(mouseimg, (mousex-50, mousey-50))
            pygame.display.update()
    else:
        break
        pygame.display.update()
#stop it from re-generating the map
#make collision with random blocks so that there is a destroying system
