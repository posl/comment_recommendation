#問題文
#空港 A, B, C があり、それぞれの空港の間では、双方向に飛行機が運航しています。
#空港 A, B 間の飛行時間は片道 P 時間、空港 B, C 間の飛行時間は片道 Q 時間、空港 C, A 間の飛行時間は片道 R 時間です。
#いずれかの空港からスタートして他の空港に飛行機で移動し、さらにそのどちらでもない空港に飛行機で移動するような経路を考えます。
#飛行時間の和は最短で何時間になるでしょうか。
#
#制約
#1 ≦ P,Q,R ≦ 100
#入力は全て整数である
#
#入力
#入力は以下の形式で標準入力から与えられる。
#P Q R
#
#出力
#飛行時間の和の最小値を出力せよ。
#
#入力例 1
#1 3 4
#
#出力例 1
#4
#A, B, C の順に移動する経路の飛行時間の和は、1 + 3 = 4 時間
#A, C, B の順に移動する経路の飛行時間の和は、4 + 3 = 7 時間
#B, A, C の順に移動する経路の飛行時間の和は、1 + 4 = 5 時間
#B, C, A の順に移動する経路の飛行時間の和は、3 + 4 = 7 時間
#C, A, B の順に移動する経路の飛行時間の和は、4 + 1 = 5 時間
#C, B, A の順に移動する経路の飛行時間の和は、3 + 1 = 4 時間
#であるので、これらの最小値は 4 時間です。
#
#入力例 2
#3 2 3
#
#出力例 2
#5

def 