#問題文
#1 以上 N 以下の整数からなる長さ N の数列 a = (a_1, ..., a_N) が与えられます。
#以下の条件を全て満たす整数 i, j の組の総数を求めてください。
#1 ≦ i < j ≦ N
#min(a_i, a_j) = i
#max(a_i, a_j) = j
#
#制約
#2 ≦ N ≦ 5 × 10^5
#1 ≦ a_i ≦ N  (1 ≦ i ≦ N)
#入力は全て整数
#
#入力
#入力は以下の形式で標準入力から与えられる。
#N
#a_1 ... a_N
#
#出力
#答えを出力せよ。
#
#入力例 1
#4
#1 3 2 4
#
#出力例 1
#2
#(i, j) = (1, 4), (2, 3) が条件を満たします。
#
#入力例 2
#10
#5 8 2 2 1 6 7 2 9 10
#
#出力例 2
#8

def 