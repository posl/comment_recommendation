#問題文
#N 個の整数の列 A_1, ..., A_N が与えられます。
#これらの逆数の総和の逆数 (1/((1/(A_1)) + ... + (1/(A_N)))) を求めてください。
#
#制約
#1 ≦ N ≦ 100
#1 ≦ A_i ≦ 1000
#
#入力
#入力は以下の形式で標準入力から与えられる。
#N
#A_1 A_2 ... A_N
#
#出力
#(1/((1/(A_1)) + ... + (1/(A_N)))) の値を表す小数 (または整数) を出力せよ。
#出力は、ジャッジの出力との絶対誤差または相対誤差が 10^{-5} 以下のとき正解と判定される。
#
#入力例 1
#2
#10 30
#
#出力例 1
#7.5
#(1/((1/(10)) + (1/(30)))) = (1/((4/(30)))) = ((30)/(4)) = 7.5 です。
#なお、7.50001, 7.49999 などと出力しても正解と判定されます。
#
#入力例 2
#3
#200 200 200
#
#出力例 2
#66.66666666666667
#(1/((1/(200)) + (1/(200)) + (1/(200)))) = (1/((3/(200)))) = ((200)/(3)) = 66.6666... です。
#なお、6.66666e+1 などと出力しても正解と判定されます。
#
#入力例 3
#1
#1000
#
#出力例 3
#1000
#(1/((1/(1000)))) = 1000 です。
#なお、+1000.0 などと出力しても正解と判定されます。

def 