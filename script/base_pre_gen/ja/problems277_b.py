#問題文
#英大文字および数字からなる 2 文字の文字列が N 個与えられます。i 個目の文字列は S_i です。
#以下の 3 つの条件をすべて満たすか判定してください。
#・すべての文字列に対して、1 文字目は H , D , C , S のどれかである。
#・すべての文字列に対して、2 文字目は A , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , T , J , Q , K のどれかである。
#・すべての文字列は相異なる。つまり、i ≠ j ならば S_i ≠ S_j である。
#
#制約
#1 ≦ N ≦ 52
#S_i は英大文字および数字からなる 2 文字の文字列
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
#3 つの条件をすべて満たす場合は Yes、そうでない場合は No を出力せよ。
#
#入力例 1
#4
#H3
#DA
#D3
#SK
#
#出力例 1
#Yes
#このとき 3 つの条件をすべて満たすことが確認できます。
#
#入力例 2
#5
#H3
#DA
#CK
#H3
#S7
#
#出力例 2
#No
#S_1 と S_4 がともに H3 となってしまっているため、3 番目の条件に反します。
#
#入力例 3
#4
#3H
#AD
#3D
#KS
#
#出力例 3
#No
#
#入力例 4
#5
#00
#AA
#XX
#YY
#ZZ
#
#出力例 4
#No

def 