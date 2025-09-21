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
for i in range(1,6):
    person.append(pygame.image.load('h{}.png'.format(i)))
    person[-1]=pygame.transform.smoothscale(person[-1],(25,25))
pygame.display.set_icon(person[1])
rect_ob1=[]
isdel=0
score=0
score_p=del_p=0
r=0
num=0
d=1
over=False
y=475
t=time.time()
t2=0
lx=0
rtime=random.randint(130,150)
with open('best2.txt','r+') as f1:
    best=int(f1.read())

gray = [[i,i,i] for i in range(0,256)]    # [0] means black,[255] means white
black, white = tuple(gray[0]), tuple(gray[255])

while True:
    if t2%225==0:
        pygame.mixer.music.play()
    t2=round(time.time()-t)
    clock.tick(30)
    if score<=best:
        mes2=font.render('score:'+str(score),1,(150,150,150))
    else:
        mes2=font.render('score:'+str(score),1,(250,250,150))
    screen.fill(white)
    land=(lx,500,2000,300)
    lx-=8    
    pygame.draw.rect(screen,gray[200],land)
    rect_p=Rect(200,y,25,25)
    if y<0:
        d=0
    if Rect(land).colliderect(rect_p) and r<=0 and d:
        r=0
        y=475
    if rtime==0:
        rl=max(random.randint(200-score,240-score),50)
        rh=random.randint(200,400)
        ry=rh+200
        rsize1=(1600,0,rl,rh)
        rsize2=(1600,ry,rl,600-rh)
        rect_ob1.append(list(rsize1))
        rect_ob1.append(list(rsize2))
        rtime=random.randint(50,100)
    else:
        rtime-=1
    for i in rect_ob1:
        if score<25:
            clr=gray[score*10]
        else:
            clr[0]-=2
            clr[0]%=256
            clr[1]-=3
            clr[1]%=256
            clr[2]-=1
            clr[2]%=256             
        i[0]-=min((8+score)*d,32)
        pygame.draw.rect(screen,tuple(clr),i)
        if Rect(i).colliderect(rect_p) and d and r<=0:
            if i[0]<200 and i[1]:
                y=i[1]-25
                r=0
                if i[3]<800:
                    score+=1
                i[3]=800
            else:
                d=0
        #else:
            #r-=1       
        if i[0]<-300:
            isdel=1
    r-=2.5
    if isdel:
        del rect_ob1[0]
        isdel=0 
    y-=r     
    num+=1
    num%=5
    screen.blit(person[num],(200,y))    
    if y>800:
        over=True
    if over:
        pygame.display.update()
        if best<score:
            best=score
            mes4=font.render('# NEW RECORD! #',1,(255,0,0))
            screen.blit(mes4,(500,400))
            with open('best2.txt','w+') as f2:
                f2.write(str(best))
        mes3=font.render('best score:'+str(best),1,(200,200,200))
        screen.blit(mes3,(500,100))
        screen.blit(mes1,(500,300))
        screen.blit(mes2,(500,200))
        
        while True:
            if t2%225==0:
                pygame.mixer.music.play()
            t2=round(time.time()-t)
            event = pygame.event.poll()
            if event.type==QUIT:
                pygame.quit()
            elif event.type==KEYDOWN and event.key==K_RETURN:
                rect_ob1=[]
                isdel=0
                score=0
                score_p=del_p=0
                r=0
                num=0
                d=1
                over=False
                y=475
                lx=0
                rtime=random.randint(130,150)
                break
            pygame.display.update()
            
    else:
        screen.blit(mes2,(500,0))        
    
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
        if event.type==KEYDOWN:
            if event.key==K_1 and d:
                r=20 
    pygame.display.update()