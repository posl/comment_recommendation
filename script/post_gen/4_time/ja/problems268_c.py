#問題文
#回転テーブルの周りに人 0、人 1、...、人 N-1 がこの順番で反時計回りに等間隔で並んでいます。また、人 i の目の前には料理 p_i が置かれています。
#あなたは次の操作を 0 回以上何度でも行うことが出来ます。
#回転テーブルを反時計回りに 1 周の (1/(N)) だけ回す。これによって、(この操作の直前に)人 i の目の前にあった料理は人 (i+1) mod N の目の前に移動する。
#操作を完了させた後において、人 i は料理 i が人 (i-1) mod N、人 i、人 (i+1) mod N のいずれかの目の前に置かれていると喜びます。
#喜ぶ人数の最大値を求めてください。
# a mod m とは 整数 a と正整数 m に対し、a mod m は a-x が m の倍数となるような 0 以上 m 未満の整数 x を表します。(このような x は一意に定まることが証明できます) 
#
#制約
#3 ≦ N ≦ 2 × 10^5
#0 ≦ p_i ≦ N-1
#i ≠ j ならば p_i ≠ p_j
#入力はすべて整数
#
#入力
#入力は以下の形式で標準入力から与えられる。
#N
#p_0 ... p_{N-1}
#
#出力
#答えを出力せよ。
#
#入力例 1
#4
#1 2 0 3
#
#出力例 1
#4
#操作を 1 回行うと下の画像のようになります。
#この時、4 人が喜ぶことを以下のように確かめられます。
#人 0 は料理 0 が人 3 (=(0-1) mod 4) の目の前に置かれているので喜びます。
#人 1 は料理 1 が人 1 (=1) の目の前に置かれているので喜びます。
#人 2 は料理 2 が人 2 (=2) の目の前に置かれているので喜びます。
#人 3 は料理 3 が人 0 (=(3+1) mod 4) の目の前に置かれているので喜びます。
#5 人以上が喜ぶことは無いため、答えは 4 です。
#
#入力例 2
#3
#0 1 2
#
#出力例 2
#3
#
#入力例 3
#10
#3 9 6 1 7 2 8 0 5 4
#
#出力例 3
#5

def 