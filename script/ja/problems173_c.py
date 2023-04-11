#問題文
#H 行 W 列に並ぶマスからなるマス目があります。上から i 行目、左から j 列目 (1 ≦ i ≦ H, 1 ≦ j ≦ W) のマスの色は文字 c_{i,j} として与えられ、c_{i,j} が . のとき白、# のとき黒です。
#次の操作を行うことを考えます。
#行を何行か選び (0 行でもよい)、列を何列か選ぶ (0 列でもよい)。そして、選んだ行に含まれるマスと、選んだ列に含まれるマスをすべて赤く塗る。
#正の整数 K が与えられます。操作後に黒いマスがちょうど K 個残るような行と列の選び方は何通りでしょうか。ここで、二つの選び方は、一方においてのみ選ばれる行または列が存在するときに異なるとみなされます。
#
#制約
#1 ≦ H, W ≦ 6
#1 ≦ K ≦ HW
#c_{i,j} は . または #
#
#入力
#入力は以下の形式で標準入力から与えられる。
#H W K
#c_{1,1}c_{1,2}...c_{1,W}
#c_{2,1}c_{2,2}...c_{2,W}
#:
#c_{H,1}c_{H,2}...c_{H,W}
#
#出力
#条件を満たす行と列の選び方の個数を表す整数を出力せよ。
#
#入力例 1
#2 3 2
#..#
####
#
#出力例 1
#5
#以下の 5 通りの選び方が条件を満たします。
#1 行目、1 列目
#1 行目、2 列目
#1 行目、3 列目
#1 列目、2 列目
#3 列目
#
#入力例 2
#2 3 4
#..#
####
#
#出力例 2
#1
#何も選ばないという 1 通りの選び方が条件を満たします。
#
#入力例 3
#2 2 3
###
###
#
#出力例 3
#0
#
#入力例 4
#6 6 8
#..##..
#.#..#.
##....#
#######
##....#
##....#
#
#出力例 4
#208

def 