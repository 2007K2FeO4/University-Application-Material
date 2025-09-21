#鼠标点击，空格切换模式，'+'表示插上旗帜
#24*24,72lms
import pygame
import random
import time,timeit
from pygame.locals import *
pygame.init()
s=pygame.display.set_mode((900,700))
s.fill((230,200,250))
endtime=starttime=time.time()
pygame.display.set_caption('landmind')
f=pygame.font.Font('framd.ttf',20)
f2=pygame.font.Font('comic.ttf',144)
lmpos=[0 for i in range(576)]
# 0 未点击 1 已查找 2 被标记 3 地雷爆炸
lmimg=[]
for i in range(1,9):
    if i<5:
        lmimg.append(f.render(' '+str(i),1,(90+40*i,90,250)))
    else:
        lmimg.append(f.render(' '+str(i),1,(250,90,410-40*i)))
flag=f.render(' +',1,(255,255,255))
wrong=f.render(' X',1,(255,0,0))
lmimg.append(pygame.image.load('boom.png'))
lmimg.append(pygame.image.load('boom2.png'))
lmimg[-1]=pygame.transform.smoothscale(lmimg[-1],(25,25))
lmimg[-2]=pygame.transform.smoothscale(lmimg[-2],(25,25))
# 0~8 数量 9 地雷 10 爆炸地雷
lm1=pygame.image.load('lm1.png')
lm1=pygame.transform.smoothscale(lm1,(25,25))
lm2=pygame.image.load('lm2.png')
lm2=pygame.transform.smoothscale(lm2,(25,25))    
bac=pygame.image.load('lmbac.png')
bac=pygame.transform.smoothscale(bac,(700,700))
tip1=f.render(' =>',1,(150,100,160))
tip2=f.render(' + ',1,(150,100,160))
lose=f2.render('Failed',1,(150,145,155))
win=f2.render('Successed',1,(255,250,155))
pygame.display.set_icon(lm1)
clicked=576
# 576 初始状态
pcs=0
lmode=0
lmnum=72
lmeve=[]
lms=[]
bm=0
def makemap():
    global lmeve
    lmeve=[0 for i in range(504)]
    lmeve+=[9 for i in range(72)]
    random.shuffle(lmeve)     
    for j in range(24):
        for i in range(24):
            nt=set()
            test=[-25,-24,-23,-1,1,23,24,25]
            if i==0:
                nt.add(-25)
                nt.add(-1)
                nt.add(23)
            elif i==23:
                nt.add(-23)
                nt.add(1)
                nt.add(25)
            if j==0:
                nt.add(-25)
                nt.add(-24)
                nt.add(-23)
            elif j==23:
                nt.add(23)
                nt.add(24)
                nt.add(25)
            for k in test:
                if not(k in nt or lmeve[j*24+i]==9):
                    if lmeve[j*24+i+k]==9:
                        lmeve[j*24+i]+=1
            #print(lmeve[j*12+i],end=' ')
        #print('') 
######
def makeimage():
    global f,s,lmeve,lmpos,lms,lmode,bac,lm1,lm2,\
           lmimg,flag,tip1,tip2,lmnum,starttime,endtime
    s.fill((230,200,250))
    s.blit(bac,(100,0))
    tip3=f.render(str(lmnum),1,(150,100,160))
    tip4=f.render(str(round(endtime-starttime)),1,(150,100,160))
    for j in range(24):
        for i in range(24):
            s.blit(lm2,(i*25+150,j*25+50))
            if lmeve[j*24+i]:
                s.blit(lmimg[lmeve[j*24+i]-1],(i*25+150,j*25+50))
            if lmpos[j*24+i]%2==0:
                s.blit(lm1,(i*25+150,j*25+50))
            if j*24+i in lms:
                s.blit(flag,(i*25+150,j*25+50))  
            if lmpos[j*24+i]==4:
                s.blit(wrong,(i*25+150,j*25+50))            
    if lmode==0:
        s.blit(tip1,(20,0))
    else:
        s.blit(tip2,(20,0))        
    s.blit(tip3,(30,630))
    s.blit(tip4,(805,0))
'''
-25 -24 -23
-1   0   1 
 23  24  25
'''
def auto(cl):
    global lmeve,lmpos
    test=[-25,-24,-23,-1,1,23,24,25]   
    nt=set()
    if cl%24==0:
        nt.add(-25)
        nt.add(-1)
        nt.add(23)
    elif cl%24==23:
        nt.add(-23)
        nt.add(1)
        nt.add(25)
    if cl//24==0:
        nt.add(-23)
        nt.add(-24)
        nt.add(-25)
    elif cl//24==23:
        nt.add(23)
        nt.add(24)
        nt.add(25)    
    if lmpos[cl]==0:
        lmpos[cl]=1
        if lmeve[cl]==0:
            for i in test:
                if not i in nt:
                    if lmpos[cl+i]==0:
                        auto(cl+i)
def check():
    global lmeve,lmpos,boom2,lmnum,lms,bm
    correct=0
    for i in range(576):
        if lmeve[i]==9 and lmpos[i]==1 and bm==0:
            lmpos[i]=3
            lmeve[i]=10
            bm=1
            break
    if bm==1:
        for i in range(576):
            if lmeve[i]==9:
                lmpos[i]=3
            elif i in lms:
                lmpos[i]=4                
    if lmnum==0:
        for i in range(576):
            if lmeve[i]==9 and i in lms:
                correct+=1
        if correct==72:
            bm=2
            for i in range(576):
                lmpos[i]=1     
def fine():
    if bm==1:
        s.blit(lose,(290,250))
    elif bm==2:
        s.blit(win,(370,250))     
makemap()
while True:
    makeimage()
    if bm==0:
        endtime=time.time()
        if clicked<576:
            if lmode==0:
                if lmpos[clicked]==0:
                    if pcs==0:
                        while lmeve[clicked]:
                            makemap()
                    makeimage()
                    auto(clicked)
                    pcs+=1
            else:
                if lmpos[clicked]==2:
                    lmpos[clicked]=0
                    lms.remove(clicked)
                    lmnum+=1 
                else:
                    lmpos[clicked]=2
                    lms.append(clicked)
                    lmnum-=1 
    else:
        fine()
    clicked=576
    check()
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()   
        if event.type==MOUSEBUTTONDOWN:
            for j in range(24):
                for i in range(24):
                    if Rect(i*25+150,j*25+50,25,25).collidepoint(event.pos):
                        clicked=j*24+i
        if event.type==KEYDOWN and pygame.key.get_pressed()[K_SPACE]:
            if lmode:
                lmode=0
            else:
                lmode=1    
    pygame.display.update()

