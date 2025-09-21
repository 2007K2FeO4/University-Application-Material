'''
1.导入模块，画小蛇，三个正方形
2.方向键控制小蛇移动
3.画食物，位置随机
4.吃掉食物，分数+1
5.碰到墙壁游戏结束，回车重新开始  
重新完成贪吃蛇项目
'''
import pygame,random,time
from pygame.locals import *
pygame.init()
s=pygame.display.set_mode((1000,600))
c=pygame.time.Clock()
def my_init():
    global font,font2,snake_list,snake_head,pos,food,food_list,move,score,over,food_image,food_pos,sound
    font=pygame.font.Font('comic.ttf',30)
    font2=pygame.font.Font('framd.ttf',100)
    snake_list = [[100,100],[120,100],[140,100]]
    snake_head = [140,100]
    pos = 20
    food=[500,500]
    food_list=[]
    for i in range(1,7):
        food_image=pygame.image.load('f{}.png'.format(i))
        food_list.append(pygame.transform.smoothscale(food_image,(20,20)))
        food_image=food_list[0]
    food_pos=[0,0]
    move = 'right'
    score=0
    over=0
my_init()
while True:
    c.tick(10)
    s.fill((240,230,250))
    # score
    score_image=font.render('score:'+str(score),1,(150,100,160))
    s.blit(score_image,(20,20))
    if over:
        s.blit(over_message,(250,240))
        pygame.display.update()
        time.sleep(3)
        while over:
            for event in pygame.event.get():
                if event.type==QUIT:
                    pygame.quit()
                if event.type==KEYDOWN and event.key==K_RETURN:
                    my_init()
                    break
    else:
        # draw a snake
        clr=len(snake_list)
        for i in snake_list:
            pygame.draw.rect(s,(255,255*clr//len(snake_list),0),(i[0],i[1],pos,pos))
            clr-=1
        # move the snake
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
            if event.type==KEYDOWN:
                if event.key==K_UP and move != 'down':
                    move = 'up'
                if event.key==K_DOWN and move != 'up':
                    move = 'down'  
                if event.key==K_LEFT and move != 'right':
                    move = 'left' 
                if event.key==K_RIGHT and move != 'left':
                    move = 'right'                
        if move == 'up':
            snake_head[1] -= pos
        if move == 'down':
            snake_head[1] += pos
        if move == 'left':
            snake_head[0] -= pos
        if move == 'right':
            snake_head[0] += pos                
        snake_list.append(list(snake_head))
        del snake_list[0]
        # draw some food
        s.blit(food_image,food)
        if food==snake_head:
            food=[random.randint(2,47)*pos,random.randint(2,27)*pos]
            food_image=random.choice(food_list)
            snake_list.append([-200,-200])
            score+=1
            if score>=40:
                food_pos=random.choice([[-1,-1],[-1,1],[1,-1],[1,1]])            
            elif score>=20:
                food_pos=random.choice([[1,0],[0,1],[1,1],[-1,1]])
            elif score>=10:
                food_pos=random.choice([[1,0],[0,1],[-1,0],[0,-1]])
        if score>=30:
            food[0]+=food_pos[0]*pos*random.randint(0,2)
            food[1]+=food_pos[1]*pos*random.randint(0,2)
        else:
            food[0]+=food_pos[0]*pos*random.randint(0,1)
            food[1]+=food_pos[1]*pos*random.randint(0,1)        
        if score>=10:
            if food[0]>47*pos:
                food_pos[0]=-1
            if food[0]<2*pos:
                food_pos[0]=1   
            if food[1]>27*pos:
                food_pos[1]=-1
            if food[1]<2*pos:
                food_pos[1]=1        
        # over
        if snake_head[0]<0 or snake_head[0]>=1000 or snake_head[1]<0 or snake_head[1]>=600:
            over_message=font2.render('Game Over',1,(100,50,110))
            over=1

    pygame.display.update()