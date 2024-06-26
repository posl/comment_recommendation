#問題文
#N 問の問題からなるコンテストが開催され、i (1≦ i≦ N) 問目の配点は A_i 点でした。
#すぬけくんはこのコンテストに参加し、B_1,B_2,...,B_M 問目の M 問を解きました。
#すぬけくんの総得点を求めてください。
#ただし、総得点とは解いた問題の配点の総和を意味するものとします。
#
#制約
#1≦ M ≦ N ≦ 100
#1≦ A_i ≦ 100
#1≦ B_1 < B_2 < ... < B_M ≦ N
#入力は全て整数
#
#入力
#入力は以下の形式で標準入力から与えられる。
#N M
#A_1 A_2 ... A_N
#B_1 B_2 ... B_M
#
#出力
#答えを整数として出力せよ。
#
#入力例 1
#3 2
#10 20 30
#1 3
#
#出力例 1
#40
#すぬけくんは 1 問目と 3 問目を解きました。
#配点はそれぞれ 10 点と 30 点なので、総得点は 10+30=40 点です。
#
#入力例 2
#4 1
#1 1 1 100
#4
#
#出力例 2
#100
#
#入力例 3
#8 4
#22 75 26 45 72 81 47 29
#4 6 7 8
#
#出力例 3
#202

def 