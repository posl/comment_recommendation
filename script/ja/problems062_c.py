#問題文
#縦 H ブロック、横 W ブロックの板チョコがあります。
#すぬけ君は、この板チョコをちょうど 3 つのピースに分割しようとしています。
#ただし、各ピースはブロックの境目に沿った長方形でなければなりません。
#すぬけ君は、3 つのピースの面積 (ブロック数) をできるだけ均等にしようとしています。
#具体的には、3 つのピースの面積の最大値を S_{max}、最小値を S_{min} としたとき、S_{max} - S_{min} を最小化しようとしています。
#S_{max} - S_{min} の最小値を求めてください。
#
#制約
#2 ≤ H, W ≤ 10^5
#
#入力
#入力は以下の形式で標準入力から与えられる。
#H W
#
#出力
#S_{max} - S_{min} の最小値を出力せよ。
#
#入力例 1
#3 5
#
#出力例 1
#0
#次図のように分割すると、S_{max} - S_{min} = 5 - 5 = 0 となります。
#
#
#入力例 2
#4 5
#
#出力例 2
#2
#次図のように分割すると、S_{max} - S_{min} = 8 - 6 = 2 となります。
#
#
#入力例 3
#5 5
#
#出力例 3
#4
#次図のように分割すると、S_{max} - S_{min} = 10 - 6 = 4 となります。
#
#
#入力例 4
#100000 2
#
#出力例 4
#1
#
#入力例 5
#100000 100000
#
#出力例 5
#50000

def 