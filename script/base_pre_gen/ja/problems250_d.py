#問題文
#以下の条件を満たす整数 k を「 250 に似た数」と呼びます。
#k が素数 p<q を使って k=p × q^3 と表される。
#N 以下の「 250 に似た数」は全部でいくつありますか？
#
#制約
#N は 1 以上 10^{18} 以下の整数
#
#入力
#入力は以下の形式で標準入力から与えられる。
#N
#
#出力
#答えを整数として出力せよ。
#
#入力例 1
#250
#
#出力例 1
#2
#54 = 2 × 3^3 なので、「 250 に似た数」です。
#250 = 2 × 5^3 なので、「 250 に似た数」です。
#250 以下の「 250 に似た数」は、以上の 2 つです。
#
#入力例 2
#1
#
#出力例 2
#0
#
#入力例 3
#123456789012345
#
#出力例 3
#226863

def 