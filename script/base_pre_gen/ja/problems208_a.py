#問題文
#1,2,...,6 の出目がある 6 面サイコロを A 回振ったとき、出た目の合計が B になることはありますか？
#
#制約
#1 ≦ A ≦ 100
#1 ≦ B ≦ 1000
#A, B は整数である。
#
#入力
#入力は以下の形式で標準入力から与えられる。
#A B
#
#出力
#出た目の合計が B になり得る場合は Yes を、そうでない場合は No を出力せよ。
#
#入力例 1
#2 11
#
#出力例 1
#Yes
#6 面サイコロを 2 回振ったときに出た目の和が 11 になるのは次の 2 通りの場合です。
#1 回目のサイコロの出目が 6 で、2 回目のサイコロの出目が 5 である。
#1 回目のサイコロの出目が 5 で、2 回目のサイコロの出目が 6 である。
#
#入力例 2
#2 13
#
#出力例 2
#No
#6 面サイコロを 2 回振ったときに出た目の和が 13 になることはありません。
#
#入力例 3
#100 600
#
#出力例 3
#Yes

def 