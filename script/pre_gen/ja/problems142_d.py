#問題文
#正整数 A, B が与えられます。
#A と B の正の公約数の中からいくつかを選びます。
#ただし、選んだ整数の中のどの異なる 2 つの整数についても互いに素でなければなりません。
#最大でいくつ選べるでしょうか。
#公約数とは
#整数 d が整数 x と整数 y の公約数であるとは、d が x と y をともに割り切ることをいいます。
#互いに素とは
#整数 x, y が互いに素であるとは、x, y の正の公約数が 1 のみであることをいいます。
#割り切るとは
#整数 x が整数 y を割り切るとは、y = alpha x なる整数 alpha が存在することをいいます。
#
#制約
#入力は全て整数である。
#1 ≦ A, B ≦ 10^{12}
#
#入力
#入力は以下の形式で標準入力から与えられる。
#A B
#
#出力
#条件を満たすように選べる整数の個数の最大値を出力せよ。
#
#入力例 1
#12 18
#
#出力例 1
#3
#12 と 18 の正の公約数は 1, 2, 3, 6 です。
#1 と 2、2 と 3、3 と 1 は互いに素なので、1, 2, 3 を選ぶことができ、このときが最大です。
#
#入力例 2
#420 660
#
#出力例 2
#4
#
#入力例 3
#1 2019
#
#出力例 3
#1
#1 と 2019 の正の公約数は 1 しかありません。

def 