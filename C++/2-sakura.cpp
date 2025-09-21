#include<bits/stdc++.h>
using namespace std;
struct sakura{
	int t,c,p;
}a;
const int T[5]={600,60,0,10,1};
int m,t=0;
int f[1444]={0};
char st[5],et[5];
void zeroonepack(int c,int w){
	for(int j=t;j>=c;j--)
	f[j]=max(f[j],f[j-c]+w);
}
void completepack(int c,int w){
	for(int j=c;j<=t;j++)
	f[j]=max(f[j],f[j-c]+w);
}
void multiplepack(int c,int w,int n){
	if(c*n>=t){
		completepack(c,w);
		return;
	}
	int k=1;
	while(k<n){
		zeroonepack(k*c,k*w);
		n-=k;
		k*=2;
	}
	zeroonepack(n*c,n*w);
}
int main(){
	int i,j;
	scanf("%s",st);
	scanf("%s",et);
	cin>>m;
	if(strlen(st)==4){
		for(i=4;i>=1;i--){
			st[i]=st[i-1];
		}
		st[0]='0';
	}
	if(strlen(et)==4){
		for(i=4;i>=1;i--){
			et[i]=et[i-1];
		}
		et[0]='0';
	}
	for(i=0;i<5;i++){
		t+=((int)et[i]-48)*T[i];
		t-=((int)st[i]-48)*T[i];
	}
	for(i=1;i<=m;i++){
		cin>>a.t>>a.c>>a.p;
		if(a.p==0)completepack(a.t,a.c);
		else multiplepack(a.t,a.c,a.p);
	}
	cout<<f[t]<<endl;;
	return 0;
}
