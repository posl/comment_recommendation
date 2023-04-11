#問題文
#N 個の町が一直線上に並んでいます。行商人の高橋君は町 1 から出発し、リンゴの売買をしながら町 N へと向かいます。
#はじめ高橋君は町 1 におり、リンゴを 1 つも持っていません。高橋君は次のいずれかの行動を繰り返し行います。
#移動: 町 i (i < N) にいるとき、町 i + 1 へ移動する。
#リンゴの売買: リンゴを好きな個数だけ売買する。ここで、町 i (1 ≦ i ≦ N) ではリンゴの買値も売値もともに A_i 円とする。ここで A_i は相異なる整数です。
#1 つの町で売買するリンゴの個数に制限はありませんが、旅の中で売買するリンゴの個数は合計で (買う個数と売る個数を合わせて) T 個以下にしなくてはなりません。
#高橋君は旅の利益、すなわちリンゴを売った代金から買った代金を引いた値を最大にするように旅をするとします。旅が終わったときに持っていたリンゴの価値は考えず、旅の中で売買した金額だけを考えます。
#この旅に先立って、青木君は任意の町 i に対して A_i を好きな非負整数 A_i' に変えるという操作を好きなだけ行うことができます。ただし、この操作は行うごとに |A_i - A_i'| のコストがかかります。操作後には異なる町の間でリンゴの値段が同じになっていても構いません。
#青木君の目的はできるだけ少ない合計コストの操作で高橋君の利益を少なくとも 1 円下げることです。合計コストの最小値を求めてください。
#ただし、元の状態で高橋君が 1 円以上の利益を上げられることは仮定して構いません。
#
#制約
#1 ≦ N ≦ 10^5
#1 ≦ A_i ≦ 10^9 (1 ≦ i ≦ N)
#A_i は相異なる
#2 ≦ T ≦ 10^9
#入力の状態では高橋君は 1 円以上の利益を上げられることが保証される
#
#入力
#入力は以下の形式で標準入力から与えられる。
#N T
#A_1 A_2 ... A_N
#
#出力
#高橋君の収益を少なくとも 1 円下げるために必要な合計コストの最小値を出力せよ。
#
#入力例 1
#3 2
#100 50 200
#
#出力例 1
#1
#この入力の状態では、高橋君は次のようにして最大の利益である 150 円を達成することができます。
#町 1 から町 2 へ移動する。
#町 2 で 50 円を支払い、リンゴを 1 個買う。
#町 2 から町 3 へ移動する。
#町 3 で 200 円でリンゴを 1 個売る。
#たとえば、青木君が町 2 のリンゴの値段を 50 円から 51 円に変えると、高橋君はどのようにしても 150 円の利益を上げることができなくなります。すなわち、コスト 1 で高橋君の利益を少なくとも 1 円下げることが可能であり、答えは 1 となります。
#他にも、町 3 のリンゴの値段を 200 円から 199 円に変えることでもコスト 1 で高橋君の利益を下げることが可能です。
#
#入力例 2
#5 8
#50 30 40 10 20
#
#出力例 2
#2
#
#入力例 3
#10 100
#7 10 4 5 9 3 6 8 2 1
#
#出力例 3
#2

def 