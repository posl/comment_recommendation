#問題文
#X 秒を測れる砂時計があります。はじめ上のパーツに砂が X [g] あり、1 秒間に 1 [g] 砂が落ちます。なお、上のパーツにもう砂が残っていない場合は砂は落ちません。
#t 秒後に上のパーツに残っている砂は何gでしょう。
#
#制約
#1≤X≤10^9
#1≤t≤10^9
#X,t は整数
#
#入力
#入力は以下の形式で標準入力から与えられる。
#X t
#
#出力
#t 秒後に上のパーツに残っている砂は何gかを出力せよ。
#
#入力例 1
#100 17
#
#出力例 1
#83
#100 [g] の砂のうち 17 [g] が落ちるので、83 [g] になります。
#
#入力例 2
#48 58
#
#出力例 2
#0
#48 [g] の砂は全て落ちきるので、0 [g] になります。
#
#入力例 3
#1000000000 1000000000
#
#出力例 3
#0

def 