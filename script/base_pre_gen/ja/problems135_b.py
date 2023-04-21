#問題文
#{1, 2, ..., N} を並び替えた数列 p = {p_1, p_2, ..., p_N} があります。
#あなたは一度だけ、整数  i, j  (1 ≦ i < j ≦ N) を選んで  p_i  と  p_j  を入れ替える操作を行うことができます。操作を行わないことも可能です。
#p を昇順にすることができるなら YES を、できないならば NO を出力してください。
#
#制約
#入力は全て整数である。
#2 ≦ N ≦ 50
#p は {1, 2, ..., N} を並び替えた数列である。
#
#入力
#入力は以下の形式で標準入力から与えられる。
#N
#p_1 p_2 ... p_N
#
#出力
#p を昇順にすることができるなら YES を、できないならば NO を出力せよ。
#
#入力例 1
#5
#5 2 3 4 1
#
#出力例 1
#YES
#p_1 と p_5 を入れ替えることで p を昇順にできます。
#
#入力例 2
#5
#2 4 3 5 1
#
#出力例 2
#NO
#この場合、どのような操作を行っても p を昇順にすることはできません。
#
#入力例 3
#7
#1 2 3 4 5 6 7
#
#出力例 3
#YES
#p が最初から昇順なので、操作を行う必要はありません。

def 