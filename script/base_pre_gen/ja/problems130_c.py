#問題文
#平面上に長方形があり、4 つの頂点の座標は (0,0),(W,0),(W,H),(0,H) です。
#この長方形の内部または周上の点 (x,y) が与えられます。(x,y) を通る直線で長方形を 2 つの部分に分割するとき、
#面積の大きくない方の面積の最大値を求めてください。また、その最大値を達成する分割の方法が複数あるかも判定してください。
#
#制約
#1 ≦ W,H ≦ 10^9
#0≦ x≦ W
#0≦ y≦ H
#入力はすべて整数である
#
#入力
#入力は以下の形式で標準入力から与えられる。
#W H x y
#
#出力
#はじめに、面積の大きくない方の面積の最大値を出力せよ。つづいて、その最大値を達成する分割の方法が複数あるなら 1 を、そうでないなら 0 を出力せよ。
#出力された面積は、絶対誤差あるいは相対誤差が 10^{-9} 以下の時正答と判定される。
#
#入力例 1
#2 3 1 2
#
#出力例 1
#3.000000 0
#直線 x=1 で分割するのが最適です。また、最適な分割方法はこれ以外には存在しません。
#
#入力例 2
#2 2 1 1
#
#出力例 2
#2.000000 1

def 