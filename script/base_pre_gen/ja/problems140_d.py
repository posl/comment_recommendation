#問題文
#東西一列に N 人の人が並んでいます。
#各人の状態を表す長さ N の文字列 S が与えられます。
#西から i 番目の人は、文字列 S の i 文字目が L ならば西を、R ならば東を向いています。
#どの人も、目の前の人が自分と同じ方向を向いていれば幸福です。
#ただし、目の前に人が居ない場合、幸福ではありません。
#あなたは、以下の操作を 0 回以上 K 回以下の好きな回数だけ行います。
#操作: 1 ≦ l ≦ r ≦ N を満たす整数 l, r を選ぶ。西から l, l+1, ..., r 番目の人の列を 180 度回転する。すなわち、i = 0, 1, ..., r-l について、西から l + i 番目の人は操作後には西から r - i 番目に移動し、元々西を向いていれば東を、東を向いていれば西を向く。
#幸福である人は最大で何人にできるでしょうか。
#
#制約
#N は 1 ≦ N ≦ 10^5 を満たす整数である。
#K は 1 ≦ K ≦ 10^5 を満たす整数である。
#|S| = N
#S の各文字は L または R である。
#
#入力
#入力は以下の形式で標準入力から与えられる。
#N K
#S
#
#出力
#K 回以下の操作後に幸福である人数の最大値を出力せよ。
#
#入力例 1
#6 1
#LRLRRL
#
#出力例 1
#3
#(l, r) = (2, 5) と選べば LLLRLL となり、西から 2, 3, 6 番目の人が幸福です。
#
#入力例 2
#13 3
#LRRLRLRRLRLLR
#
#出力例 2
#9
#
#入力例 3
#10 1
#LLLLLRRRRR
#
#出力例 3
#9
#
#入力例 4
#9 2
#RRRLRLRLL
#
#出力例 4
#7

def 