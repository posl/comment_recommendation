#問題文
#英小文字からなる N 個の文字列 W_1,W_2,...,W_N が与えられます。
#これらのうち一つ以上が and, not, that, the, you のいずれかと一致するなら Yes 、そうでないなら No と出力してください。
#
#制約
#N は 1 以上 100 以下の整数
#1 ≦ |W_i| ≦ 50 ( |W_i| は文字列 W_i の長さ )
#W_i は英小文字からなる
#
#入力
#入力は以下の形式で標準入力から与えられる。
#N
#W_1 W_2 ... W_N
#
#出力
#答えを出力せよ。
#
#入力例 1
#10
#in that case you should print yes and not no
#
#出力例 1
#Yes
#例えば W_4= you なので、 Yes と出力します。
#
#入力例 2
#10
#in diesem fall sollten sie no und nicht yes ausgeben
#
#出力例 2
#No
#文字列 W_i はいずれも、 and, not, that, the, you のいずれとも一致しません。

def 