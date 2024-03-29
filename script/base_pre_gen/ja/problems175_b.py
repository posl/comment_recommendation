#問題文
#1, ..., N の番号がついた N 本の棒があります。棒 i (1 ≦ i ≦ N) の長さは L_i です。
#このうち、三角形を作ることのできるような長さの異なる 3 本の棒を選ぶ方法は何通りあるでしょうか。
#つまり、3 つの整数 1 ≦ i < j < k ≦ N の組であって次の 2 つの条件の両方を満たすものの個数を求めてください。
#L_i, L_j, L_k がすべて異なる
#3 辺の長さが L_i, L_j, L_k であるような三角形が存在する
#
#制約
#1 ≦ N ≦ 100
#1 ≦ L_i ≦ 10^9
#入力は全て整数である
#
#入力
#入力は以下の形式で標準入力から与えられる。
#N
#L_1 L_2 ... L_N
#
#出力
#三角形を作ることのできるような、長さの異なる 3 本の棒を選ぶ方法の個数を出力せよ。
#
#入力例 1
#5
#4 4 9 7 5
#
#出力例 1
#5
#条件を満たすような (i, j, k) は、(1, 3, 4), (1, 4, 5), (2, 3, 4), (2, 4, 5), (3, 4, 5) の 5 個があります。
#
#入力例 2
#6
#4 5 4 3 3 5
#
#出力例 2
#8
#長さ 3, 4, 5 の棒が 2 本ずつあります。1 つ目の条件を満たすためにはそれぞれから 1 本ずつ選ぶしかありません。
#3 辺の長さが 3, 4, 5 の三角形は存在するので、条件を満たすような (i, j, k) は 2 ^ 3 = 8 個あります。
#
#入力例 3
#10
#9 4 6 1 9 6 10 6 6 8
#
#出力例 3
#39
#
#入力例 4
#2
#1 1
#
#出力例 4
#0
#1 ≦ i < j < k ≦ N を満たす (i, j, k) が存在しないので、0 を出力してください。

def 