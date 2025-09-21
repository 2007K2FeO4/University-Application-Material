#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
const int N=200711;
int n,p,q,t;
char a[N],b[N];
signed main(){
	scanf("%d",&t);
	while(t--){
		scanf("%d",&n);
		scanf("%s",a+1);
		if(n==2){
			puts(a[1]==a[2]?"RH":"NO");
			continue;
		}
		p=q=0;
		for(int i=1;i<=n;i++){
			switch(a[i]){
				case 'N':p++;break;
				case 'S':p++;break;
				case 'E':q++;break;
				case 'W':q++;break;
			}
		}
		if((p&1)||(q&1))puts("NO");
		else{
			p/=2,q/=2;
			for(int i=1;i<=n;i++){
				switch(a[i]){
					case 'N':b[i]=p>0?'R':'H';p--;break;
					case 'S':b[i]=p<=0?'R':'H';p--;break;
					case 'E':b[i]=q>0?'R':'H';q--;break;
					case 'W':b[i]=q<=0?'R':'H';q--;break;
				}
			}
			int i=1,j=1;
			while(b[i]!='R'&&i<=n)i++;
			while(b[j]!='H'&&j<=n)j++;
			if(i>n){
				i=1,j=1;
				while(a[i]!='S'&&i<=n)i++;
				while(a[j]!='N'&&j<=n)j++;
				if(i>n||j>n){
					i=1,j=1;
					while(a[i]!='E'&&i<=n)i++;
					while(a[j]!='W'&&j<=n)j++;
				}
				b[i]=b[j]='R';
			}
			if(j>n){
				i=1,j=1;
				while(a[i]!='E'&&i<=n)i++;
				while(a[j]!='W'&&j<=n)j++;
				if(i>n||j>n){
					i=1,j=1;
					while(a[i]!='S'&&i<=n)i++;
					while(a[j]!='N'&&j<=n)j++;
				}
				b[i]=b[j]='H';
			}
			b[n+1]=0;
			puts(b+1);
		}
	}
	return 0;
}
