#問題文
#N 匹のスライムが横一列に並んでいます。これらの色に関する情報が、長さ N の英小文字から成る文字列 S で与えられます。左から i 番目のスライムは、 S の i 文字目に対応する色を持っています。
#同じ色を持ち隣接するスライムは融合し、色は変わらずに 1 匹のスライムとなります。このとき、融合した後のスライムは、融合する前の各スライムが隣接していた他のスライムと隣接した状態になります。
#最終的に存在するスライムは何匹となるでしょうか。
#
#制約
#1 ≤ N ≤ 10^5
#|S| = N
#S は英小文字から成る
#
#入力
#入力は以下の形式で標準入力から与えられる。
#N
#S
#
#出力
#最終的に存在するスライムの数を出力せよ。
#
#入力例 1
#10
#aabbbbaaca
#
#出力例 1
#5
#最終的に残るスライムを文字列で表すと、abacaとなります。
#
#入力例 2
#5
#aaaaa
#
#出力例 2
#1
#全てのスライムが融合します。
#
#入力例 3
#20
#xxzaffeeeeddfkkkkllq
#
#出力例 3
#10

def 