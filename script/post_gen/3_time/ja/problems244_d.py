#問題文
#1, 2, 3 の番号がついた 3 人の高橋くんがおり、赤・緑・青の色がついた 3 種類の帽子がそれぞれ 1 つずつあります。それぞれの高橋くんは帽子を 1 つかぶっており、高橋くん i がはじめにかぶっている帽子の色は文字 S_i で表されます。ここで、R は赤、G は緑、B は青に対応しています。これから、以下の操作をちょうど 10^{18} 回行います。
#操作
#3 人の高橋くんのうち 2 人を選ぶ。2 人はお互いのかぶっている帽子を交換する。
#10^{18} 回の操作の後、高橋くん i が文字 T_i に対応する色の帽子をかぶっているようにすることはできますか？
#
#制約
#S_1, S_2, S_3 は R, G, B の並べ替えである
#T_1, T_2, T_3 は R, G, B の並べ替えである
#
#入力
#入力は以下の形式で標準入力から与えられる。
#S_1 S_2 S_3
#T_1 T_2 T_3
#
#出力
#10^{18} 回の操作の後、高橋くん i が文字 T_i に対応する色の帽子をかぶっているようにすることはできる場合は Yes を、できない場合は No を出力せよ。
#
#入力例 1
#R G B
#R G B
#
#出力例 1
#Yes
#例えば、高橋くん 1 と高橋くん 2 の帽子を交換する操作を 10^{18} 回行うと目的を達成できます。

def 