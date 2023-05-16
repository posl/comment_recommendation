#問題文
#以下のような、無限に広い六角形のグリッドがあります。最初、全てのマスは白です。  
#ある六角形のマスは 2 つの整数 i,j を用いて (i,j) と表されます。
#マス (i,j) は以下の 6 つのマスと隣接します。
#(i-1,j-1)
#(i-1,j)
#(i,j-1)
#(i,j+1)
#(i+1,j)
#(i+1,j+1)
#高橋くんは、 N 個のマス (X_1,Y_1),(X_2,Y_2),...,(X_N,Y_N) を黒く塗りました。
#黒いマスがいくつの連結成分をなすか求めてください。
#ただし、ある 2 つの黒いマスが同じ連結成分に属するとは、この 2 つの黒いマスの間をいくつかの隣接する黒いマスを辿って移動できることを指します。  
#
#制約
#入力は全て整数
#1 ≦ N ≦ 1000
#|X_i|,|Y_i| ≦ 1000
#(X_i,Y_i) は相異なる
#
#入力
#入力は以下の形式で標準入力から与えられる。
#N
#X_1 Y_1
#X_2 Y_2
#.
#.
#.
#X_N Y_N
#
#出力
#答えを整数として出力せよ。
#
#入力例 1
#6
#-1 -1
#0 1
#0 2
#1 0
#1 2
#2 0
#
#出力例 1
#3
#高橋くんがマスを黒く塗った後、グリッドは下図の状態になります。
#黒いマスがなす連結成分は以下の 3 つです。
#(-1,-1)
#(1,0),(2,0)
#(0,1),(0,2),(1,2)
#
#入力例 2
#4
#5 0
#4 1
#-3 -4
#-2 -5
#
#出力例 2
#4
#
#入力例 3
#5
#2 1
#2 -1
#1 0
#3 1
#1 -1
#
#出力例 3
#1

def 