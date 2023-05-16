#問題文
#2 次元平面上の原点に高橋君がいます。
#高橋君が 1 歩歩くと、いまいる点からのユークリッド距離がちょうど R であるような点に移動することができます(移動先の座標が整数である必要はありません)。これ以外の方法で移動することはできません。
#高橋君が点 (X,Y) に到達するまでに必要な歩数の最小値を求めてください。
#なお、点 (x_1,y_1) と点 (x_2,y_2) のユークリッド距離は ((x_1-x_2)^2+(y_1-y_2)^2)^(1/2) で与えられます。
#
#制約
#1 ≦ R ≦ 10^5
#0 ≦ X,Y ≦ 10^5
#(X,Y) ≠ (0,0)
#入力は全て整数
#
#入力
#入力は以下の形式で標準入力から与えられる。
#R X Y
#
#出力
#高橋君が (X,Y) に到達するまでに必要な歩数の最小値を出力せよ。
#
#入力例 1
#5 15 0
#
#出力例 1
#3
#(0,0) -> (5,0) -> (10,0) -> (15,0) と 3 歩で到達できます。
#2 歩以下で到達することはできないのでこれが最小です。
#
#入力例 2
#5 11 0
#
#出力例 2
#3
#例えば (0,0) -> (5,0) -> (8,4) -> (11,0) と移動すれば良いです。
#
#入力例 3
#3 4 4
#
#出力例 3
#2
#例えば (0,0) -> (2-(((2)^(1/2))/(2)), 2+(((2)^(1/2))/(2))) -> (4,4) と移動すれば良いです。

def 