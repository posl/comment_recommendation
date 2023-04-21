#問題文
#長さ N の正整数のみからなる数列 A=(A_1,...,A_N) があります。
#A を 10^{100} 回連結した数列を数列 B とします。  
#B の項を前から順に足したとき、和が初めて X を超えるのは何項目まで足したときですか？
#すなわち、以下の式を満たす最小の整数 k を求めてください。  
#(sum_{i=1}^{k} B_i > X) 
#
#制約
#1 ≦ N ≦ 10^5
#1 ≦ A_i ≦ 10^9
#1 ≦ X ≦ 10^{18}
#入力は全て整数
#
#入力
#入力は以下の形式で標準入力から与えられる。
#N
#A_1 ... A_N
#X
#
#出力
#答えを出力せよ。  
#
#入力例 1
#3
#3 5 2
#26
#
#出力例 1
#8
#B=(3,5,2,3,5,2,3,5,2,...) です。
#(sum_{i=1}^{8} B_i = 28 > 26) であり、k が 7 以下のとき条件を満たさないので、8 が答えです。
#
#入力例 2
#4
#12 34 56 78
#1000
#
#出力例 2
#23

def 