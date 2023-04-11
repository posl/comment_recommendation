#問題文
#「N も (N+1)÷2 も素数」を満たす奇数 N を 2017に似た数 とします。
#Q 個のクエリが与えられます。
#クエリ i(1≦i≦Q) では奇数 l_i,r_i が与えられるので、l_i≦x≦r_i かつ 2017に似た数 となる奇数 x の個数を求めてください。
#
#制約
#1≦Q≦10^5
#1≦l_i≦r_i≦10^5
#l_i,r_i は奇数
#入力は全て整数
#
#入力
#入力は以下の形式で標準入力から与えられる。
#Q
#l_1 r_1
#:
#l_Q r_Q
#
#出力
#i 行目 (1≦i≦Q) に、クエリ i の答えが x 個のとき、x を出力せよ。
#
#入力例 1
#1
#3 7
#
#出力例 1
#2
#
#3 も (3+1)÷2=2 も素数であるため、3 は 2017に似た数 です。
#5 も (5+1)÷2=3 も素数であるため、5 は 2017に似た数 です。
#7 は素数ですが、 (7+1)÷2=4 は素数ではないため、7 は 2017に似た数 ではありません。
#よって、クエリ 1 の答えは 2 個です。
#
#入力例 2
#4
#13 13
#7 11
#7 11
#2017 2017
#
#出力例 2
#1
#0
#0
#1
#2017 も 2017に似た数 であることに注意してください。
#
#入力例 3
#6
#1 53
#13 91
#37 55
#19 51
#73 91
#13 49
#
#出力例 3
#4
#4
#1
#1
#1
#2

def 