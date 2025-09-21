#include<bits/stdc++.h>
using namespace std;
const int N=565450;
typedef long long ll;
int n,m,a[N];
int lowbit(int x){
	return x&-x;
}
void add(int x,int y){
	for(int i=x;i<=n;i+=lowbit(i))a[i]+=y;
}
int ask(int x,int y){
	int s=0;
	for(int i=y;i;i-=lowbit(i))s+=a[i];
	for(int i=x-1;i;i-=lowbit(i))s-=a[i];
	return s;
}
signed main(){
	scanf("%d %d",&n,&m);
	for(int i=1;i<=n;i++)
	scanf("%d",a+i);
	for(int i=2;i<=n;i<<=1)
	for(int j=i;j<=n;j+=i){
		a[j]+=a[j-(i>>1)];
	}
	for(int i=1;i<=m;i++){
		int p,x,y;
		scanf("%d %d %d",&p,&x,&y);
		if(p==1)add(x,y);
		else printf("%d\n",ask(x,y));
	}
	return 0;
}
