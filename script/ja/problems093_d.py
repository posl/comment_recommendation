#問題文
#高橋君を含めた 10^{10^{10}} 人の参加者が 2 回のプログラミングコンテストに参加しました。
#各コンテストでは全員に 1 位から 10^{10^{10}} 位までの相異なる順位がつきました。
#参加者のスコアとは、2 回のコンテストでの順位を掛け合わせた値です。
#次のクエリ Q 個に答えてください。
#i 個目のクエリでは、2 つの正の整数 A_i,B_i が与えられる。高橋君が 1 回目のコンテストで A_i 位、2 回目のコンテストで B_i 位を取ったと仮定して、高橋君よりスコアの小さい参加者の人数の最大値を求めよ。
#
#制約
#1 ≦ Q ≦ 100
#1≦ A_i,B_i≦ 10^9(1≦ i≦ Q)
#入力はすべて整数である
#
#入力
#入力は以下の形式で標準入力から与えられる。
#Q
#A_1 B_1
#:
#A_Q B_Q
#
#出力
#クエリごとに、高橋君よりスコアの小さい参加者の人数の最大値を出力せよ。
#
#入力例 1
#8
#1 4
#10 5
#3 3
#4 11
#8 9
#22 40
#8 36
#314159265 358979323
#
#出力例 1
#1
#12
#4
#11
#14
#57
#31
#671644785
#1 回目のコンテストで x 位を、2 回目のコンテストで y 位を取った参加者を (x,y) で表すことにします。
#1 つめのクエリでは、高橋君よりスコアの小さい参加者として (2,1) が考えられます。2 人以上のスコアが高橋君のスコアより小さくなることはないため、1 を出力します。

def 