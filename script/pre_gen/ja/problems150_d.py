#問題文
#長さ N の偶数からなる正の整数列 A= {a_1,a_2,...,a_N} と、整数 M が与えられます。
#任意の k(1 ≦ k ≦ N) に対して以下の条件を満たす正の整数 X を A の「半公倍数」と定義します。
#X= a_k × (p+0.5) を満たす負でない整数 p が存在する。
#1 以上 M 以下の整数のうちの A の半公倍数の個数を求めてください。
#
#制約
#1 ≦ N ≦ 10^5
#1 ≦ M ≦ 10^9
#2 ≦ a_i ≦ 10^9
#a_i は偶数である。
#入力は全て整数である。
#
#入力
#入力は以下の形式で標準入力から与えられる。
#N M
#a_1 a_2 ... a_N
#
#出力
#1 以上 M 以下の整数のうちの A の半公倍数の個数を出力せよ。
#
#入力例 1
#2 50
#6 10
#
#出力例 1
#2
#15 = 6  × 2.5 
#15 = 10 × 1.5 
#45 = 6  × 7.5 
#45 = 10 × 4.5 
#より、15,45 は A の半公倍数です。1 以上 50 以下の整数に他に A の半公倍数はないので、答えは 2 となります。
#
#入力例 2
#3 100
#14 22 40
#
#出力例 2
#0
#答えが 0 の場合もあります。
#
#入力例 3
#5 1000000000
#6 6 2 6 2
#
#出力例 3
#166666667

def 