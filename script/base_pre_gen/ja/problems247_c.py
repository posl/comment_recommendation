#問題文
#列 S_n を次のように定義します。
#S_1 は 1 つの 1 からなる長さ 1 の列である。
#S_n (n は 2 以上の整数) は S_{n-1}, n, S_{n-1} をこの順につなげた列である。
#たとえば S_2,S_3 は次のような列です。
#S_2 は S_1, 2, S_1 をこの順につなげた列なので 1,2,1 である。
#S_3 は S_2, 3, S_2 をこの順につなげた列なので 1,2,1,3,1,2,1 である。
#N が与えられるので、列 S_N をすべて出力してください。
#
#制約
#N は整数
#1 ≦ N ≦ 16
#
#入力
#入力は以下の形式で標準入力から与えられる。
#N
#
#出力
#S_N を空白区切りで出力せよ。
#
#入力例 1
#2
#
#出力例 1
#1 2 1
#問題文の説明にある通り、S_2 は 1,2,1 となります。
#
#入力例 2
#1
#
#出力例 2
#1
#
#入力例 3
#4
#
#出力例 3
#1 2 1 3 1 2 1 4 1 2 1 3 1 2 1
#S_4 は S_3,4,S_3 をこの順につなげた列です。

def 