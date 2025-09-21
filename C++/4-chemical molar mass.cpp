#include<bits/stdc++.h>
using namespace std;
const int N=1e5+5;
typedef long long ll;
float m=0;string s;
pair<string,float> mas[120]={
	make_pair("X",0),//invalid
	make_pair("H",1),
	make_pair("He",4),
	make_pair("Li",7),
	make_pair("Be",9),
	make_pair("B",11),
	make_pair("C",12),
	make_pair("N",14),
	make_pair("O",16),
	make_pair("F",19),
	make_pair("Ne",20),
	make_pair("Na",23),
	make_pair("Mg",24),
	make_pair("Al",27),
	make_pair("Si",28),
	make_pair("P",31),
	make_pair("S",32),
	make_pair("Cl",35.5),
	make_pair("Ar",40),
	make_pair("K",39),
	make_pair("Ca",40),
	make_pair("Sc",45),
	make_pair("Ti",48),
	make_pair("V",51),
	make_pair("Cr",52),
	make_pair("Mn",55),
	make_pair("Fe",56),
	make_pair("Co",59),
	make_pair("Ni",59),
	make_pair("Cu",64),
	make_pair("Zn",65),
	make_pair("Ga",70),
	make_pair("Ge",73),
	make_pair("As",75),
	make_pair("Se",79),
	make_pair("Br",80),
	make_pair("Kr",84),
	make_pair("Ag",108),
	make_pair("I",127),
	make_pair("Xe",131),
	make_pair("Ba",137),
	make_pair("Hf",178.5),
	make_pair("Pt",195),
	make_pair("Au",197),
	make_pair("Hg",201),
	make_pair("Pb",207)
	//I wrote this in order to help myself!
};
float getm(string x){
	for(int i=1;i<=120;i++)
	if(x==mas[i].first)return mas[i].second; 
}
void h2o(int x){
	int t=0;
	for(int i=x;s[i]!='H';i++)
	t=t*10+s[i]-48;
	if(!t)t=1;
	m+=t*18;
}
float gset(int i){
	float mm=0,pp=0;
	int p=s.find(')');
	for(;i<p;)
		if(s[i]=='_'){
			i+=2;
			int t=0;
			while(s[i]!='}')t=t*10+s[i++]-48;
			pp*=t;
			i++;
		}
		else{
			mm+=pp;
			pp=0;
			if(s[i+1]>='a'&&s[i+1]<='z')
			pp=getm(s.substr(i,2)),i+=2;
			else pp=getm(s.substr(i,1)),i++;
		}
	if(i==p)mm+=pp;
	return mm;
}
void sol(){
	int len=s.length();
	float p=0;
	int i;
	for(i=0;i<len;){
		if(s[i]=='~'){
			m+=p;
			h2o(i+1);
			break;
		}
		else if(s[i]=='('){
			m+=p;
			p=gset(i+1);
			while(s[i]!=')')i++;
			i++;
			continue;
		}
		else if(s[i]=='_'){
			i+=2;
			int t=0;
			while(s[i]!='}')t=t*10+s[i++]-48;
			p*=t;
			i++;
		}
		else{
			m+=p;
			p=0;
			if(s[i+1]>='a'&&s[i+1]<='z')
			p=getm(s.substr(i,2)),i+=2;
			else p=getm(s.substr(i,1)),i++;
		}
	}
	if(i==len)m+=p;
}
int main(){
	int i,j;
	cin>>s;
	sol();
	if(m-(int)m<=1e-4)
	printf("%.0f",m);
	else printf("%.1f",m);
	return 0;
}

