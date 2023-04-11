#問題文
#左右一列に N 枚のタイルが並んでおり、各タイルの初めの色は長さ N の文字列 S で表されます。
#左から i 番目のタイルは、S の i 番目の文字が 0 のとき黒色で、1 のとき白色で塗られています。
#あなたは、いくつかのタイルを黒色または白色に塗り替えることで、どの隣り合う 2 枚のタイルも異なる色で塗られているようにしたいです。
#最小で何枚のタイルを塗り替えることで条件を満たすようにできるでしょうか。
#
#制約
#1 ≦ |S| ≦ 10^5
#S_i は 0 または 1 である。
#
#入力
#入力は以下の形式で標準入力から与えられる。
#S
#
#出力
#条件を満たすために塗り替えるタイルの枚数の最小値を出力せよ。
#
#入力例 1
#000
#
#出力例 1
#1
#中央のタイルを白色に塗り替えれば条件を達成できます。
#
#入力例 2
#10010010
#
#出力例 2
#3
#
#入力例 3
#0
#
#出力例 3
#0

def 