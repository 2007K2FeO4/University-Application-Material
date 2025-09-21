'''
1.导入模块，画地面
2.加载人物图
3.实现人物跳跃
4.障碍物
5.碰到游戏结束
作业：障碍物时间随机 或者 障碍物有多个且都向左移动
'''
import pygame,random,time
from pygame.locals import *
pygame.init()
screen=pygame.display.set_mode((1200,600),RESIZABLE)
pygame.display.set_caption('run')
clock=pygame.time.Clock()
pygame.mixer.music.load('lone.mp3')
font=pygame.font.Font('comic.ttf',50)
mes1=font.render('game over',1,(100,100,100))
person=[]
for i in range(1,7):
    person.append(pygame.image.load('2h{}.png'.format(i)))
pygame.display.set_icon(person[1])
rect_ob=[]
color_ob=[]
isdel=0
score=0
r=0
num=0
d=1
over=False
y=445
lie=0
t=time.time()
t2=0
rtime=random.randint(30,50)
with open('best.txt','r+') as f1:
    best=int(f1.read())
while True:
    if t2%225==0:
        pygame.mixer.music.play()
    t2=round(time.time()-t)
    if score<=best:
        mes2=font.render('score:'+str(score),1,(150,150,150))
    else:
        mes2=font.render('score:'+str(score),1,(250,250,150))    
    y-=r
    if y>800:
        over=True
    elif y>445 and d:
        y=445
        r=0
    clock.tick(30)
    screen.fill((255,255,255))
    pygame.draw.rect(screen,(0,0,0),(0,500,1600,5))
    if rtime==0:
        if score<30:
            rmode=random.randint(1,3)
        else:
            rmode=random.randint(1,4)            
        if rmode==1:
            rl=min(random.randint(20+score,100+score),175)
            rh=random.randint(30,40)
            ry=500-rh
            rc=(100,100,100)
        elif rmode==2:
            rl=min(random.randint(120+score,150+score),225)
            rh=20
            ry=500
            rc=(255,255,255)
        elif rmode==3:
            rl=random.randint(20+score//3,30+score//2)
            rh=random.randint(1,12)*25
            ry=460-rh
            rc=(100,100,100)
        else:
            rl=random.randint(30+score//3,40+score//3)
            rh=random.randint(30,40)
            ry=random.randint(300,480)
            rc=(200,0,0)
        if rmode!=4:
            rsize=(1600,ry,rl,rh)
        else:
            rsize=(3300,ry,rl,rh)
        rect_ob.append(list(rsize))
        color_ob.append(rc)
        rtime=max(random.randint(30-score//10,50-score//10),10)
    else:
        rtime-=1    
    for i in range(len(color_ob)):
        pygame.draw.rect(screen,color_ob[i],rect_ob[i])
        if color_ob[i]==(200,0,0):
            ry=rect_ob[i][1]+rect_ob[i][3]/2
            pygame.draw.line(screen,(200,0,0),(0,ry),(rect_ob[i][0],ry),1)
            rect_ob[i][0]-=15+score*3//2
        else:
            rect_ob[i][0]-=15+score//3
        if rect_ob[i][0]<-200:
            isdel=1
        if Rect(rect_ob[i]).colliderect(rect_p):
            if color_ob[i]!=(255,255,255):
                if color_ob[i]==(200,0,0):
                    over=True
                elif rect_ob[i][0]>45 and rect_ob[i][1]>=460:
                    over=True
                elif rect_ob[i][1]<y<460:
                    over=True
                else:
                    y=rect_ob[i][1]-ph
                    r=0
            else:
                #print(rect_ob[i][0],50-rect_ob[i][2])
                if (72-rect_ob[i][2]<rect_ob[i][0]<72 and num!=5)\
                   or (75-rect_ob[i][2]<rect_ob[i][0]<75 and num==5):
                    d=0
        elif color_ob[i]==(255,255,255) and y<445:
            d=1
    num+=1
    if lie==0:
        num%=5
        ph=60
        screen.blit(person[num],(45,y))
        rect_p=Rect(45,y,45,ph)
    else:
        num=5
        ph=25
        screen.blit(person[num],(45,y+37))
        rect_p=Rect(45,y+37,60,ph)           
    if isdel:
        score+=1
        if color_ob:
            del rect_ob[0]
            del color_ob[0]
        isdel=0
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
        if event.type==KEYDOWN:
            if event.key==K_1 and lie==0 and r==0:
                r=30
            if event.key==K_2:
                lie=1
                for i in rect_ob:
                    if not Rect(i).colliderect(rect_p):
                        y=445
        if event.type==KEYUP:
            if event.key==K_2:
                lie=0 
    if over:
        pygame.display.update()
        if best<score:
            best=score
            mes4=font.render('# NEW RECORD! #',1,(255,0,0))
            screen.blit(mes4,(300,400))
            with open('best.txt','w+') as f2:
                f2.write(str(best))
        mes3=font.render('best score:'+str(best),1,(200,200,200))
        screen.blit(mes3,(300,100))
        screen.blit(mes1,(300,300))
        screen.blit(mes2,(300,200))
        
        while True:
            if t2%225==0:
                pygame.mixer.music.play()
            t2=round(time.time()-t)
            event = pygame.event.poll()
            if event.type==QUIT:
                pygame.quit()
            elif event.type==KEYDOWN and event.key==K_RETURN:
                rect_ob=[]
                color_ob=[]
                r=0
                score=0
                num=0
                d=1
                over=False
                y=445
                lie=0
                rtime=random.randint(30,60)
                break
            pygame.display.update()
    else:
        screen.blit(mes2,(300,0))     
    r-=2.5
    pygame.display.update()
    
    