#問題文
#atcoder の並べ替えである文字列 S が与えられます。
#この文字列 S に対して以下の操作を 0 回以上行います。
#S 中の隣接する 2 文字を選び、入れ替える。
#S を atcoder にするために必要な最小の操作回数を求めてください。
#
#制約
#S は atcoder の並べ替えである文字列
#
#入力
#入力は以下の形式で標準入力から与えられる。
#S
#
#出力
#答えを整数として出力せよ。
#
#入力例 1
#catredo
#
#出力例 1
#8
#catredo -> [ac]tredo -> actre[od] -> actr[oe]d -> actro[de] -> act[or]de -> acto[dr]e -> a[tc]odre -> atcod[er]
#という流れで操作を行うと、 8 回で S を atcoder にすることができ、これが達成可能な最小の操作回数です。
#
#入力例 2
#atcoder
#
#出力例 2
#0
#この場合、文字列 S は元から atcoder です。
#
#入力例 3
#redocta
#
#出力例 3
#21

def 