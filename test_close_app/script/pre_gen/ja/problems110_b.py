#問題文
#この世界は 1 次元世界であり、世界を治める 2 つの帝国はそれぞれ A 帝国、B 帝国と呼ばれています。
#A 帝国の首都は座標 X、B 帝国の首都は座標 Y に位置しています。
#ある日、A 帝国は座標 x_1, x_2, ..., x_N、B 帝国は座標 y_1, y_2, ..., y_M の都市を支配下に置きたくなりました。
#このとき、以下の 3 つの条件をすべて満たす整数 Z が存在すれば、合意が成立して戦争は起きませんが、存在しない場合には戦争が起こります。
#X < Z ≦ Y
#x_1, x_2, ..., x_N < Z
#y_1, y_2, ..., y_M ≧ Z
#戦争が起こるかどうか判定してください。
#
#制約
#入力はすべて整数である
#1 ≦ N, M ≦ 100
#-100 ≦ X < Y ≦ 100
#-100 ≦ x_i, y_i ≦ 100
#x_1, x_2, ..., x_N ≠ X
#x_i はすべて異なる
#y_1, y_2, ..., y_M ≠ Y
#y_i はすべて異なる
#
#入力
#入力は以下の形式で標準入力から与えられる。
#N M X Y
#x_1 x_2 ... x_N
#y_1 y_2 ... y_M
#
#出力
#戦争が起こるなら War、そうでないなら No War を出力せよ。
#
#入力例 1
#3 2 10 20
#8 15 13
#16 22
#
#出力例 1
#No War
#Z = 16 とすれば、次のように 3 つの条件をすべて満たすので合意が成立し、戦争は起きません。
#X = 10 < 16 ≦ 20 = Y
#8, 15, 13 < 16
#16, 22 ≧ 16
#
#入力例 2
#4 2 -48 -1
#-20 -35 -91 -23
#-22 66
#
#出力例 2
#War
#
#入力例 3
#5 3 6 8
#-10 3 1 5 -100
#100 6 14
#
#出力例 3
#War

def 