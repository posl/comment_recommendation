#問題文
#長さ N の数列 A が与えられます。
#各要素同士の差の 2 乗の和、すなわち  sum_{i = 2}^{N} sum_{j = 1}^{i - 1} (A_i - A_j)^2 を求めてください。  
#
#制約
#2 ≦ N ≦ 3 × 10^5
#|A_i| ≦ 200
#入力に含まれる値は全て整数
#
#入力
#入力は以下の形式で標準入力から与えられる。
#N
#A_1 A_2 A_3 ... A_N
#
#出力
#答えを出力せよ。  
#
#入力例 1
#3
#2 8 4
#
#出力例 1
#56
#sum_{i = 2}^{N} sum_{j = 1}^{i - 1} (A_i - A_j)^2 = (8 - 2)^2 + (4 - 2) ^ 2 + (4 - 8) ^ 2 = 56 です。  
#
#入力例 2
#5
#-5 8 9 -4 -3
#
#出力例 2
#950

def 