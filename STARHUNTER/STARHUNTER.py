import os
import msvcrt
import random
import time


global mapname
global mas
global corpoz
global aim
global score
global scrin
global start_t

#MAPNAME
mapname="MAP1.txt"

mas=[]
corpoz=[1,1]
aim=[1,1]
score=-1
#[H,W]
scrin=[20,20]
start_t=time.time()


#INIT MAP
with open(f"MAPS/{mapname}") as fmap:
    for line in fmap:
        tmp=[]
        for sumvol in line:
            tmp.append(sumvol)
        mas.append(tmp)


def display(key):
    global mas
    global corpoz
    global aim
    global score
    global scrin
    global start_t
    
    mas[corpoz[0]][corpoz[1]]=' '
    tmppoz=[0,0]
    tmppoz[0]=corpoz[0]
    tmppoz[1]=corpoz[1]
    print("TMPPOZ:",tmppoz)#DEL
    if key=='s':
        corpoz[0]+=1
        if corpoz[0] >= scrin[0]:
            corpoz[0]=scrin[0]-1
    if key=='w':
        corpoz[0]-=1
        if corpoz[0] <= 0:
            corpoz[0]=0
    if key=='d':
        corpoz[1]+=1
        if corpoz[1] >= scrin[1]:
            corpoz[1]=scrin[1]-1
    if key=='a':
        corpoz[1]-=1
        if corpoz[1] <= 0:
            corpoz[1]=0
    if mas[corpoz[0]][corpoz[1]]=='#':
        corpoz[0]=tmppoz[0]
        corpoz[1]=tmppoz[1]
        print("CORPOZ:",corpoz,"TMPPOZ:",tmppoz)
    mas[corpoz[0]][corpoz[1]]='@'
            
    os.system('cls')
    for i in mas:
        for j in i:
            print(j, sep='',end='')
    print("CORPOZ:",corpoz,"AIM:",aim,"SCORE:",score)
    print("GAMETIME:",round(time.time()-start_t),"\bs","SPS:",round(score/(time.time()-start_t),3))
    
    if corpoz[0]==aim[0] and corpoz[1]==aim[1]:
        score+=1
        while True:
            aim=[random.randint(1,scrin[0]-2),random.randint(1,scrin[1]-2)]
            if mas[aim[0]][aim[1]]!='#':
                break
        mas[aim[0]][aim[1]]='*'


display(' ')
while True:
    time.sleep(0.001)
    if msvcrt.kbhit():
        key=chr(msvcrt.getch()[0])
        if key=='p':
            exit
        if key in ['s','w','d','a']:
            display(key)
