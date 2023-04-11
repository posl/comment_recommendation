#問題文
#2 次元平面上に中心 (X, Y) 、半径 R の円があります。
#この円の内部または周上にある格子点 (x, y 座標がともに整数である点) の個数を求めてください。
#
#制約
#|X| ≦ 10^5
#|Y| ≦ 10^5
#0 < R ≦ 10^5
#X, Y, R は高々小数第 4 位まで与えられる
#
#入力
#入力は以下の形式で標準入力から与えられる。
#X Y R
#
#出力
#答えを出力せよ。
#
#入力例 1
#0.2 0.8 1.1
#
#出力例 1
#3
#以下のような円になります。赤く印の付いた点が、この円の内部または周上にある格子点です。
#
#入力例 2
#100 100 1
#
#出力例 2
#5
#X, Y, R には小数点が含まれないかもしれません。
#円周上の格子点も数える対象に含むことに注意してください。  
#
#入力例 3
#42782.4720 31949.0192 99999.99
#
#出力例 3
#31415920098

def 