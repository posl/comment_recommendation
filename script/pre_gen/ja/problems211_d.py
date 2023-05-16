#問題文
#AtCoder 国には 1 から N の番号がついた N 個の都市と、1 から M の番号がついた M 個の道路があります。
#道路 i を通ると都市 A_i と都市 B_i の間を双方向に 1 時間で移動することができます。
#都市 1 から都市 N へ最も早く移動することができる経路は何通りありますか？
#答えは非常に大きくなる可能性があるので (10^9+7) で割ったあまりを求めてください。
#
#制約
#2 ≦ N ≦ 2× 10^5
#0 ≦ M ≦ 2× 10^5
#1 ≦ A_i < B_i ≦ N
#(A_i,B_i) は相異なる
#入力に含まれる値は全て整数である
#
#入力
#入力は以下の形式で標準入力から与えられる。
#N M
#A_1 B_1
#.
#.
#.
#A_M B_M
#
#出力
#答えを出力せよ。
#都市 1 から都市 N へ移動することが出来ない場合は 0 と出力せよ。
#
#入力例 1
#4 5
#2 4
#1 2
#2 3
#1 3
#3 4
#
#出力例 1
#2
#都市 1 から都市 4 へは最短 2 時間で移動することができ、それを実現する経路は 1 -> 2 -> 4 と 1 -> 3 -> 4 の 2 つです。
#
#入力例 2
#4 3
#1 3
#2 3
#2 4
#
#出力例 2
#1
#都市 1 から都市 4 へは最短 3 時間で移動することができ、それを実現する経路は 1 -> 3 -> 2 -> 4 の 1 つです。
#
#入力例 3
#2 0
#
#出力例 3
#0
#都市 1 から都市 2  に移動することはできません。この場合 0 を出力してください。
#
#入力例 4
#7 8
#1 3
#1 4
#2 3
#2 4
#2 5
#2 6
#5 7
#6 7
#
#出力例 4
#4

def 