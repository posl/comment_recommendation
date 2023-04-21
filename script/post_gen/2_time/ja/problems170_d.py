#問題文
#長さ N の数列 A が与えられます。
#次の性質を満たす整数 i (1 ≦ i ≦ N ) の数を答えてください。
#i ≠ j  である任意の整数 j (1 ≦ j ≦ N) について A_i は A_j で割り切れない
#
#制約
#入力は全て整数
#1 ≦ N ≦ 2 × 10^5
#1 ≦ A_i ≦ 10^6
#
#入力
#入力は以下の形式で標準入力から与えられる。
#N
#A_1 A_2 ... A_N
#
#出力
#答えを出力せよ。
#
#入力例 1
#5
#24 11 8 3 16
#
#出力例 1
#3
#問の性質を満たすのは 2 , 3 , 4 です。
#
#入力例 2
#4
#5 5 5 5
#
#出力例 2
#0
#同じ数が存在する場合に注意してください。
#
#入力例 3
#10
#33 18 45 28 8 19 89 86 2 4
#
#出力例 3
#5

def 