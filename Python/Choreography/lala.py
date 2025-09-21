import turtle,time
from math import *
turtle.colormode(255)
turtle.tracer(False)
turtle.penup()
turtle.hideturtle()

t1=[[-15,60],[15,60]]+[[i,30] for i in range(-30,31,30)]\
    +[[i,0] for i in range(-60,61,30)]\
    +[[i,-30] for i in range(-90,91,30)]\
    +[[i,-60] for i in range(-120,121,40)]
t2=[[i,30] for i in range(-40,41,20)]\
    +[[i,0] for i in range(-60,61,30)]\
    +[[i,-30] for i in range(-90,91,30)]\
    +[[i,-60] for i in range(-90,91,30)]
t3=[[cos(radians(i))*80,sin(radians(i))*80] for i in range(18,360,36)]\
    +[[cos(radians(i))*50,sin(radians(i))*50] for i in range(0,360,36)]\
    +[[20,0],[0,20],[-20,0],[0,-20]]
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
    +[[cos(radians(i))*20,sin(radians(i))*10] for i in range(b1,b1+a1*6,a1)]\
    +[[cos(radians(i))*50,sin(radians(i))*30] for i in range(b2,b2+a2*6,a2)]\
    +[[cos(radians(i))*80,sin(radians(i))*50] for i in range(b3,b3+a3*6,a3)]

s1=[i for i in range(24)]
s2=[2,0,3,1,4]+[i for i in range(5,24)]
s3=[10,5,4,3,6,18,19,21,23,24,
    17,9,2,1,7,11,12,20,22,16,
    15,8,13,14]
s4=[3,1,4,2,9,5,
    6,7,8,15,17,10,
    18,11,13,14,16,24,
    19,12,20,21,22,23]
for i in range(24):
    s3[i]-=1
    s4[i]-=1
s5=s6=s4

def st(s,t):
    ec=[0 for i in range(24)]
    for i in range(24):
        ec[s[i]]=t[i]
    return ec

def show(lis):
    for i in range(24):
        turtle.pencolor(230,210,250)
        turtle.goto(lis[i][0],lis[i][1])
        turtle.dot(20)
        turtle.pencolor(0,0,0)
        turtle.goto(lis[i][0]-5,lis[i][1]-7)
        turtle.write(str(i+1),font=('Arial',10))

def change(start,end,sp=100):
    event=end
    d=start
    lis=[]
    for i in range(24):
        event[i][0]-=start[i][0]
        event[i][1]-=start[i][1]
        event[i][0]/=sp
        event[i][1]/=sp
    print(event)
    for j in range(sp):
        for i in range(24):
            d[i][0]+=event[i][0]
            d[i][1]+=event[i][1]
        lis.append(d)
    return lis

ss=[st(s1,t1),st(s2,t2),st(s3,t3),st(s4,t4),st(s5,t5),st(s6,t6)]
cg=[change(ss[i],ss[i+1]) for i in range(5)]
#####
#for i in cg[0]:
    #print(i)
#####
for i in range(6):
    for j in range(24):
        ss[i][j][0]*=2
        if i!=5:
            ss[i][j][1]*=2
        else:
            ss[i][j][1]*=1.5
        if i==2:
            ss[i][j][1]-=40
        

for i in range(6):
    turtle.clear()
    show(ss[i])
    turtle.update()
    if i==5:
        break
    for j in range(100):
        show(cg[i][j])
        turtle.update()
        time.sleep(0.01)
    time.sleep(5)
#show(ss[5])
    




turtle.done()