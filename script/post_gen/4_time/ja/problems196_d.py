#問題文
#縦 H メートル、横 W メートルの長方形の部屋があります。
#この部屋に 2 メートル × 1 メートルの区別できない畳 (長方形のタイル) A 枚と、1 メートル × 1 メートルの区別できない半畳 (正方形のタイル) B 枚を敷き詰めます。
#2 メートル × 1 メートルの畳は縦長にも横長にも使うことができます。
#敷き詰める方法は何通りあるでしょうか？
#なお、2A + B = HW であることが保証されます。
#また、回転や反転を行うことで初めて一致するような敷き詰め方は区別します。
#
#制約
#入力は全て整数
#1 ≤ H, W
#HW ≤ 16
#0 ≤ A, B
#2A + B = HW
#
#入力
#入力は以下の形式で標準入力から与えられる。
#H W A B
#
#出力
#答えを出力せよ。
#
#入力例 1
#2 2 1 2
#
#出力例 1
#4
#以下の 4 つです。
#
#入力例 2
#3 3 4 1
#
#出力例 2
#18
#以下の 6 つと、これらを回転させたものが含まれます。
#
#入力例 3
#4 4 8 0
#
#出力例 3
#36

def 