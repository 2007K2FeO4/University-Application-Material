import time,random
localtime=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())
print(localtime)
print('%-4d'%20)
#with open('C:/Users/dell/Desktop/8_11/lmhistory_primary.txt','r') as f1:
    #a=f1.read()
    #print(len(a))
ptime=random.randint(100,9999)
ldbd=[]
with open('C:/Users/dell/Desktop/8_11/lmhistory_primary.txt','r') as f1:
    ld=f1.read()
    #localtime=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())
    #f1.write('%s %-4d\n'%(localtime,ptime))    
    if ld:
        print(type(ld))
        ldbd=list(ld.split('\n'))
        ldbd.pop()
        a=0
        for i in range(len(ldbd)):
            t1=int(eval(ldbd[i][20:]))
            if t1>ptime:
                localtime=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())
                ldbd.insert(i,'%s %-4d\n'%(localtime,ptime)) 
                a=1
                break
        if a==0:
            localtime=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())
            ldbd.append('%s %-4d\n'%(localtime,ptime))            
    else:
        localtime=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())
        ldbd.append('%s %-4d\n'%(localtime,ptime))   
print(ldbd)
with open('C:/Users/dell/Desktop/8_11/lmhistory_primary.txt','a+') as f2:
    for i in ldbd:
        f2.write(str(i)+'\n')