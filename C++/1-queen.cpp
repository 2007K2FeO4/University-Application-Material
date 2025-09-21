#include<bits/stdc++.h>
using namespace std;
bool fg[20];
int num[20],n,k=3,s=0;
bool judge(int k){
	for(int i=0;i<k;i++)
	if(num[i]+k==i+num[k]||
	num[i]+i==k+num[k])
	return false;
	return true;
}
void arr(int i){
    if(i==n){
    	s++;
        if(--k>=0){
        	for(int j=0;j<n;j++)
        	printf("%d ",num[j]+1);
        	puts("");
		}
    }
    for(int j=0;j<n;j++){
        if(fg[j]==0){
            num[i]=j;
            fg[j]=1;
            if(judge(i))arr(i+1);
            fg[j]=0;
        }
    }
}
int main(){
    scanf("%d",&n);
    arr(0);
    printf("%d",s);
    return 0;
}
