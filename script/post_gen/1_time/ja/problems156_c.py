#問題文
#数直線上に N 人の人が住んでいます。
#i 番目の人が住んでいるのは座標 X_i です。
#あなたは N 人全員が参加する集会を開くことを考えています。
#集会は数直線上の任意の 整数値の座標 で開くことができ、座標 P で集会を開くとき、i 番目の人は集会に参加するために (X_i - P)^2 の体力を消費します。
#N 人が消費する体力の総和としてありえる値の最小値を求めてください。
#
#制約
#入力は全て整数である。
#1 ≦ N ≦ 100
#1 ≦ X_i ≦ 100
#
#入力
#入力は以下の形式で標準入力から与えられる。
#N
#X_1 X_2 ... X_N
#
#出力
#N 人が消費する体力の総和としてありえる値の最小値を出力せよ。
#
#入力例 1
#2
#1 4
#
#出力例 1
#5
#座標 2 で集会を開くとき、1 番目の人が消費する体力は (1 - 2)^2 = 1、
#2 番目の人が消費する体力は (4 - 2)^2 = 4、よってその総和は 5 です。
#これが 2 人が消費する体力の総和としてありえる値の最小値です。
#集会を開くことができるのは整数値の座標だけであることに注意してください。
#
#入力例 2
#7
#14 14 2 13 56 2 37
#
#出力例 2
#2354

def 