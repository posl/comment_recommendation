#問題文
#数字のみからなる、長さがちょうど 9 の文字列 S が与えられます。
#S には 0 から 9 までのうち、ちょうど 1 つの数字を除いた 9 種類の数字が一度ずつ登場します。
#S に登場しない唯一の数字を出力してください。
#
#制約
#S は数字のみからなる長さ 9 の文字列である。
#S の文字はすべて相異なる。
#
#入力
#入力は以下の形式で標準入力から与えられる。
#S
#
#出力
#S に登場しない唯一の数字を出力せよ。
#
#入力例 1
#023456789
#
#出力例 1
#1
#文字列 023456789 には 1 のみが登場していません。
#よって、1 を出力します。
#
#入力例 2
#459230781
#
#出力例 2
#6
#文字列 459230781 には 6 のみが登場していません。
#よって、6 を出力します。
#文字列に数字が現れる順番は昇順とは限らないので注意してください。

def 