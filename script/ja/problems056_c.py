#問題文
#無限に左右に伸びている数直線上の 0 の地点に時刻 0 にカンガルーがいます。
#カンガルーは時刻 i-1 から i にかけて、なにもしないか、もしくは長さがちょうど i のジャンプを、左右どちらかの方向を選んで行えます。
#つまり、時刻 i-1 に座標 x にいたとすると、時刻 i には x-i, x, x+i のどれかに存在することが出来ます。
#カンガルーの家は座標 X にあります。カンガルーはできるだけ早く座標 X まで移動しようとしています。
#カンガルーが座標 X に到着する時刻の最小値を求めてください。
#
#制約
#X は整数
#1≦X≦10^9
#
#入力
#入力は以下の形式で標準入力から与えられる。
#X
#
#出力
#カンガルーが座標 X に到着する時刻の最小値を出力せよ。
#
#入力例 1
#6
#
#出力例 1
#3
#3 回右にジャンプすると時刻 3 に家にたどり着けて、これが最小です。
#
#入力例 2
#2
#
#出力例 2
#2
#時刻 0 にはなにもせず、時刻 1 に右にジャンプすることで時刻 2 に家にたどり着けます。
#
#入力例 3
#11
#
#出力例 3
#5

def 