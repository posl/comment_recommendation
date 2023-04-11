#問題文
#二次元平面に，赤い点と青い点が N 個ずつあります。
#i 個目の赤い点の座標は (a_i, b_i) で，i 個目の青い点の座標は (c_i, d_i) です。
#赤い点と青い点は，赤い点の x 座標が青い点の x 座標より小さく，
#また赤い点の y 座標も青い点の y 座標より小さいとき，仲良しペアになれます。
#あなたは最大で何個の仲良しペアを作ることができますか？
#ただし，1 つの点が複数のペアに所属することはできません。
#
#制約
#入力は全て整数
#1 ≦ N ≦ 100
#0 ≦ a_i, b_i, c_i, d_i < 2N
#a_1, a_2, ..., a_N, c_1, c_2, ..., c_N はすべて異なる
#b_1, b_2, ..., b_N, d_1, d_2, ..., d_N はすべて異なる
#
#入力
#入力は以下の形式で標準入力から与えられる。
#N
#a_1 b_1
#a_2 b_2
#:
#a_N b_N
#c_1 d_1
#c_2 d_2
#:
#c_N d_N
#
#出力
#仲良しペアの個数の最大値を出力せよ。
#
#入力例 1
#3
#2 0
#3 1
#1 3
#4 2
#0 4
#5 5
#
#出力例 1
#2
#例えば，
#(2, 0) と (4, 2) をペアにし，
#(3, 1) と (5, 5) をペアにすればよいです。
#
#入力例 2
#3
#0 0
#1 1
#5 2
#2 3
#3 4
#4 5
#
#出力例 2
#2
#例えば，
#(0, 0) と (2, 3) をペアにし，
#(1, 1) と (3, 4) をペアにすればよいです。
#
#入力例 3
#2
#2 2
#3 3
#0 0
#1 1
#
#出力例 3
#0
#一つもペアが作れない場合もあります。
#
#入力例 4
#5
#0 0
#7 3
#2 2
#4 8
#1 6
#8 5
#6 9
#5 4
#9 1
#3 7
#
#出力例 4
#5
#
#入力例 5
#5
#0 0
#1 1
#5 5
#6 6
#7 7
#2 2
#3 3
#4 4
#8 8
#9 9
#
#出力例 5
#4

def 