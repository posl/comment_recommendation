#問題文
#ある合宿におやつとしてチョコレートが何個か準備されました。
#合宿は N 人が参加して D 日間行われました。
#i 人目の参加者 (1 ≦ i ≦ N) は合宿の 1, A_i + 1, 2A_i + 1, ... 日目にチョコレートを 1 個ずつ食べました。
#その結果、合宿終了後に残っていたチョコレートは X 個となりました。また、合宿の参加者以外がチョコレートを食べることはありませんでした。
#合宿開始前に準備されていたチョコレートの個数を求めてください。
#
#制約
#1 ≦ N ≦ 100
#1 ≦ D ≦ 100
#1 ≦ X ≦ 100
#1 ≦ A_i ≦ 100 (1 ≦ i ≦ N)
#
#入力
#入力は以下の形式で標準入力から与えられる。
#N
#D X
#A_1
#A_2
#:
#A_N
#
#出力
#合宿開始前に準備されていたチョコレートの個数を出力せよ。
#
#入力例 1
#3
#7 1
#2
#5
#10
#
#出力例 1
#8
#3 人が 7 日間の合宿に参加します。
#それぞれの参加者は以下のようにチョコレートを食べます。
#1 人目の参加者は、1, 3, 5, 7 日目にチョコレートを 1 個ずつ、合計 4 個食べます。
#2 人目の参加者は、1 日目および 6 日目にチョコレートを 1 個ずつ、合計 2 個食べます。
#3 人目の参加者は、1 日目だけにチョコレートを食べます。食べるチョコレートは合計 1 個です。
#合宿終了後に残っていたチョコレートは 1 個であるので、合宿開始前に準備されていたチョコレートは 1 + 4 + 2 + 1 = 8 個あったことになります。
#
#入力例 2
#2
#8 20
#1
#10
#
#出力例 2
#29
#
#入力例 3
#5
#30 44
#26
#18
#81
#18
#6
#
#出力例 3
#56

def 