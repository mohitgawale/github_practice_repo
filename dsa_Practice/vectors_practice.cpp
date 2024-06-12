  #include<iostream>
  #include<vector>
  using namespace std;

int main(){
  cout<< "Test Function";
  
  vector<int> v;
  v.push_back(300);
  v.push_back(100);
  // cout<< " "<<v[0]<< endl;

  for (vector<int>::iterator it = v.begin(); it != v.end();it++ ){
    cout<< *(it) << endl;
  }

  v.erase(v.begin());
  
   for (vector<int>::iterator it = v.begin(); it != v.end();it++ ){
    cout<<" after erasing";
    cout<< *(it) << endl;
  }
  return 0;
}

