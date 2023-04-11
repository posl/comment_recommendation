#問題文
#N 個のサイコロが左から右に一列に並べてあります。左から i 番目のサイコロは 1 から p_i までの p_i 種類の目がそれぞれ等確率で出ます。
#隣接する K 個のサイコロを選んでそれぞれ独立に振ったとき、出る目の合計の期待値の最大値を求めてください。
#
#制約
#1 ≤ K ≤ N ≤ 200000
#1 ≤ p_i ≤ 1000
#入力で与えられる値は全て整数
#
#入力
#入力は以下の形式で標準入力から与えられる。
#N K
#p_1 ... p_N
#
#出力
#隣接する K 個のサイコロを選んで振ったときに出る目の合計の期待値の最大値を出力せよ。
#なお、想定解答との絶対誤差または相対誤差が 10^{-6} 以下であれば正解として扱われる。
#
#入力例 1
#5 3
#1 2 2 4 5
#
#出力例 1
#7.000000000000
#左から 3 番目、4 番目、5 番目のサイコロを振った時、出る目の合計の期待値は 7 となり、これが最大です。
#
#入力例 2
#4 1
#6 6 6 6
#
#出力例 2
#3.500000000000
#どのサイコロを選んで振っても、出る目の期待値は 3.5 です。
#
#入力例 3
#10 4
#17 13 13 12 15 20 10 13 17 11
#
#出力例 3
#32.000000000000

def 