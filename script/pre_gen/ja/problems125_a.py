#問題文
#ビスケット生産装置を起動すると、起動してから A 秒後、2A 秒後、3A 秒後、... (A の倍数秒後) に B 枚ずつビスケットを生産します。
#ビスケット生産装置を起動してから T + 0.5 秒後までに生産されるビスケットの合計枚数を求めてください。
#
#制約
#入力は全て整数である。
#1 ≦ A, B, T ≦ 20
#
#入力
#入力は以下の形式で標準入力から与えられる。
#A B T
#
#出力
#ビスケット生産装置を起動してから T + 0.5 秒後までに生産されるビスケットの合計枚数を出力せよ。
#
#入力例 1
#3 5 7
#
#出力例 1
#10
#ビスケット生産装置を起動してから 3 秒後に 5 枚のビスケットが生産されます。
#ビスケット生産装置を起動してから 6 秒後に 5 枚のビスケットが生産されます。
#したがって、ビスケット生産装置を起動してから 7.5 秒後までに合計 10 枚のビスケットが生産されます。
#
#入力例 2
#3 2 9
#
#出力例 2
#6
#
#入力例 3
#20 20 19
#
#出力例 3
#0

def 