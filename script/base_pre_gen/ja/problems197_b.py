#問題文
#縦 H 行、横 W 列のマス目があり、いくつかのマスには障害物が置かれています。
#上から i 番目、左から j 番目のマスをマス (i, j) と表すことにします。
#H 個の文字列 S_1, S_2, S_3, ..., S_H が与えられます。S_i の j 文字目はマス (i, j) の状態を表し、# なら障害物が置かれていることを、. なら障害物が置かれていないことを表します。
#このマス目上のあるマスからあるマスが見えるとは、2 つのマスが同じ行または列にあり、2 つのマスの間 (2 つのマス自身を含む) に障害物が 1 つも置かれていないことを意味します。
#このマス目上のマスであって、マス (X, Y) から見えるもの (マス (X, Y) 自身を含む) の数を求めてください。
#
#制約
#1 ≦ H ≦ 100
#1 ≦ W ≦ 100
#1 ≦ X ≦ H
#1 ≦ Y ≦ W
#S_i は . および # のみからなる長さ W の文字列
#マス (X, Y) に障害物は置かれていない
#
#入力
#入力は以下の形式で標準入力から与えられる。
#H W X Y
#S_1
#S_2
#S_3
#.
#.
#.
#S_H
#
#出力
#答えを出力せよ。  
#
#入力例 1
#4 4 2 2
###..
#...#
##.#.
#.#.#
#
#出力例 1
#4
#以下がマス (2, 2) から見えるマスです。  
#マス (2, 1)
#マス (2, 2)
#マス (2, 3)
#マス (3, 2)
#
#入力例 2
#3 5 1 4
##....
######
#....#
#
#出力例 2
#4
#行または列が同じでも、間に障害物があるようなマスは見えません。  
#
#入力例 3
#5 5 4 2
#.#..#
##.###
###...
##..#.
##.###
#
#出力例 3
#3

def 