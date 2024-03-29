#問題文
#祭壇に、左から右へと一列に並ぶ N 個の石が祀られています。左から i 個目 (1 ≦ i ≦ N) の石の色は文字 c_i として与えられ、c_i が R のとき赤、W のとき白です。
#あなたは、以下の二種の操作を任意の順に何度でも行うことができます。
#石を 2 個選び (隣り合っていなくてもよい)、それらを入れ替える。
#石を 1 個選び、その石の色を変える (赤なら白に、白なら赤に)。
#占い師によると、赤い石の左隣に置かれた白い石は災いを招きます。そのような白い石がない状態に至るには、最小で何回の操作が必要でしょうか。
#
#制約
#2 ≦ N ≦ 200000
#c_i は R または W
#
#入力
#入力は以下の形式で標準入力から与えられる。
#N
#c_{1}c_{2}...c_{N}
#
#出力
#必要な最小の操作回数を表す整数を出力せよ。
#
#入力例 1
#4
#WWRR
#
#出力例 1
#2
#例えば、以下の 2 回の操作で目的を達成できます。
#左から 1 番目の石と左から 3 番目の石を入れ替え、RWWR とする。
#左から 4 番目の石の色を変え、RWWW とする。
#
#入力例 2
#2
#RR
#
#出力例 2
#0
#一度も操作を行う必要がない可能性もあります。
#
#入力例 3
#8
#WRWWRWRR
#
#出力例 3
#3

def 