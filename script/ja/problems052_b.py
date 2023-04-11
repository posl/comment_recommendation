#問題文
#あなたは整数 x を持っています。
#最初、x=0 です。
#あなたは、長さ N の文字列 S をもらったので、これを使って N 回の操作を行いました。
#i 回目の操作では、S_i=I ならば x の値を 1 増やし、S_i=D ならば x の値を 1 減らしました。
#操作の途中( 1 回目の操作の前、N 回目の操作の後も含む)で x がとる値の最大値を答えてください。
#
#制約
#1≦N≦100
#|S|=N
#S には、I、D 以外の文字は含まれない
#
#入力
#入力は以下の形式で標準入力から与えられる。
#N
#S
#
#出力
#操作の途中での整数 x がとる値の最大値を出力せよ。
#
#入力例 1
#5
#IIDID
#
#出力例 1
#2
#それぞれの操作後の x の値は、1,2,1,2,1 となるので、最大値である 2 を出力します。
#
#入力例 2
#7
#DDIDDII
#
#出力例 2
#0
#最初の x=0 の状態で x が最大になるので、0 を出力します。

def 