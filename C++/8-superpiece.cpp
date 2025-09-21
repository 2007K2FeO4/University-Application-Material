#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
const int dn[8][2]={1,2,2,1,-1,2,2,-1,1,-2,-2,1,-1,-2,-2,-1};
const int dk[8][2]={1,0,1,1,0,1,-1,1,-1,0,-1,-1,0,-1,1,-1};
int q,a,b,c,d;
char s[8];
bool v[8];//1=Pawn,2=Rook,3=kNight,4=Bishop,5=Queen,6=King
int knight(int x,int y){
	int ans;
	if((x==0&&y==1)||(x==1&&y==0))ans=3;
	else if(x==2&&y==2)ans=4;
	else{
		int gr=max(max((x+1)/2,(y+1)/2),(x+y+2)/3);
		ans=((gr^x^y)&1)+gr;
	}
	return ans;
}
signed main(){
	scanf("%d",&q);
	while(q--){
		memset(s,0,sizeof(s));
		memset(v,0,sizeof(v));
		scanf("%s",s+1);
		scanf("%d %d %d %d",&a,&b,&c,&d);
		for(int i=1;i<=6;i++){
			switch(s[i]){
				case 'P':v[1]=1;break;
				case 'R':v[2]=1;break;
				case 'N':v[3]=1;break;
				case 'B':v[4]=1;break;
				case 'Q':v[5]=1;break;
				case 'K':v[6]=1;break;
			}
		}
		//for(int i=1;i<=6;i++)printf("%d",v[i]);
		if(v[5]){//q
			int ans=2;
			if(v[3]){//n
				for(int i=0;i<8;i++)
				if(a+dn[i][0]==c&&b+dn[i][1]==d){
					ans=1;break;
				}
			}
			if(a==c||b==d||a-c==b-d||a-c==d-b)ans=1;
			printf("%d\n",ans);
		}
		else if(v[2]){//r
			int ans=2;
			if(v[3]){//n
				for(int i=0;i<8;i++)
				if(a+dn[i][0]==c&&b+dn[i][1]==d){
					ans=1;break;
				}
			}
			if(v[6]){//k
				for(int i=1;i<8;i+=2)
				if(a+dk[i][0]==c&&b+dk[i][1]==d){
					ans=1;break;
				}
			}
			if(v[4]&&(a-c==b-d||a-c==d-b))ans=1;//b
			if(a==c||b==d)ans=1;
			printf("%d\n",ans);
		}
		else if(v[4]){//b
			if((a^b^c^d)&1){//odd
				int ans=3;
				bool fg=true;
				if(v[3]){//n
					fg=false;
					for(int i=0;i<8;i++){
						int na=a+dn[i][0],nb=b+dn[i][1];
						if(na==c&&nb==d){
							ans=1;break;
						}
						else if(na-c==nb-d||na-c==d-nb){
							ans=min(ans,2);
						}
					}
				}
				if(v[6]){//k
					fg=false;
					for(int i=0;i<8;i+=2){
						int na=a+dk[i][0],nb=b+dk[i][1];
						if(na==c&&nb==d){
							ans=1;break;
						}
						else if(na-c==nb-d||na-c==d-nb){
							ans=min(ans,2);
						}
					}
				}
				if(v[1]){//p
					fg=false;
					if(a+1==c&&b==d)ans=1;
					else if(a+1-c==b-d||a+1-c==d-b)ans=min(ans,2);
				}
				if(fg)puts("-1");//no
				else printf("%d\n",ans);//yes
			}
			else{//even
				if(a-c==b-d||a-c==d-b)puts("1");
				else puts("2");
			}
		}
		else if(v[3]){//n
			//int x=abs(a-c),y=abs(b-d);
			int ans=knight(abs(a-c),abs(b-d));
			if(v[1])ans=min(ans,1+knight(abs(a-c+1),abs(b-d)));
			if(v[6]){
				for(int i=0;i<8;i++)
				ans=min(ans,1+knight(abs(a-c+dk[i][0]),abs(b-d+dk[i][1])));
			}//ans=min(min(min(ans,1+knight(x-1,y)),
			//1+min(knight(x,y-1),knight(x-1,y-1))),1+knight(x-1,y+1));
			printf("%d\n",ans);
		}
		else if(v[6])printf("%d\n",max(abs(a-c),abs(b-d)));//k
		else if(a<c&&b==d)printf("%d\n",c-a);//p
		else puts("-1");
	}
	
	return 0;
}
