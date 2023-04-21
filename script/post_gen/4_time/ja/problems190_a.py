#問題文
#高橋くんと青木くんがゲームを行います。
#はじめ、高橋くんは A 個、青木くんは B 個のアメを持っています。
#C=0 ならば高橋くんが先手、C=1 ならば青木くんが先手で、高橋くんと青木くんは以下の操作を交互に繰り返します。
#自分の持っているアメを 1 個食べる。
#先に操作を行えなくなった者の負けです。どちらが勝つでしょうか？
#
#制約
#入力は全て整数
#0 ≤ A, B ≤ 100
#C in {0, 1}
#
#入力
#入力は以下の形式で標準入力から与えられる。
#A B C
#
#出力
#高橋くんが勝つならば Takahashi を、青木くんが勝つならば Aoki を出力せよ。
#
#入力例 1
#2 1 0
#
#出力例 1
#Takahashi
#はじめ、高橋くんと青木くんの持っているアメの個数はそれぞれ 2, 1 個です。
#ゲームは以下のように進行します。
#高橋くんがアメを 1 個食べる。
#青木くんがアメを 1 個食べる。
#高橋くんがアメを 1 個食べる。
#青木くんはアメを持っていないので、高橋くんが勝つ。
#
#入力例 2
#2 2 0
#
#出力例 2
#Aoki
#
#入力例 3
#2 2 1
#
#出力例 3
#Takahashi

def 