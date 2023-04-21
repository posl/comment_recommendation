#問題文
#1 から N までの番号が付いた N 個の区間が与えられます。区間 i は、
#t_i=1 なら [l_i,r_i]
#t_i=2 なら [l_i,r_i)
#t_i=3 なら (l_i,r_i]
#t_i=4 なら (l_i,r_i)
#です。
#1 ≦ i < j ≦ N を満たす整数の組 (i,j) のうち、区間 i と区間 j が共通部分を持つようなものは幾つありますか？
#区間 [X,Y],[X,Y),(X,Y],(X,Y) とは？
#閉区間 [X,Y] は、 X 以上 Y 以下の全ての実数からなる区間
#半開区間 [X,Y) は、 X 以上 Y 未満の全ての実数からなる区間
#半開区間 (X,Y] は、 X より大きく Y 以下の全ての実数からなる区間
#開区間 (X,Y) は、 X より大きく Y 未満の全ての実数からなる区間
#を表します。一言で言うと、角括弧 [] を使っている側は端点を含み、丸括弧 () を使っている側は端点を含みません。
#
#制約
#2 ≦ N ≦ 2000
#1 ≦ t_i ≦ 4
#1 ≦ l_i < r_i ≦ 10^9
#入力は全て整数
#
#入力
#入力は以下の形式で標準入力から与えられる。
#N
#t_1 l_1 r_1
#t_2 l_2 r_2
#.
#.
#.
#t_N l_N r_N
#
#出力
#区間 i と区間 j が共通部分を持つような整数の組 (i,j) の個数を出力せよ。
#
#入力例 1
#3
#1 1 2
#2 2 3
#3 2 4
#
#出力例 1
#2
#問題文中の定義より、区間 1 は [1,2], 区間 2 は [2,3), 区間 3 は (2,4] です。
#区間 i と区間 j が共通部分を持つような整数の組 (i,j) は、(1,2) と (2,3) の 2 つとなります。それぞれ、[2,2] と (2,3) を共通部分として持っています。
#
#入力例 2
#19
#4 210068409 221208102
#4 16698200 910945203
#4 76268400 259148323
#4 370943597 566244098
#1 428897569 509621647
#4 250946752 823720939
#1 642505376 868415584
#2 619091266 868230936
#2 306543999 654038915
#4 486033777 715789416
#1 527225177 583184546
#2 885292456 900938599
#3 264004185 486613484
#2 345310564 818091848
#1 152544274 521564293
#4 13819154 555218434
#3 507364086 545932412
#4 797872271 935850549
#2 415488246 685203817
#
#出力例 2
#102

def 