# Rubik-s-Cube-Solver

This project concentrates on solving a unsolved Rubik's Cube. The program contains OpenCV libraries and when executed will show a live video from the webcam. When a unsolved Rubik's cube is shown in front of a camera, it will scan the faces of the Rubik's cube. These instructions will be displayed along with the live video in a text format. After a successful scan the program will start to give the instructions on the moves to be made using Augmented arrow on the cube in the live video. When these moves are followed we get the end product of a solved Rubik's Cube within 30 moves.

1.  Clone the repository
	```
	$ git clone https://github.com/swapnil-tayal/Rubik-s-Cube-Solver.git
	```
2.  Run 
	```
	$ pip install opencv-python
	```
3.  Run
	```
	$ pip install numpy
	```

Click below for a sample VIDEO:

[![Watch the video](https://img.youtube.com/vi/BXai7tTxbdE/sddefault.jpg)](https://youtu.be/BXai7tTxbdE)

#pragma GCC optimize("Ofast")
#pragma GCC target("avx,avx2,fma")
#pragma GCC optimization("unroll-loops")
#include <iostream>
#include <bits/stdc++.h>
// #include "utilities.cpp"
using namespace std;
#define int long long
#define pb push_back
#define all(x) x.begin(), x.end()
#define rall(x) x.rbegin(), x.rend()
#define forn(i, x, n) for (int i = x; i < n; i++)
#define vi vector<int>
#define vpp vector<pair<int,int>>
#define vs vector<string>
#define vll vector<long long>
int row[] = {1,0,-1,0};
int col[] = {0,1,0,-1};
const int mod = 1e9 + 7;
// const int mod = 998244353;


void solve(){   

    int n,k;
    cin>>n>>k;

    int a[n], b[n];
    forn(i,0,n) cin>>a[i];
    forn(i,0,n) cin>>b[i];

    int sum = 0;
    forn(i,0,n){
        if(b[i] == 1) sum += a[i];
    }

    int i = 0;
    int j = 0;
    int ans = sum;

    int newSm = 0;

    while(j < n){

        if(b[j] == 0) newSm += a[j];

        if(j-i+1 < k) j++;
        else{

            ans = max(ans, newSm + sum);
            if(b[i] == 0) newSm -= a[i];
            i++; j++;

        }
    }
    cout<<ans<<'\n';
}   

signed main(){

    std::ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    int t = 1;
    // cin >> t;
    while (t--) solve();
    return 0;

}
