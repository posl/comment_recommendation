#問題文
#長さ N の値の分からない整数列 A があります。
#長さ N-1 の整数列 B が与えられます。このとき、
# B_i ≧ max(A_i, A_{i+1}) 
#が成立することが分かっています。
#A の要素の総和として考えられる値の最大値を求めてください。
#
#制約
#入力は全て整数
#2 ≤ N ≤ 100
#0 ≦ B_i ≦ 10^5
#
#入力
#入力は以下の形式で標準入力から与えられる。
#N
#B_1 B_2 ... B_{N-1}
#
#出力
#A の要素の総和として考えられる値の最大値を出力せよ。
#
#入力例 1
#3
#2 5
#
#出力例 1
#9
#A として、例えば A = ( 2 , 1 , 5 )や、 A = ( -1 , -2 , -3 ), A = ( 2 , 2 , 5 ) 等が考えられます。これらのうち A の要素の総和が最大となるものは、 A = ( 2 , 2 , 5 ) です。
#
#入力例 2
#2
#3
#
#出力例 2
#6
#
#入力例 3
#6
#0 153 10 10 23
#
#出力例 3
#53

def 