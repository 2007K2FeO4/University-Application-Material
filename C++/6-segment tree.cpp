#include<bits/stdc++.h>
#define int long long
using namespace std;
const int N=444422;
int n,m,a[N];
struct seg{
	int l,r,v,tag;
}t[N];
void push_up(int x){
	t[x].v=t[x<<1].v+t[x<<1|1].v;
}
void build(int x,int l,int r){
	t[x].l=l,t[x].r=r;
	if(l>=r){
		t[x].v=a[l];
		return;
	}
	int mid=l+r>>1;
	build(x<<1,l,mid);
	build(x<<1|1,mid+1,r);
	push_up(x);
}
void push_down(int x){
	if(t[x].tag){
		int k=t[x].tag;
		t[x<<1].tag+=k;
		t[x<<1].v+=k*(t[x<<1].r-t[x<<1].l+1);
		t[x<<1|1].tag+=k;
		t[x<<1|1].v+=k*(t[x<<1|1].r-t[x<<1|1].l+1);
		t[x].tag=0;
	}
}
void add(int x,int l,int r,int k){
	if(l<=t[x].l&&r>=t[x].r){
		t[x].v+=k*(t[x].r-t[x].l+1);
		t[x].tag+=k;
		return;
	}
	push_down(x);
	int mid=t[x].l+t[x].r>>1;
	if(l<=mid)add(x<<1,l,r,k);
	if(r>mid)add(x<<1|1,l,r,k);
	push_up(x);
}

int ques(int x,int l,int r){
	if(l<=t[x].l&&r>=t[x].r)return t[x].v;
	push_down(x);
	int mid=t[x].l+t[x].r>>1;
	int ans=0;
	if(l<=mid)ans+=ques(x<<1,l,r);
	if(r>mid)ans+=ques(x<<1|1,l,r);
	return ans;
}
signed main(){
    scanf("%lld %lld",&n,&m);
    for(int i=1;i<=n;i++)
    scanf("%lld",a+i);
    build(1,1,n);
    for(int i=1;i<=m;i++){
    	int p,x,y,k;
    	scanf("%lld",&p);
    	if(p==1){
    		scanf("%lld %lld %lld",&x,&y,&k);
    		add(1,x,y,k);
		}
		else{
    		scanf("%lld %lld",&x,&y);
    		printf("%lld\n",ques(1,x,y));
		}
	}
    
    return 0;
}
