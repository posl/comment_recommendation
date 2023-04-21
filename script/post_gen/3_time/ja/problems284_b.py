#問題文
#この問題は 1 つの入力ファイルに複数のテストケースが含まれる問題です。
#はじめに整数 T が与えられます。T 個のテストケースについて次の問題を解いてください。
#N 個の正整数 A_1, A_2, ..., A_N があります。このうち奇数は何個ありますか？
#
#制約
#1 ≦ T ≦ 100
#1 ≦ N ≦ 100
#1 ≦ A_i ≦ 10^9
#入力される値はすべて整数
#
#入力
#入力は以下の形式で標準入力から与えられる。ここで test_i は i 番目のテストケースを意味する。
#T
#test_1
#test_2
#.
#.
#.
#test_T
#各テストケースは以下の形式で与えられる。
#N
#A_1 A_2 ... A_N
#
#出力
#T 行出力せよ。i 行目には i 番目のテストケースに対する答えを出力せよ。
#
#入力例 1
#4
#3
#1 2 3
#2
#20 23
#10
#6 10 4 1 5 9 8 6 5 1
#1
#1000000000
#
#出力例 1
#2
#1
#5
#0
#この入力は 4 個のテストケースが含まれています。  
#入力の 2 行目と 3 行目が 1 番目のテストケースに対応する入力で、N = 3, A_1 = 1, A_2 = 2, A_3 = 3 になります。
#A_1, A_2, A_3 のうち奇数は全部で 2 個なので 1 行目に 2 を出力します。

def 