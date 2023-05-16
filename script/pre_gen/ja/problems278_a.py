#問題文
#長さ N の数列 A = (A_1, A_2, ..., A_N) が与えられます。
#あなたは次の操作をちょうど K 回行います。
#A の先頭の要素を取り除き、A の末尾に 0 を挿入する。
#操作を行った後の A の要素をすべて出力してください。
#
#制約
#1 ≦ N ≦ 100
#1 ≦ K ≦ 100
#1 ≦ A_i ≦ 100
#入力される値はすべて整数
#
#入力
#入力は以下の形式で標準入力から与えられる。
#N K
#A_1 A_2 ... A_N
#
#出力
#操作を行った後の A の要素を空白区切りで 1 行に出力せよ。
#
#入力例 1
#3 2
#2 7 8
#
#出力例 1
#8 0 0
#操作を行う前は A = (2, 7, 8) です。
#操作を 1 回行った時点では A = (7, 8, 0) です。
#操作を 2 回行った時点では A = (8, 0, 0) です。
#よって (8, 0, 0) が答えです。
#
#入力例 2
#3 4
#9 9 9
#
#出力例 2
#0 0 0
#
#入力例 3
#9 5
#1 2 3 4 5 6 7 8 9
#
#出力例 3
#6 7 8 9 0 0 0 0 0

def 