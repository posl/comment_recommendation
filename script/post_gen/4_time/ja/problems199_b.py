#問題文
#長さ N の数列 A = (A_1, A_2, A_3, ..., A_N), B = (B_1, B_2, B_3, ..., B_N) が与えられます。
#以下の条件を満たす整数 x の個数を求めてください。  
#1 ≦ i ≦ N を満たす全ての整数 i について A_i ≦ x ≦ B_i
#
#制約
#1 ≦ N ≦ 100
#1 ≦ A_i ≦ B_i ≦ 1000
#入力に含まれる値は全て整数
#
#入力
#入力は以下の形式で標準入力から与えられる。
#N
#A_1 A_2 A_3 ... A_N
#B_1 B_2 B_3 ... B_N
#
#出力
#答えを出力せよ。  
#
#入力例 1
#2
#3 2
#7 5
#
#出力例 1
#3
#x は 3 ≦ x ≦ 7 と 2 ≦ x ≦ 5 の両方を満たさなければなりません。
#そのような整数 x は 3, 4, 5 の 3 個あります。  
#
#入力例 2
#3
#1 5 3
#10 7 3
#
#出力例 2
#0
#条件を満たす整数 x が存在しないこともあります。  
#
#入力例 3
#3
#3 2 5
#6 9 8
#
#出力例 3
#2

def 