#問題文
#H × W のマス目が与えられます。 
#入力において、全てのマスは文字で表されており、.は空きマス、 # は爆弾マスに対応します。 
#マス目は H 個の文字列 S_1,...,S_H で表されます。 
#文字列 S_i の j 文字目は、マス目の上から i 番目、左から j 番目のマスに対応します。(1≦i≦H,1≦j≦W) 
#イルカは各空きマスの上下左右および斜めの 8 方向で隣接しているマスに爆弾マスが何個あるか気になっています。   
#そこで、各空きマスに対応する . を、その空きマスの周囲8方向に隣接するマスにおける爆弾マスの個数を表す数字で置き換えることにしました。     
#以上の規則で置き換えられた後のマス目を出力してください。
#
#制約
#1≦H,W≦50
#S_i は # と . からなる長さ W の文字列
#
#入力
#入力は以下の形式で標準入力から与えられる。  
#H W 
#S_1
#:
#S_H
#
#出力
#置き換えられた後のマス目を H 行の文字列で出力せよ。 
#i 行目 に出力する文字列 T_i の長さは W であり、 T_i の j 文字目は、置き換えられた後のマス目の上から i 番目、左から j 番目のマスに対応させよ。(1≦i≦H,1≦j≦W)
#
#入力例 1
#3 5
#.....
#.#.#.
#.....
#
#出力例 1
#11211
#1#2#1
#11211
#例として、上から 1 番目、左から 1 番目の空きマスに注目します。 
#この空きマスの周囲の 8 マスに含まれる爆弾マスは、上から 2 番目、左から 2 番目のマスのみです。
#したがって、上から 1 番目、左から 1 番目の空きマスは 1 に置き換えられています。
#
#入力例 2
#3 5
######
######
######
#
#出力例 2
######
######
######
#空きマスが存在しない場合があります。
#
#入力例 3
#6 6
######.
##.#.##
#####.#
#.#..#.
##.##..
##.#...
#
#出力例 3
######3
##8#7##
#####5#
#4#65#2
##5##21
##4#310

def 