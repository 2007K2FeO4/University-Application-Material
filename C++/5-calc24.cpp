#include<bits/stdc++.h>
using namespace std;
const int inf=1e9;
bool fg[15]={0},flag=true;float s[5]={0};
int num[15]={0},now[15]={0},a,b,c,d,t;
const char ops[4]={'+','-','*','/'};
//(((a-b)-c)-d)
//((a-(b-c))-d)
//(a-((b-c)-d))
//(a-(b-(c-d)))
//((a-b)-(c-d))
float cal(float a,float b,int op){
	switch(op){
		case 0:if(a>=b)return a+b;break;
		case 1:if(a>=b)return a-b;break;
		case 2:if(a>=b)return a*b;break;
		case 3:if(b)return a/b;break;
	}
	return inf;
}
void comb(float a,float b,float c,float d){
	for(int i=0;i<4;i++)
	for(int j=0;j<4;j++)
	for(int k=0;k<4;k++){
		s[0]=cal(cal(cal(a,b,i),c,j),d,k);
		s[1]=cal(cal(a,cal(b,c,i),j),d,k);
		s[2]=cal(a,cal(cal(b,c,i),d,j),k);
		s[3]=cal(a,cal(b,cal(c,d,i),j),k);
		s[4]=cal(cal(a,b,i),cal(c,d,j),k);
		for(int x=0;x<5;x++)
		if(fabs(s[x]-24)<=1e-4){
			flag=false;
			float p,q;
			switch(x){
				case 0:
					p=cal(a,b,i);
					q=cal(p,c,j);
					printf("%f%c%f=%f\n",a,ops[i],b,p);
					printf("%f%c%f=%f\n",p,ops[j],c,q);
					printf("%f%c%f=24\n",q,ops[k],d);break;
				case 1:
					p=cal(b,c,i);
					q=cal(a,p,j);
					printf("%f%c%f=%f\n",b,ops[i],c,p);
					printf("%f%c%f=%f\n",a,ops[j],p,q);
					printf("%f%c%f=24\n",q,ops[k],d);break;
				case 2:
					p=cal(b,c,i);
					q=cal(p,d,j);
					printf("%f%c%f=%f\n",b,ops[i],c,p);
					printf("%f%c%f=%f\n",p,ops[j],d,q);
					printf("%f%c%f=24\n",a,ops[k],q);break;
				case 3:
					p=cal(c,d,i);
					q=cal(b,p,j);
					printf("%f%c%f=%f\n",c,ops[i],d,p);
					printf("%f%c%f=%f\n",b,ops[j],p,q);
					printf("%f%c%f=24\n",a,ops[k],q);break;
				case 4:
					p=cal(a,b,i);
					q=cal(c,d,j);
					printf("%f%c%f=%f\n",a,ops[i],b,p);
					printf("%f%c%f=%f\n",c,ops[j],d,q);
					printf("%f%c%f=24\n",p,ops[k],q);break;
			}
			return;
		}
	}
	return;
}
void arr(int i){
    if(i==4&&flag){
    	now[num[0]]=a;
    	now[num[1]]=b;
    	now[num[2]]=c;
    	now[num[3]]=d;
    	comb(now[0],now[1],now[2],now[3]);
	}
    for(int j=0;j<4;j++){
        if(fg[j]==0){
            num[i]=j;
            fg[j]=1;
            arr(i+1);
            fg[j]=0;
        }
    }
}
int main(){
	flag=true;
	memset(fg,0,sizeof(fg));
	memset(num,0,sizeof(fg));
	cin>>a>>b>>c>>d;
	arr(0);
	if(flag)cout<<"No answer!"<<endl;
	return 0;
}
