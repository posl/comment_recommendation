#問題文
#N 頂点 M 辺の単純無向グラフが与えられます。頂点には 1 から N の番号がついており、i 番目の辺は頂点 A_i と頂点 B_i を結んでいます。
#このグラフから 0 本以上のいくつかの辺を削除してグラフが閉路を持たないようにするとき、削除する辺の本数の最小値を求めてください。
#単純無向グラフとは
#単純無向グラフとは、自己ループや多重辺を含まず、辺に向きの無いグラフのことをいいます。
#閉路とは
#単純無向グラフが閉路を持つとは、i ≠ j ならば v_i ≠ v_j を満たす長さ 3 以上の頂点列 (v_0, v_1, ..., v_{n-1}) であって、各 0 ≦ i < n に対し v_i と v_{i+1 mod n} の間に辺が存在するものがあることをいいます。 
#
#制約
#1 ≦ N ≦ 2 × 10^5
#0 ≦ M ≦ 2 × 10^5
#1 ≦ A_i, B_i ≦ N
#与えられるグラフは単純
#入力はすべて整数
#
#入力
#入力は以下の形式で標準入力から与えられる。
#N M
#A_1 B_1
#A_2 B_2
#.
#.
#.
#A_M B_M
#
#出力
#答えを出力せよ。
#
#入力例 1
#6 7
#1 2
#1 3
#2 3
#4 2
#6 5
#4 6
#4 5
#
#出力例 1
#2
#頂点 1 と頂点 2 を結ぶ辺・頂点 4 と頂点 5 を結ぶ辺の 2 本を削除するなどの方法でグラフが閉路を持たないようにすることができます。
#1 本以下の辺の削除でグラフが閉路を持たないようにすることはできないので、2 を出力します。
#
#入力例 2
#4 2
#1 2
#3 4
#
#出力例 2
#0
#
#入力例 3
#5 3
#1 2
#1 3
#2 3
#
#出力例 3
#1

def 