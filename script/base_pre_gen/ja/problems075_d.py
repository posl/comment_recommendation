#問題文
#2次元座標上に N 個の点があります。 
#i(1≦i≦N) 番目の点の座標は (x_i,y_i) です。 
#長方形の内部に N 点のうち K 個以上の点を含みつつ、それぞれの辺がX軸かY軸に平行な長方形を考えます。
#このとき、長方形の辺上の点は長方形の内部に含みます。 
#それらの長方形の中で、最小の面積となるような長方形の面積を求めてください。   
#
#制約
#2≦K≦N≦50 
#-10^9≦x_i,y_i≦10^9 (1≦i≦N) 
#x_i≠x_j (1≦i<j≦N) 
#y_i≠y_j (1≦i<j≦N) 
#入力値はすべて整数である。(21:50 追記)
#
#入力
#入力は以下の形式で標準入力から与えられる。  
#N K  
#x_1 y_1
#:  
#x_{N} y_{N}
#
#出力
#条件を満たす長方形の中で最小面積となるような長方形の面積を出力せよ。   
#
#入力例 1
#4 4
#1 4
#3 3
#6 2
#8 1
#
#出力例 1
#21
#条件を満たす最小面積となる長方形の 1 つは　(1,1),(8,1),(1,4),(8,4) の 4 つの頂点で構成されます。
#その面積は (8-1) × (4-1) = 21 であるため、21 と出力します。
#
#入力例 2
#4 2
#0 0
#1 1
#2 2
#3 3
#
#出力例 2
#1
#
#入力例 3
#4 3
#-1000000000 -1000000000
#1000000000 1000000000
#-999999999 999999999
#999999999 -999999999
#
#出力例 3
#3999999996000000001
#オーバーフローに注意してください。

def 