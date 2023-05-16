#問題文
#N 行 N 列のマス目があり、それぞれのマスは白または黒で塗られています。
#マス目の状態は N 個の文字列 S_i で表され、
#S_i の j 文字目が # であることはマス目の上から i 行目、左から j 列目のマスが黒く塗られていることを、
#. であることは白く塗られていることをさします。
#高橋君はこのマス目のうち高々 2 つの白く塗られているマスを選び、黒く塗ることができます。
#マス目の中に、黒く塗られたマスが縦、横、ななめのいずれかの向きに 6 つ以上連続するようにできるか判定してください。
#ただし、黒く塗られたマスがななめに 6 つ以上連続するとは、N 行 N 列のマス目に完全に含まれる 6 行 6 列のマス目であって、その少なくとも一方の対角線上のマスがすべて黒く塗られているようなものが存在する事をさします。
#
#制約
#6 ≦ N ≦ 1000
#| S_i| =N
#S_i は # と . のみからなる。
#
#入力
#入力は以下の形式で標準入力から与えられる。
#N
#S_1
#S_2
#.
#.
#.
#S_N
#
#出力
#高々 2 つのマス目を黒く塗ることで条件をみたすようにできるなら Yes を、そうでないならば No を出力せよ。
#
#入力例 1
#8
#........
#........
#.#.##.#.
#........
#........
#........
#........
#........
#
#出力例 1
#Yes
#上から 3 行目の左から 3, 6 番目のマスを塗ることで横方向に 6 つの黒く塗られたマスを連続させることができます。
#
#入力例 2
#6
#######
#######
#######
#######
#######
#######
#
#出力例 2
#Yes
#高橋君はマス目を新たに黒く塗ることはできませんが、すでにこのマス目は条件をみたしています。
#
#入力例 3
#10
#..........
##..##.....
#..........
#..........
#....#.....
#....#.....
#.#...#..#.
#..........
#..........
#..........
#
#出力例 3
#No

def 