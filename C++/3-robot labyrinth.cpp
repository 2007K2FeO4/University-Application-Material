#include<bits/stdc++.h>
using namespace std;
struct node{
    int x,y,dir;
}q[10800]={0};
int d[4][2]={1,0,0,1,-1,0,0,-1};
int a[52][52]={0},b[52][52][4]={0};
int n,m,ans;
void bfs(int sx,int sy,int sd,int ex,int ey){
    int i,l=0,r=0;node h;
    memset(b,-1,sizeof(b));
    if(a[sx][sy]||a[ex][ey]){
    	ans=-1;
    	return;
	}
	if(sx==ex&&sy==ey){
		ans=0;
		return;
	}
    q[r].x=sx;
    q[r].y=sy;
    q[r++].dir=sd;
    b[sx][sy][sd]=0;
    while(l<r){
        h=q[l++];
        for(i=0;i<5;i++){
        	int tmp=i;
        	if(tmp>2)tmp=2;
        	int fd=0;
			int x=h.x;
        	int y=h.y;
        	int dir=h.dir;
        	switch(tmp){
        		case 0:
        			dir--;
					if(dir<0)dir+=4;
					break;
        		case 1:
        			dir++;
					if(dir>=4)dir-=4;
					break;
				case 2:
					fd=i-1;
					x=h.x+d[h.dir][0]*fd;
        			y=h.y+d[h.dir][1]*fd;
        			break;
			}
			if(x<1||x>=n||y<1||y>=m||
	        b[x][y][dir]!=-1)continue;
	        if(a[x][y])break;
	        q[r].dir=dir,q[r].x=x,q[r++].y=y;
	        b[x][y][dir]=b[h.x][h.y][h.dir]+1;
	        if(x==ex&&y==ey){
	            ans=b[x][y][dir];
	            return;
	        }
		}
    }
    ans=-1;
    return;
}
int main(){
    int i,j,p,sx,sy,ex,ey,sd;char c;
    cin>>n>>m;
    for(i=1;i<=n;i++){
        for(j=1;j<=m;j++){
            scanf("%d",&p);
            if(p){
            	a[i][j]=a[i-1][j]=1;
				a[i][j-1]=a[i-1][j-1]=1;
			}
        }
    }
    cin>>sx>>sy>>ex>>ey>>c;
    switch(c){
    	case 'E':sd=1;break;
    	case 'S':sd=0;break;
    	case 'W':sd=3;break;
    	case 'N':sd=2;break;
	}
    bfs(sx,sy,sd,ex,ey);
    cout<<ans<<endl;
    return 0;
}
/*
10 10
0 0 0 0 0 0 0 0 0 0
0 1 0 0 1 0 0 1 0 0
0 0 0 0 0 0 0 0 0 0
0 0 1 0 0 1 0 0 0 0
0 0 0 0 0 0 0 0 0 1
0 0 0 1 0 0 0 0 1 1
0 0 0 0 0 0 1 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 1 1 1 0 0 0 0 1
0 0 0 0 0 0 0 0 0 0
9 1 1 9 N

0 0
0 0
0 0
0 0
0 0
0 0
0 0
0 0
0 0
0 0

*/

