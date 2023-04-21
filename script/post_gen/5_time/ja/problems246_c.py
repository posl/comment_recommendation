#問題文
#N 個の商品があります。i = 1, 2, ..., N について、i 番目の商品の値段は A_i 円です。
#高橋君は K 枚のクーポンを持っています。
#1 枚のクーポンは 1 つの商品に対して使用することができ、1 つの商品に対してはクーポンを何枚でも（ 0 枚でもよい）使用することができます。
#値段が a 円の商品に対して k 枚のクーポンを使用すると、その商品を max{a - kX, 0} 円で買うことができます。
#高橋君がすべての商品を買うために支払う合計金額の最小値を出力してください。
#
#制約
#1 ≦ N ≦ 2 × 10^5
#1 ≦ K, X ≦ 10^9
#1 ≦ A_i ≦ 10^9
#入力はすべて整数
#
#入力
#入力は以下の形式で標準入力から与えられる。
#N K X
#A_1 A_2 ... A_N
#
#出力
#答えを出力せよ。
#
#入力例 1
#5 4 7
#8 3 10 5 13
#
#出力例 1
#12
#1 番目の商品に対してクーポン 1 枚、3 番目の商品に対してクーポン 1 枚、5 番目の商品に対してクーポン 2 枚を使用すると、
#1 番目の商品を max{A_1-X, 0 } = 1 円で買うことができ、
#2 番目の商品を max{A_2, 0 } = 3 円で買うことができ、
#3 番目の商品を max{A_3-X, 0 } = 3 円で買うことができ、
#4 番目の商品を max{A_4, 0 } = 5 円で買うことができ、
#5 番目の商品を max{A_5-2X, 0 } = 0 円で買うことができます。
#よって、すべての商品を 1 + 3 + 3 + 5 + 0 = 12 円で買うことができ、これが最小です。
#
#入力例 2
#5 100 7
#8 3 10 5 13
#
#出力例 2
#0
#
#入力例 3
#20 815 60
#2066 3193 2325 4030 3725 1669 1969 763 1653 159 5311 5341 4671 2374 4513 285 810 742 2981 202
#
#出力例 3
#112

def 