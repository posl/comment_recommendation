#問題文
#snuke 君は自転車を買いに来ました。
# snuke 君はすでに買う自転車を決めたのですが、その自転車にはベルが付いていないため、
# 自転車とは別にベルも買う必要があります。
#snuke 君は安全意識が高いので、ベルをどちらの手でも鳴らせるよう、両方のハンドルに 1 つずつ
#付けることにしました。
#お店にあるベルは 3 種類で、それぞれ a円、 b円、 c円です。
#この 3 つのうち、異なる 2 つのベルを選んで買うときの、値段の合計の最小値を求めて下さい。
#
#制約
#1 ≦ a,b,c ≦ 10000
#a,b,c は整数
#
#入力
#入力は以下の形式で標準入力から与えられる。
#a b c
#
#出力
#2 つのベルを買うときの最安値を出力せよ。
#
#入力例 1
#700 600 780
#
#出力例 1
#1300
#700 円のベルと 600 円のベルを買うと、 1300 円かかります。
#700 円のベルと 780 円のベルを買うと、 1480 円かかります。
#600 円のベルと 780 円のベルを買うと、 1380 円かかります。
#よって、一番安いのは 1300 円です。
#
#入力例 2
#10000 10000 10000
#
#出力例 2
#20000
#どの 2 つを選んでも 20000 円かかってしまいます。

def 