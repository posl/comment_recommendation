#問題文
#きつねの次郎と三郎が一次元リバーシで遊んでいます。一次元リバーシでは、盤面には白か黒の石が一列に並んだ状態となっており、列の右端か左端に新たに石を打っていきます。通常のリバーシと同じように、たとえば白の石を打つことで黒の石を挟むと、挟まれた黒の石は白い石に変わります。
#ゲームの途中で三郎に急用ができて帰ってしまうことになりました。このとき、盤面の状態は文字列 S で表されます。石は |S| (文字列の長さ) 個並んでおり、左から i (1 ≦ i ≦ |S|) 個目の石の色は、S の i 文字目が B のとき黒、W のとき白です。
#次郎は現在の盤面に対して、できるだけ少ない個数の石を新たに打つことで全ての石を同じ色にしようと考えました。最小で何個の石を打てばよいかを求めてください。
#
#制約
#1 ≦ |S| ≦ 10^5
#S に含まれる文字は B または W のいずれかである
#
#入力
#入力は以下の形式で標準入力から与えられる。
#S
#
#出力
#全ての石を同じ色にするために打つ必要のある石の個数の最小値を出力せよ。
#
#入力例 1
#BBBWW
#
#出力例 1
#1
#たとえば右端に黒い石を打つとすべての白い石を黒い石にすることができます。他にも、左端に白い石を打つことでもすべての石の色を同じにできます。
#いずれの場合も 1 個の石ですべての石を同じ色にすることができるので、1 を出力します。
#
#入力例 2
#WWWWWW
#
#出力例 2
#0
#最初から全ての石が同じ色の場合、新たに石を打つ必要はありません。
#
#入力例 3
#WBWBWBWBWB
#
#出力例 3
#9

def 