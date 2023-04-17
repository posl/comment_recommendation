#問題文
#N 個の文字列 S_1,...,S_N が与えられます。各文字列は AND または OR です。
#値が True または False であるような N+1 個の変数の組 (x_0,...,x_N) であって、
#以下のような計算を行った際に、y_N が True となるようなものの個数を求めてください。
#y_0=x_0
#i≧ 1 のとき、S_i が AND なら y_i=y_{i-1} ∧ x_i、S_i が OR なら y_i=y_{i-1} ∨ x_i
#a ∧ b は a と b の論理積を表し、a ∨ b は a と b の論理和を表します。  
#
#制約
#1 ≦ N ≦ 60
#S_i は AND または OR
#
#入力
#入力は以下の形式で標準入力から与えられる。
#N
#S_1
#.
#.
#.
#S_N
#
#出力
#答えを出力せよ。
#
#入力例 1
#2
#AND
#OR
#
#出力例 1
#5
#例えば (x_0,x_1,x_2)=(True,False,True) のとき
#y_0=x_0=True
#y_1=y_0 ∧ x_1 = True ∧ False=False
#y_2=y_1 ∨ x_2 = False ∨ True=True
#となり、y_2 は True になります。
#y_2 が True となるような (x_0,x_1,x_2) の組み合わせは、
#(True,True,True)
#(True,True,False)
#(True,False,True)
#(False,True,True)
#(False,False,True)
#の 5 通りで全てです。
#
#入力例 2
#5
#OR
#OR
#OR
#OR
#OR
#
#出力例 2
#63
#全てが False のときを除く 2^6-1 通りで y_5 は True になります。

def 