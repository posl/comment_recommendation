#問題文
#xy -平面上の N 個の円が与えられます。
#i = 1, 2, ..., N について、i 番目の円は点 (x_i, y_i) を中心とする半径 r_i の円です。
#N 個の円のうち少なくとも 1 つ以上の円の円周上にある点のみを通って、点 (s_x, s_y) から点 (t_x, t_y) に行くことができるかどうかを判定してください。
#
#制約
#1 ≦ N ≦ 3000
#-10^9 ≦ x_i, y_i ≦ 10^9
#1 ≦ r_i ≦ 10^9
#(s_x, s_y) は N 個の円のうち少なくとも 1 つ以上の円の円周上にある
#(t_x, t_y) は N 個の円のうち少なくとも 1 つ以上の円の円周上にある
#入力はすべて整数
#
#入力
#入力は以下の形式で標準入力から与えられる。
#N
#s_x s_y t_x t_y
#x_1 y_1 r_1
#x_2 y_2 r_2
#.
#.
#.
#x_N y_N r_N
#
#出力
#点 (s_x, s_y) から点 (t_x, t_y) に行くことができる場合は Yes を、そうでない場合は No を出力せよ。
#ジャッジは英小文字と英大文字を厳密に区別することに注意せよ。
#
#入力例 1
#4
#0 -2 3 3
#0 0 2
#2 0 2
#2 3 1
#-3 3 3
#
#出力例 1
#Yes
#例えば、下記の経路で点 (0, -2) から点 (3, 3) へ行くことができます。
#点 (0, -2) から 1 つ目の円の円周上を反時計回りに通って点 (1, -(3)^(1/2)) へ行く。
#点 (1, -(3)^(1/2)) から 2 つ目の円の円周上を時計回りに通って点 (2, 2) へ行く。
#点 (2, 2) から 3 つ目の円の円周上を反時計回りに通って点 (3, 3) へ行く。
#よって、Yes を出力します。
#
#入力例 2
#3
#0 1 0 3
#0 0 1
#0 0 2
#0 0 3
#
#出力例 2
#No
#少なくとも 1 つ以上の円の円周上にある点のみを通って点 (0, 1) から点 (0, 3) に行くことはできないので No を出力します。

def 