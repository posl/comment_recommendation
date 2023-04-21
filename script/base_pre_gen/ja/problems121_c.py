#問題文
#栄養ドリンクにレーティング上昇効果があると聞いた高橋くんは、M 本の栄養ドリンクを買い集めることにしました。
#栄養ドリンクが売られている店は N 軒あり、i 軒目の店では 1 本 A_i 円の栄養ドリンクを B_i 本まで買うことができます。
#最小で何円あれば M 本の栄養ドリンクを買い集めることができるでしょうか。
#なお、与えられる入力では、十分なお金があれば M 本の栄養ドリンクを買い集められることが保証されます。
#
#制約
#入力は全て整数である。
#1 ≦ N, M ≦ 10^5
#1 ≦ A_i ≦ 10^9
#1 ≦ B_i ≦ 10^5
#B_1 + ... + B_N ≧ M
#
#入力
#入力は以下の形式で標準入力から与えられる。
#N M
#A_1 B_1
#A_2 B_2
#.
#.
#.
#A_N B_N
#
#出力
#M 本の栄養ドリンクを買い集めるのに必要な最小の金額を出力せよ。
#
#入力例 1
#2 5
#4 9
#2 4
#
#出力例 1
#12
#12 円あれば 1 軒目の店で 1 本、2 軒目の店で 4 本の栄養ドリンクを購入し、合計 5 本の栄養ドリンクを買い集めることができます。一方、11 円以下では 5 本の栄養ドリンクを買い集めることができません。
#
#入力例 2
#4 30
#6 18
#2 5
#3 10
#7 9
#
#出力例 2
#130
#
#入力例 3
#1 100000
#1000000000 100000
#
#出力例 3
#100000000000000
#出力が 32 ビット整数型におさまらないことがあります。

def 