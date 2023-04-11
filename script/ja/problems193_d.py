#問題文
#1, 2, ..., 9 が表に書かれたカードが K 枚ずつ、計 9K 枚のカードがあります。
#これらのカードをランダムにシャッフルして、高橋くんと青木くんにそれぞれ、4 枚を表向きに、1 枚を裏向きにして配りました。
#高橋くんに配られたカードが文字列 S として、青木くんに配られたカードが文字列 T として与えられます。
#S, T は 5 文字の文字列で、先頭 4 文字は 1, 2, ..., 9 からなり、表向きのカードに書かれた数を表します。
#末尾 1 文字は # であり、裏向きのカードであることを表します。
#5 枚の手札の点数を、c_i をその手札に含まれる i の枚数として、 sum_{i=1}^9 i × 10^{c_i} で定義します。
#高橋くんが青木くんより点数の高い手札を持っていたら高橋くんの勝ちです。
#高橋くんの勝つ確率を求めてください。 
#
#制約
#2 ≤ K ≤ 10^5
#|S| = |T| = 5
#S, T の 1 文字目から 4 文字目は 1, 2, ..., 9 のいずれか
#1, 2, ..., 9 はそれぞれ、S と T に合計 K 回までしか出現しない
#S, T の 5 文字目は #
#
#入力
#入力は以下の形式で標準入力から与えられる。
#K
#S
#T
#
#出力
#高橋くんの勝つ確率を小数で出力せよ。
#想定解答との絶対誤差または相対誤差が 10^{-5} 以下であれば正解と判定される。
#
#入力例 1
#2
#1144#
#2233#
#
#出力例 1
#0.4444444444444444
#例えば、高橋くんの手札が 11449 、青木くんの手札が 22338 の場合、高橋くんの点数は 100+2+3+400+5+6+7+8+90=621 、青木くんの点数は 1+200+300+4+5+6+7+80+9=612 で、高橋くんの勝ちになります。
#裏向きのカードの大小によって勝敗が決まるので、高橋くんの勝つ確率は frac49 です。
#
#入力例 2
#2
#9988#
#1122#
#
#出力例 2
#1.0
#
#入力例 3
#6
#1122#
#2228#
#
#出力例 3
#0.001932367149758454
#高橋くんの手札が 11222 、青木くんの手札が 22281 の場合にのみ高橋くんの勝ちになります。
#高橋くんの勝つ確率は (2/1035) です。
#
#入力例 4
#100000
#3226#
#3597#
#
#出力例 4
#0.6296297942426154

def 