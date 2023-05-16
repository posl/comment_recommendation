#問題文
#整数 N が与えられます。N! (= 1 × 2 × ... × N) の約数のうち、七五数 は何個あるでしょうか？
#ここで、七五数とは約数をちょうど 75 個持つ正の整数です。
#
#注記
#正の整数 A が正の整数 B を割り切るとき、A を B の 約数 といいます。
#例えば、6 の約数は 1,2,3,6 の 4 個です。
#
#制約
#1 ≦ N ≦ 100
#N は整数である。
#
#入力
#入力は以下の形式で標準入力から与えられる。
#N
#
#出力
#N! の約数であるような七五数の個数を出力せよ。
#
#入力例 1
#9
#
#出力例 1
#0
#9! = 1 × 2 × ... × 9 = 362880 の約数に七五数はありません。
#
#入力例 2
#10
#
#出力例 2
#1
#10! = 3628800 の約数のうち、七五数であるのは 32400 の 1 個です。
#
#入力例 3
#100
#
#出力例 3
#543

def 