#問題文
#整数 N が与えられます。 
#N が -2^{31} 以上かつ 2^{31} 未満ならば Yes を、そうでないならば No を出力してください。
#
#制約
#-2^{63} ≦ N < 2^{63}
#N は整数である。
#
#入力
#入力は以下の形式で標準入力から与えられる。
#N
#
#出力
#N が -2^{31} 以上かつ 2^{31} 未満ならば Yes を、そうでないならば No を出力せよ。
#
#入力例 1
#10
#
#出力例 1
#Yes
#10 は -2^{31} 以上かつ 2^{31} 未満であるので、Yes を出力します。
#
#入力例 2
#-9876543210
#
#出力例 2
#No
#-9876543210 は -2^{31} 未満であるので、No を出力します。
#
#入力例 3
#483597848400000
#
#出力例 3
#No
#483597848400000 は 2^{31} 以上であるので、No を出力します。

def 