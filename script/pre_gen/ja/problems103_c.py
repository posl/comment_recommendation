#問題文
#N 個の正整数 a_1, a_2, ..., a_N が与えられます。
#非負整数 m に対して、f(m) = (m mod a_1) + (m mod a_2) + ... + (m mod a_N) とします。
#ここで、X mod Y は X を Y で割った余りを表します。
#f の最大値を求めてください。
#
#制約
#入力は全て整数である
#2 ≦ N ≦ 3000
#2 ≦ a_i ≦ 10^5
#
#入力
#入力は以下の形式で標準入力から与えられる。
#N
#a_1 a_2 ... a_N
#
#出力
#f の最大値を出力せよ。
#
#入力例 1
#3
#3 4 6
#
#出力例 1
#10
#f(11) = (11 mod 3) + (11 mod 4) + (11 mod 6) = 10 が f の最大値です。
#
#入力例 2
#5
#7 46 11 20 11
#
#出力例 2
#90
#
#入力例 3
#7
#994 518 941 851 647 2 581
#
#出力例 3
#4527

def 