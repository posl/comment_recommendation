#問題文
#1, 2, ..., N の番号がついた N 個の皿と、1, 2, ..., M の番号がついた M 個の条件があります。
#条件 i は、皿 A_i と皿 B_i の両方にボールが (1 個以上) 置かれているとき満たされます。
#1, 2, ..., K の番号がついた K 人の人がいて、人 i は皿 C_i か皿 D_i のどちらか一方にボールを置きます。
#満たされる条件の個数は最大でいくつでしょうか？
#
#制約
#入力は全て整数
#2 ≤ N ≤ 100
#1 ≤ M ≤ 100
#1 ≤ A_i < B_i ≤ N
#1 ≤ K ≤ 16
#1 ≤ C_i < D_i ≤ N
#
#入力
#入力は以下の形式で標準入力から与えられる。
#N M
#A_1 B_1
#.
#.
#.
#A_M B_M
#K
#C_1 D_1
#.
#.
#.
#C_K D_K
#
#出力
#答えを出力せよ。
#
#入力例 1
#4 4
#1 2
#1 3
#2 4
#3 4
#3
#1 2
#1 3
#2 3
#
#出力例 1
#2
#例えば、人 1, 2, 3 がそれぞれ皿 1, 3, 2 にボールを置くと、条件 1, 2 の 2 つが満たされます。
#
#入力例 2
#4 4
#1 2
#1 3
#2 4
#3 4
#4
#3 4
#1 2
#2 4
#2 4
#
#出力例 2
#4
#例えば、人 1, 2, 3, 4 がそれぞれ皿 3, 1, 2, 4 にボールを置くと、全ての条件が満たされます。
#
#入力例 3
#6 12
#2 3
#4 6
#1 2
#4 5
#2 6
#1 5
#4 5
#1 3
#1 2
#2 6
#2 3
#2 5
#5
#3 5
#1 4
#2 6
#4 6
#5 6
#
#出力例 3
#9

def 