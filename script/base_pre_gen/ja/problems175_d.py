#問題文
#高橋君は 1, 2, ..., N の番号のついた N マスから成るマス目の上で、コマを使ってゲームを行おうとしています。マス i には整数 C_i が書かれています。また、1, 2 …, N の順列 P_1, P_2, ..., P_N が与えられています。
#これから高橋君は好きなマスを 1 つ選んでコマを 1 つ置き、1 回以上 K 回以下の好きな回数だけ、次のような方法でコマを移動させます。
#1 回の移動では、現在コマがマス i (1 ≦ i ≦ N) にあるなら、コマをマス P_i に移動させる。このとき、スコアに C_{P_i} が加算される。
#高橋君のために、ゲーム終了時のスコアとしてあり得る値の最大値を求めてください。(ゲーム開始時のスコアは 0 です。)
#
#制約
#2 ≦ N ≦ 5000
#1 ≦ K ≦ 10^9
#1 ≦ P_i ≦ N
#P_i ≠ i
#P_1, P_2, ..., P_N は全て異なる
#-10^9 ≦ C_i ≦ 10^9
#入力は全て整数である
#
#入力
#入力は以下の形式で標準入力から与えられる。
#N K
#P_1 P_2 ... P_N
#C_1 C_2 ... C_N
#
#出力
#ゲーム終了時のスコアとしてあり得る値の最大値を出力せよ。
#
#入力例 1
#5 2
#2 4 5 1 3
#3 4 -10 -8 8
#
#出力例 1
#8
#好きなマスから始めて 2 回以下コマを移動させる方法は以下の通りです。
#初めマス 1 にコマを置く場合。1 回移動するとマス 2 に動き、スコアが 4 になる。2 回移動するとマス 4 に動き、スコアが 4 + (-8) = -4 になる。
#初めマス 2 にコマを置く場合。1 回移動するとマス 4 に動き、スコアが -8 になる。2 回移動するとマス 1 に動き、スコアが -8 + 3 = -5 になる。
#初めマス 3 にコマを置く場合。1 回移動するとマス 5 に動き、スコアが 8 になる。2 回移動するとマス 3 に動き、スコアが 8 + (-10) = -2 になる。
#初めマス 4 にコマを置く場合。1 回移動するとマス 1 に動き、スコアが 3 になる。2 回移動するとマス 2 に動き、スコアが 3 + 4 = 7 になる。
#初めマス 5 にコマを置く場合。1 回移動するとマス 3 に動き、スコアが -10 になる。2 回移動するとマス 5 に動き、スコアが -10 + 8 = -2 になる。
#これらの最大値は 8 です。
#
#入力例 2
#2 3
#2 1
#10 -7
#
#出力例 2
#13
#
#入力例 3
#3 3
#3 1 2
#-1000 -2000 -3000
#
#出力例 3
#-1000
#最低 1 回はコマを移動させる必要があります。
#
#入力例 4
#10 58
#9 1 6 7 8 4 3 2 10 5
#695279662 988782657 -119067776 382975538 -151885171 -177220596 -169777795 37619092 389386780 980092719
#
#出力例 4
#29507023469
#答えの絶対値は非常に大きくなる場合があります。

def 