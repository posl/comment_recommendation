#問題文
#N 個の整数 A_1,...,A_N が与えられます。
#1≦ i < j ≦ N を満たす全ての i,j の組についての |A_i-A_j| の和を求めてください。
#すなわち、(sum_{i=1}^{N-1}sum_{j=i+1}^{N} |A_i-A_j|) を求めてください。
#
#制約
#2 ≦ N ≦ 2 × 10^5
#|A_i|≦ 10^8
#A_i は整数である。
#
#入力
#入力は以下の形式で標準入力から与えられる。
#N
#A_1 ... A_N
#
#出力
#答えを出力せよ。
#
#入力例 1
#3
#5 1 2
#
#出力例 1
#8
#|5-1|+|5-2|+|1-2|=8 です。
#
#入力例 2
#5
#31 41 59 26 53
#
#出力例 2
#176

def 