#include<iostream>
using namespace std;
int main(){
int N;
cout<<"Number of input symbol: ";
cin>>N;
char symbols[N];
cout<<"Input Symbols: ";
for(int i = 0; i < N; i++){
cin>>symbols[i];
}
int StatesNo;
cout<<"Enter Number of States: ";
cin>>StatesNo;
int initialState;
cout<<"Initial State: ";
cin>>initialState;
int noFinalstate;
cout<<"Number of Accepting state: ";
cin>>noFinalstate;
int acceptingState[noFinalstate];
cout<<"Accepting State: ";
for(int i = 0; i < noFinalstate; i++){
cin>>acceptingState[i];
}
int transtitionTable[StatesNo][N];
cout<<endl<<"Enter Transition Table entries:"<<endl;
for(int i = 1; i <= StatesNo; i++){
for(int j = 0; j < N; j++){
// cout<<"For State "<< i + 1 <<" transition to " << symbols[j] << " is ";
cout<<"For Transition " << i + 1 << " to " << symbols[j] << " is ";
cin>>transtitionTable[i][j];
}
}
string inputStr;
cout<<endl<<"Enter Input String: ";
cin>>inputStr;
cout<<endl;
int currentstate = initialState;
for(int i = 0; i < inputStr.length(); i++){
char ch = inputStr[i];
int symbolidx = -1;
for(int j = 0; j < N; j++){
if(symbols[j] == ch){
symbolidx = j;
break;
}
}
if(symbolidx == -1){
cout<<"Invalid String";
return 0;
}
currentstate = transtitionTable[currentstate][symbolidx];
}
for(int i = 0; i < noFinalstate; i++){
if(currentstate == acceptingState[i]){
cout<<"Valid String"<<endl;
return 0;
}
}
cout<<"Invalid String"<<endl;
return 0;
}