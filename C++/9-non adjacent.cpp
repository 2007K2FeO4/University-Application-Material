#include <bits/stdc++.h>
#define mpvc(x,y) make_pair(x,y)
#define p1 first
#define p2 second
using namespace std;
typedef long long ll;
typedef pair<ll,ll> pvc;//poly vinyl chlorine
map<pvc,bool> mp;
const ll mod=1e9+7;
int c2[4][2]={0,1,1,0,0,-1,-1,0};
int c3[18][4]={{0,1,0,2},{0,1,1,1},{1,0,1,1},{1,0,2,0},{1,0,1,-1},{0,-1,1,-1},
{0,-1,0,-2},{0,-1,-1,-1},{-1,0,-1,-1},{-1,0,-2,0},{-1,0,-1,1},{0,1,-1,1},
{0,1,1,0},{0,1,0,-1},{0,1,-1,0},{1,0,0,-1},{1,0,-1,0},{0,-1,-1,0}};
ll n,m,t,d,k;
bool ok(ll x,ll y){
    if(x<1||x>n||y<1||y>m)return false;
    return mp[mpvc(x,y)]^1;
}
int main(){
    scanf("%lld",&t);
    while(t--) {
        mp.clear();
        scanf("%lld%lld%lld%lld",&n,&m,&k,&d);
        ll ls2=(2*n*m-n-m)%mod,ls3=((n-1)*(m-1)*4%mod+2*n*m-2*n-2*m)%mod;
        if(n==1)ls3+=m;
        if(m==1)ls3+=n;
        ls3%=mod;
        for(int i=0;i<d;i++){
            ll x,y;
            scanf("%lld%lld",&x,&y);
            if(!ok(x,y))continue;
            for(int j=0;j<4;j++)
            if(ok(x+c2[j][0],y+c2[j][1]))ls2--;
            for(int j=0;j<18;j++)
            if(ok(x+c3[j][0],y+c3[j][1])&&ok(x+c3[j][2],y+c3[j][3]))ls3--;
            mp[mpvc(x,y)]=1;
        }
        ll p=(n*m-d)%mod;
        ll ans,inv=166666668;
        if(k==2)ans=((p*(p-1+mod)%mod*(mod+1)/2%mod-ls2)%mod+mod)%mod;
        else ans=((p*(p+mod-1)%mod*(p+mod-2)%mod*inv%mod-ls2*(p-2)%mod+ls3)%mod+mod)%mod;
        printf("%lld\n",ans);
        
    }
    return 0;
}
