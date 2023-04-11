#問題文
#1 以上 26 以下の整数からなる長さ 26 の数列 P=(P_1,P_2, ... ,P_{26}) が与えられます。ここで、P の要素は相異なることが保証されます。
#以下の条件を満たす長さ 26 の文字列 S を出力してください。
#任意の i (1 ≦ i ≦ 26) について、S の i 文字目は辞書順で小さい方から P_i 番目の英小文字である。
#
#制約
#1 ≦ P_i ≦ 26
#P_i ≠ P_j (i ≠ j)
#入力は全て整数である。
#
#入力
#入力は以下の形式で標準入力から与えられる。
#P_1 P_2 ... P_{26}
#
#出力
#文字列 S を出力せよ。
#
#入力例 1
#1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26
#
#出力例 1
#abcdefghijklmnopqrstuvwxyz
#
#入力例 2
#2 1 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26
#
#出力例 2
#bacdefghijklmnopqrstuvwxyz
#
#入力例 3
#5 11 12 16 25 17 18 1 7 10 4 23 20 3 2 24 26 19 14 9 6 22 8 13 15 21
#
#出力例 3
#eklpyqragjdwtcbxzsnifvhmou

def 