#問題文
#N 枚のカードがあり、i 番目のカードには整数 A_i が書かれています。
#あなたは、j = 1, 2, ..., M について順に以下の操作を 1 回ずつ行います。
#操作: カードを B_j 枚まで選ぶ(0 枚でもよい)。選んだカードに書かれている整数をそれぞれ C_j に書き換える。
#M 回の操作終了後に N 枚のカードに書かれた整数の合計の最大値を求めてください。
#
#制約
#入力は全て整数である。
#1 ≦ N ≦ 10^5
#1 ≦ M ≦ 10^5
#1 ≦ A_i, C_i ≦ 10^9
#1 ≦ B_i ≦ N
#
#入力
#入力は以下の形式で標準入力から与えられる。
#N M
#A_1 A_2 ... A_N
#B_1 C_1
#B_2 C_2
#.
#.
#.
#B_M C_M
#
#出力
#M 回の操作終了後に N 枚のカードに書かれた整数の合計の最大値を出力せよ。
#
#入力例 1
#3 2
#5 1 4
#2 3
#1 5
#
#出力例 1
#14
#2 番目のカードに書かれた整数を 5 に書き換えることで、3 枚のカードに書かれた整数の合計が 5 + 5 + 4 = 14 となり、このときが最大です。
#
#入力例 2
#10 3
#1 8 5 7 100 4 52 33 13 5
#3 10
#4 30
#1 4
#
#出力例 2
#338
#
#入力例 3
#3 2
#100 100 100
#3 99
#3 99
#
#出力例 3
#300
#
#入力例 4
#11 3
#1 1 1 1 1 1 1 1 1 1 1
#3 1000000000
#4 1000000000
#3 1000000000
#
#出力例 4
#10000000001
#出力が 32 bit 整数型に収まらない場合があります。

def 