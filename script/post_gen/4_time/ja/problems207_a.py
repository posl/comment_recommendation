#問題文
#机の上に、正整数が書かれた 3 枚のカードがあります。 3 枚のカードにはそれぞれ整数 A,B,C が書き込まれています。
#いま、この中からちょうど 2 枚のカードを選んで手に持ちました。
#手に持ったカードに書き込まれた整数の和として考えられる最大値を求めてください。
#
#制約
#1 ≦ A,B,C ≦ 100
#入力は全て整数
#
#入力
#入力は以下の形式で標準入力から与えられる。
#A B C
#
#出力
#答えを整数として出力せよ。
#
#入力例 1
#3 4 5
#
#出力例 1
#9
#4,5 の書き込まれた 2 枚のカードを手に持つと、そこに書き込まれた整数の和が 4+5=9 となります。
#これより和が大きくなるカードの選び方は存在しないので、9 を出力します。
#
#入力例 2
#6 6 6
#
#出力例 2
#12
#どのように手に持つカードを選んでも、そこに書き込まれた整数の和は 12 になります。
#
#入力例 3
#99 99 98
#
#出力例 3
#198

def 