import sys
def myinput(con,status=0):
    flag=True
    while flag:
        try:
            y=input(con)
            x=int(y)
            if x<2 and status==1:
                raise ValueError
            if (x<1 or x>n) and status==2:
                raise ValueError
            if x==0 and status==3:
                raise ValueError
        except:
            if status==2 and y in player:
                x=player.index(y)+1
                print("Input successfully.")
                flag=False
            else:
                print("Input failed. Please try again.")
        else:
            print("Input successfully.")
            flag=False
    return x

def myinput2(con,status=0):
    flag=True
    while flag:
        x=input(con)
        try:
            if x not in player:
                y=int(x)
        except:
            print("Input successfully.")
            flag=False
        else:
            print("Input failed. Please try again.")
            
    return x

f=open("GDY counting.txt","r+")
a=list(f.readlines())
n=0        
flag=True
player=[]
if len(a)==0:
    n=myinput("How many players are there in the game GDY?\n",status=1)
    f.write(str(n)+'\n')
    for i in range(n):
        player.append(myinput2("What's the name of player {}?\n"
        "(At least a non-digit character and do not repeat)\n".format(i+1)))
        if not player[i]:
            player[i]='player {}'.format(i+1)
    for i in player:
        f.write(i+' ')
    f.write('\n')
    a.append([0 for i in range(n)])
    for i in a[0]:
        f.write(str(i)+' ')
    f.write('\n')
    if myinput2("Do you want to start the game?\nIf you don't, click 'q'.\n"
    "Otherwise click any other key except the numbers and the player names.\n")=='q':    
        flag=False
        print("See you next time!")    
else:
    n=int(a.pop(0)[0:-1])
    player=a.pop(0).split(' ')
    player.pop()
    for i in range(len(a)):
        a[i]=a[i].split(' ')
        a[i].pop()
        for j in range(n):
            a[i][j]=int(a[i][j])
    print("There has already been a game of {} players.".format(n))
    if myinput2("Do you want to restore the data?\nIf you do, click 'q'.\n"
    "Otherwise click any other key except the numbers and the player names.\n")=='q':
        f.close()
        f=open("GDY counting.txt","w")
        f.close()
        print("Data restored. Please restart the program to continue.")
        flag=False
    else:
        print("Then continue to count. \nBelow this comes the player list.")
        for i in range(n):
            print(player[i],a[-1][i])

while flag:
    winner=myinput("Who won in the last turn?\nWrite down the index (1~{}) or name.\n".format(n),status=2)
    winner-=1
    cur=[0 for i in range(n)]
    s=0
    for i in range(n):
        if i!=winner:
            sub=abs(myinput("How many points did player {} ({}) lost?\n".format(i+1,player[i]),status=3))
            s+=sub
            cur[i]=a[-1][i]-sub
    cur[winner]=a[-1][winner]+s
    for i in range(n):
        print(player[i],cur[i])
    a.append(cur)
    for i in cur:
        f.write(str(i)+' ')
    f.write('\n')
    sta=myinput2("Do you want to continue?\nIf you don't, "
    "click 'q'.\nAnd click 'u' to undo.\n"
    "Otherwise click any other key except the numbers and the player names.\n")
    if sta=='u':
        print('Undid.')
        a.pop()
    else:
        if sta=='q':    
            flag=False
            print("See you next time!")

f.close()