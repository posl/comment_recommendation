#問題文
#xy 平面上に 1, 2, ..., N の番号が付けられた N 個の点があります。点 i は (x_i, y_i) にあり、N 個の点の x 座標は互いに異なります。  
#以下の条件を満たす整数の組 (i, j) (i < j) の個数を求めてください。
#点 i と点 j を通る直線の傾きが -1 以上 1 以下である。
#
#制約
#入力は全て整数
#1 ≦ N ≦ 10^3
#|x_i|, |y_i| ≦ 10^3
#i ≠ j ならば x_i ≠ x_j
#
#入力
#入力は以下の形式で標準入力から与えられる。
#N
#x_1 y_1
#.
#.
#.
#x_N y_N
#
#出力
#答えを出力せよ。
#
#入力例 1
#3
#0 0
#1 2
#2 1
#
#出力例 1
#2
#(0, 0) と (1, 2) を通る直線の傾きは 2、
#(0, 0) と (2, 1) を通る直線の傾きは (1/(2))、
#(1, 2) と (2, 1) を通る直線の傾きは -1 です。
#
#入力例 2
#1
#-691 273
#
#出力例 2
#0
#
#入力例 3
#10
#-31 -35
#8 -36
#22 64
#5 73
#-14 8
#18 -58
#-41 -85
#1 -88
#-21 -85
#-11 82
#
#出力例 3
#11

def 