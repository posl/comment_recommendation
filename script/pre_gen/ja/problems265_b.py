#問題文
#高橋君はゲームの中で洞窟を探索しています。
#洞窟は N 個の部屋が一列に並んだ構造であり、入り口から順に部屋 1,2,...,N と番号がついています。  
#最初、高橋君は部屋 1 におり、持ち時間 は T です。
#各 1 ≦ i ≦ N-1 について、持ち時間を A_i 消費することで、部屋 i から部屋 i+1 へ移動することができます。これ以外に部屋を移動する方法はありません。
#また、持ち時間が 0 以下になるような移動は行うことができません。
#洞窟内には M 個のボーナス部屋があります。i 番目のボーナス部屋は部屋 X_i であり、この部屋に到達すると持ち時間が Y_i 増加します。
#高橋君は部屋 N にたどりつくことができますか？
#
#制約
#2 ≦ N ≦ 10^5
#0 ≦ M ≦ N-2
#1 ≦ T ≦ 10^9
#1 ≦ A_i ≦ 10^9 
#1 < X_1 < ... < X_M < N
#1 ≦ Y_i ≦ 10^9
#入力に含まれる値は全て整数である
#
#入力
#入力は以下の形式で標準入力から与えられる。
#N M T
#A_1 A_2 ... A_{N-1}
#X_1 Y_1
#X_2 Y_2
#.
#.
#.
#X_M Y_M
#
#出力
#高橋君が部屋 N にたどりつくことができるなら Yes を、できないなら No を出力せよ。
#
#入力例 1
#4 1 10
#5 7 5
#2 10
#
#出力例 1
#Yes
#高橋君は最初、部屋 1 にいて持ち時間は 10 です。
#持ち時間を 5 消費して部屋 2 に移動します。持ち時間は 5 になります。その後、持ち時間が 10 増え 15 になります。
#持ち時間を 7 消費して部屋 3 に移動します。持ち時間は 8 になります。
#持ち時間を 5 消費して部屋 4 に移動します。持ち時間は 3 になります。
#
#入力例 2
#4 1 10
#10 7 5
#2 10
#
#出力例 2
#No
#部屋 1 から部屋 2 へ移動することができません。

def 