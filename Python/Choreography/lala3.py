import pygame
from pygame.locals import *
from math import *
pygame.init()

width,height=800,600
screen=pygame.display.set_mode((width,height),RESIZABLE)
pygame.display.set_caption('cheerleading')
font=pygame.font.Font('fzwxz.ttf',20)
clock=pygame.time.Clock()
lala=pygame.mixer.music.load('cheerleading.mp3')
num=[font.render(str(i),1,(0,0,0)) for i in range(1,25)]
sex=[     0,0,
         0,1,0,
       0,1,0,1,0,
     1,1,0,0,0,1,1,
     0,0,1,1,1,0,0]
# 0=girl 1=boy
  
name=['孙易', '朱婧妤', 
      '张乐萱', '金校毅', '许馨然', 
      '俞婧琳', '冯品源', '陆桐雨', '屠天瑞', '施闻怿珩', 
      '孙杨', '胡文智', '陈肖然', '许心怡', '沈雨恬', '李瑞启', '邵钰翔', 
      '陆奕含', '郭轩萱', '吴子函', '刘雨川', '李浚豪', '陈欣怡', '陶佳玟']
nameimage=[]
for i in range(24):
    #print(str(i+1)+' '+name[i])
    nameimage.append(font.render(str(i+1)+' '+name[i],1,(0,0,0)))

t1=[[-15,60],[15,60]]+[[i,30] for i in range(-30,31,30)]\
    +[[i,0] for i in range(-60,61,30)]\
    +[[i,-30] for i in range(-90,91,30)]\
    +[[i,-60] for i in range(-120,121,40)]
t2=[[i,30] for i in range(-40,41,20)]\
    +[[i,0] for i in range(-60,61,30)]\
    +[[i,-30] for i in range(-90,91,30)]\
    +[[i,-60] for i in range(-90,91,30)]
t3=[]
for i in range(45,-46,-30):
    for j in range(-105,106,30):
        if j<=-45 or j>=45:
            t3.append([j-30 if i>0 else j+45,i])
t4=[]
for i in range(45,-46,-30):
    for j in range(-75,76,30):
        t4.append([j,i])
t5=[]
for i in range(45,-46,-30):
    for j in range(-105,106,30):
        if j<=-45 or j>=45:
            t5.append([j,i])
a1,a2,a3=42,36,30
b1,b2,b3=165,180,195
t6=[[-100,20],[-60,20],[-20,30],[20,30],[60,20],[100,20]]\
    +[[cos(radians(i))*20,sin(radians(i))*20] for i in range(b1,b1+a1*6,a1)]\
    +[[cos(radians(i))*50,sin(radians(i))*30] for i in range(b2,b2+a2*6,a2)]\
    +[[cos(radians(i))*80,sin(radians(i))*50] for i in range(b3,b3+a3*6,a3)]

s1=[i for i in range(24)]
s2=[2,0,3,1,4]+[i for i in range(5,24)]
s4=[3,1,4,9,2,5,
    6, 7, 8, 15,16,10,
    11,12,13,14,22,17,
    18,19,20,21,23,24]
s6=[3,1,4,9,2,5,
    6, 7, 8, 14,21,10,
    11,12,13,15,16,17,
    18,19,20,22,23,24]
for i in range(24):
    s4[i]-=1
    s6[i]-=1
s3=s5=s4

a=[]
def st(s,t):
    ec=[0 for i in range(24)]
    for i in range(24):
        ec[s[i]]=t[i]
    return ec

def change(start,end,sp=200):
    global a
    for i in range(24):
        end[i][0]-=start[i][0]
        end[i][1]-=start[i][1]
        end[i][0]/=sp
        end[i][1]/=sp
    for j in range(sp):
        d=[[0,0] for i in range(24)]
        for i in range(24):
            d[i][0]=start[i][0]+end[i][0]*j
            d[i][1]=start[i][1]+end[i][1]*j
        a.append(d)
    

ss=[st(s1,t1),st(s2,t2),st(s4,t4),st(s5,t5),st(s3,t3),st(s6,t6)]

for i in range(6):
    for j in range(24):
        ss[i][j][0]*=2
        if i!=5:
            ss[i][j][1]*=2
        else:
            ss[i][j][1]*=1.7
        if i==2:
            ss[i][j][1]-=40

for i in range(6):
    for j in range(24):
        ss[i][j][0]+=width/2
        ss[i][j][1]-=height/2
        ss[i][j][1]*=-1
        
sp=[200 for i in range(5)]
for i in range(5):
    change(ss[i+1],ss[i],sp=sp[i])
b=[]
for i in range(5):
    if i:
        b+=a[sp[i]*(i+1)-1:sp[i]*i-1:-1]
    else:
        b+=a[sp[i]-1::-1]
add=(890,2720,1680,1680,1400)
su=0
for i in range(5):
    for j in range(add[i]):
        b.insert(su,b[su])
    su+=add[i]+sp[i]
b.append(ss[5])
n=0
flag=False
pygame.mixer.music.play()

while True:
    clock.tick(60)
    screen.fill((255,255,255))
    
    for i in range(24):
        pos=(b[n][i][0],b[n][i][1])
        pos2=(b[n][i][0]-(5 if i<9 else 10),b[n][i][1]-10)  
        pygame.draw.circle(screen,(210,230,250) if sex[i] else (230,210,250),pos,15)
        screen.blit(num[i],pos2)
        screen.blit(nameimage[i],(800,i*20+50))
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
    n+=1
    if n>=len(b):
        n=len(b)-1
            
    pygame.display.update()

