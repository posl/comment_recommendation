#問題文
#整数 N が与えられます。
#以下の操作を K 回行った後の整数 N を出力してください。
#整数 N が 200 の倍数であれば、N を 200 で割る。
#そうでなければ、整数 N を、N の後ろに文字列として 200 を付け加えた整数に置き換える。
#例えば、7 を置き換えると 7200 に、1234 を置き換えると 1234200 になります。
#
#
#制約
#入力は全て整数
#1 ≦ N ≦ 10^5
#1 ≦ K ≦ 20
#
#入力
#入力は以下の形式で標準入力から与えられる。
#N K
#
#出力
#答えを整数として出力せよ。
#
#入力例 1
#2021 4
#
#出力例 1
#50531
#N=2021 に 4 回操作を行うと、N の値は操作を行うごとに 2021 -> 2021200 -> 10106 -> 10106200 -> 50531 となります。
#
#入力例 2
#40000 2
#
#出力例 2
#1
#
#入力例 3
#8691 20
#
#出力例 3
#84875488281
#答えは 32 bit 符号付き整数型に収まらない可能性があります。

def 