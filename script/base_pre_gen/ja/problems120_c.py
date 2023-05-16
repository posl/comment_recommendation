#問題文
#机の上に N 個のキューブが縦に積まれています。長さ N の文字列 S が与えられます。
#下から i 番目のキューブの色は、S の i 文字目が 0 のとき赤色、1 のとき青色です。
#あなたは、赤色のキューブと青色のキューブが隣り合っているような部分を選んで、それら 2 個のキューブを取り除く操作を何度でも行えます。
#このとき、取り除いたキューブの上にあったキューブは真下の物体の上に落下します。
#最大で何個のキューブを取り除けるでしょうか。
#
#制約
#1 ≦ N ≦ 10^5
#|S| = N
#S の各文字は 0 または 1 である。
#
#入力
#入力は以下の形式で標準入力から与えられる。
#S
#
#出力
#最大で何個のキューブを取り除けるかを出力せよ。
#
#入力例 1
#0011
#
#出力例 1
#4
#以下の順に操作を行うと 4 個全てのキューブを取り除けます。
#下から 2 番目のキューブと 3 番目のキューブを取り除きます。その結果、下から 4 番目のキューブが下から 1 番目のキューブの上に落下します。
#下から 1 番目のキューブと 2 番目のキューブを取り除きます。
#
#入力例 2
#11011010001011
#
#出力例 2
#12
#
#入力例 3
#0
#
#出力例 3
#0

def 