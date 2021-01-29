#include <bits/stdc++.h>
using namespace std;

int main(){
  int x;
  string s,r;
  cin >> x >>s;
  vector<char> c(s.begin(),s.end());
  for(int l = 0;l < x;l++){
    if(c.at(l) == 'J'){
      r += 'J';
    }
  }
  for(int z = 0;z < x;z++){
    if(c.at(z) == 'O'){
      r += 'O';
    }
  }
  for(int p = 0;p < x;p++){
    if(c.at(p) == 'I'){
      r += 'I';
    }
  }
  cout << r << endl;
}
  
  
