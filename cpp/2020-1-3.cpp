#include <bits/stdc++.h>
using namespace std;

int main(){
  int n,m;
  int x = 0;
  int y = 0;
  vector<int> r;
  cin >> n >> m;
  vector<int> a(n);
  vector<int> b(m);
  for(int i = 0;i < n;i++){
    cin >> a[i];
  }
  for(int j = 0;j < m;j++){
    cin >> b[j];
  }
  sort(a.begin(),a.end());
  sort(b.begin(),b.end());
  while(true){
    if(x >= n || y >= m){
      break;
    }
    if(a.at(x) == b.at(y)){
      r.push_back(a.at(x));
      x++;
      y++;
      continue;
      cout << "same" << endl;
    }
    if(a.at(x) > b.at(y)){
      y++;
      continue;
    }
    if(a.at(x) < b.at(y)){
      x++;
      continue;
    
    }
  }
  sort(r.begin(),r.end());
  for(int z = 0;z < r.size();z++){
    cout << r.at(z) << endl;
  }
}
