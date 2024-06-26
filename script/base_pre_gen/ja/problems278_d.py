#問題文
#長さ N の数列 A = (A_1, A_2, ..., A_N) が与えられます。  
#Q 個のクエリが与えられるので、順番にすべて処理してください。
#q 番目 (1≦ q≦ Q) のクエリは以下の 3 つのいずれかの形式で、それぞれ次のようなクエリを表します。
#1 x _ q ： A のすべての要素に x _ q を代入する。
#2 i _ q x _ q ： A _ {i _ q} に x _ q を加える。
#3 i _ q ： A _ {i _ q} の値を出力する。
#
#制約
#1 ≦ N ≦ 2×10^5
#1 ≦ Q ≦ 2×10^5
#0 ≦ A _ i ≦ 10^9 (1≦ i≦ N)
#q 番目 (1≦ q≦ Q) のクエリが 2 番目もしくは 3 番目の形式のとき、1 ≦ i _ q ≦ N
#q 番目 (1≦ q≦ Q) のクエリが 1 番目もしくは 2 番目の形式のとき、0 ≦ x _ q ≦ 10^9
#3 番目の形式のクエリが存在する
#入力される値はすべて整数
#
#入力
#入力は以下の形式で標準入力から与えられる。
#N
#A_1 A_2 ... A_N
#Q
#query_1
#query_2
#.
#.
#.
#query_Q
#ただし、query_q は q 番目のクエリであり、1 x, 2 i x, 3 i の形式のいずれかで与えられる。
#
#出力
#query_q が 3 番目の形式であるような q (1≦ q≦ Q) の個数を X として、X 行出力せよ。
#j (1≦ j≦ X) 行目にはそのようなクエリのうち j 番目のクエリに対する答えを出力せよ。
#
#入力例 1
#5
#3 1 4 1 5
#6
#3 2
#2 3 4
#3 3
#1 1
#2 3 4
#3 3
#
#出力例 1
#1
#8
#5
#はじめ、A=(3,1,4,1,5) です。
#それぞれのクエリでは、以下のような処理が行われます。
#A_2=1 なので、1 を出力します。
#A_3 に 4 を加えます。A=(3,1,8,1,5) となります。
#A_3=8 なので、8 を出力します。
#A の要素すべてに 1 を代入します。A=(1,1,1,1,1) となります。
#A_3 に 4 を加えます。A=(1,1,5,1,1) となります。
#A_3=5 なので、5 を出力します。
#
#入力例 2
#1
#1000000000
#8
#2 1 1000000000
#2 1 1000000000
#2 1 1000000000
#2 1 1000000000
#2 1 1000000000
#2 1 1000000000
#2 1 1000000000
#3 1
#
#出力例 2
#8000000000
#A の要素の値が 32bit 整数に収まらない可能性があることに注意してください。
#
#入力例 3
#10
#1 8 4 15 7 5 7 5 8 0
#20
#2 7 0
#3 7
#3 8
#1 7
#3 3
#2 4 4
#2 4 9
#2 10 5
#1 10
#2 4 2
#1 10
#2 3 1
#2 8 11
#2 3 14
#2 1 9
#3 8
#3 8
#3 1
#2 6 5
#3 7
#
#出力例 3
#7
#5
#7
#21
#21
#19
#10

def 