'''
1.导入模块，画小蛇，三个正方形
2.方向键控制小蛇移动
3.画食物，位置随机
4.吃掉食物，分数+1
5.碰到墙壁游戏结束，回车重新开始 
作业：1.整理pygame的思维导图
      2.画食物
'''
import pygame,random
from pygame.locals import *
pygame.init()
s=pygame.display.set_mode((1000,600))
c=pygame.time.Clock()
snake_list = [[100,100],[120,100],[140,100]]
snake_head = [140,100]
pos = 20
food=[500,500]
food_image=pygame.image.load('food.png')
food_image=pygame.transform.smoothscale(food_image,(20,20))
move = 'right'
try:
    while True:
        # draw a snake
        c.tick(10)
        s.fill((240,230,250))
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
        if snake_head==food:
            if move == 'up':
                snake_list.insert(0,[snake_list[0][0],snake_list[0][1]-pos])
            if move == 'down':
                snake_list.insert(0,[snake_list[0][0],snake_list[0][1]+pos])
            if move == 'left':
                snake_list.insert(0,[snake_list[0][0]-pos,snake_list[0][1]])
            if move == 'right':
                snake_list.insert(0,[snake_list[0][0]+pos,snake_list[0][1]])
            food=[random.randint(2,47)*20,random.randint(2,27)*20]
        if snake_head[0]<0 or snake_head[0]>1000 or\
           snake_head[1]<0 or snake_head[1]<600:
            pass
        pygame.display.update()
except pygame.error:
    pass