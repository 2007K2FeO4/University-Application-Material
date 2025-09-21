import turtle,math,random
turtle.hideturtle()
turtle.colormode(255)
turtle.pu()
turtle.tracer(False)
turtle.screensize(1000,800)
turtle.bgcolor(0,0,0)
clr=[(25,20,50),(70,30,90),(100,40,120),
     (150,50,200),(200,100,250),(230,220,250)]

def piece(size):
    turtle.begin_fill()
    turtle.pd()
    turtle.right(30)
    turtle.circle(size*2*(2+3**0.5),30)
    turtle.circle(size,180)
    turtle.circle(size*2*(2+3**0.5),30)
    turtle.left(150)
    turtle.pu()
    turtle.end_fill()

def flower(pienum,size):
    for i in range(pienum):
        turtle.right(360/pienum)
        piece(size)
        
def lavender():
    # dress
    for i in range(6):
        for j in range(i*10+100):
            direc=random.randint(225,315)
            length=random.randint(0,1000)
            size=int(length/100*random.uniform(0.5,1.5))
            color=clr[i]
            pienum=random.randint(4,8)
            turtle.pencolor(color)
            turtle.fillcolor(color)
            turtle.goto(0,0)
            turtle.seth(direc)
            turtle.forward(length)
            turtle.right(direc*length)
            flower(pienum,size)
    # body
    size=list(range(3,8))*2+[10,15]
    pienum=[i//2 for i in range(8,13)]*2+[6,8]
    color=[i//2 for i in range(2,7)]*2+[4,5]
    pos=[(i*(abs(i)+5)*2,-abs(i)*10) for i in range(-9,10,2)]+[(0,50),(0,-30)]
    pos[5],pos[9]=pos[9],pos[5]
    pos[6],pos[8]=pos[8],pos[6]
    for i in range(12):
        turtle.seth(0)
        turtle.pencolor(clr[color[i]])
        turtle.fillcolor(clr[color[i]])        
        turtle.goto(pos[i][0],pos[i][1]) 
        flower(pienum[i],size[i])       
        

lavender()
turtle.update()
turtle.done()