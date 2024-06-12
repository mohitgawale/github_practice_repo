  #include<iostream>
  #include<vector>
  using namespace std;


  void rectanglePattern(int n){
    for (int i=0; i<n; i++){
      for (int j=0; j<n ; j++){
          cout<<'#';
      }
    cout<<endl;
    }
  }

  void ascendingPatter(int n){
    /* Print *
             **
             ***
    */
    for (int i=0; i<n; i++){
      for (int j=0; j<i ; j++){
          cout<<'*';
      }
    cout<<endl;
    }
  }
  void ascendingPatternwithnumbers(int n){
    /*
    Print 1
          12
          123
    */
    for (int i=1; i<=n; i++){
      for (int j=1; j<=i ; j++){
          cout<<j;
      }
    cout<<endl;
    }
  }

  void increasingNumbers(int n){
    /*
    Print 12345
          11 12 13 14 15
          21  22  23  24  25
    */
    for (int i=0; i<=n; i++){
      for (int j=1; j<=n ; j++){

          cout<< j+ (10*i);
          cout<< "\t";
      }
    cout<<endl;
    }
  }

  void ascendingPatternwithsamenumbers(int n){
    /*
    Print 1
          12
          123
    */
    for (int i=1; i<=n; i++){
      for (int j=1; j<=i ; j++){
          cout<<i;
      }
    cout<<endl;
    }
  }

  void descendingPattern(int n){
    /*
    */
   for (int i=1; i<=n ; i++){
    for (int j=1; j<=n-i+1; j++){
    cout<<'*';
    }
    cout<<endl;
   }
  }

   void descendingPatternwithNumbers(int n){
    /*
    */
   for (int i=1; i<=n ; i++){
    for (int j=1; j<=n-i+1; j++){
    cout<<j;
    }
    cout<<endl;
   }
  }

  void pyramidPattern(int n){
    for(int i=0; i<n; i++){

      for (int j=0;j<=i; j++){
        cout<<' ';
      }
      for (int k=0;k<((n*2)-1)-i*2; k++){
        cout<<'*';
      }
      for (int j=0;j<=i; j++){
        cout<<' ';
      }
    cout<<endl;
    }
  }

  int main(){
    rectanglePattern(4);
    ascendingPatter(5);
    ascendingPatternwithnumbers(5);
    increasingNumbers(5);
    ascendingPatternwithsamenumbers(5);
    descendingPattern(5);
    descendingPatternwithNumbers(5);
     pyramidPattern(5);
    return 0;
  }