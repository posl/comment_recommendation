#問題文
#高橋君は数直線上の座標 0 の位置にいます。
#これから高橋君は N 回のジャンプを行います。i  (1 ≦ i ≦ N) 回目のジャンプでは、正の方向に a_i または b_i 移動します。
#N 回のジャンプの後に座標 X の位置にいるようにすることはできますか？
#
#制約
#1 ≦ N ≦ 100
#1 ≦ a_i < b_i ≦ 100  (1 ≦ i ≦ N)
#1 ≦ X ≦ 10000
#入力は全て整数
#
#入力
#入力は以下の形式で標準入力から与えられる。
#N X
#a_1 b_1
#.
#.
#.
#a_N b_N
#
#出力
#N 回のジャンプの後に座標 X の位置にいるようにすることができるならば Yes と、そうでないなら No と出力せよ。
#
#入力例 1
#2 10
#3 6
#4 5
#
#出力例 1
#Yes
#1 回目のジャンプでは b_1 (= 6) 移動し、2 回目のジャンプでは a_2 (= 4) 移動することで、座標 X (= 10) の位置にいるようにすることができます。
#
#入力例 2
#2 10
#10 100
#10 100
#
#出力例 2
#No
#1 回目のジャンプの後に座標 X (= 10) の位置にいるようにすることはできますが、全てのジャンプの後に座標 X (= 10) の位置にいるようにすることはできません。
#
#入力例 3
#4 12
#1 8
#5 7
#3 4
#2 6
#
#出力例 3
#Yes

def 