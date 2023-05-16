#問題文
#N 曲からなるプレイリストがあり、曲には 1, ..., N の番号が付けられています。
#曲 i の長さは A_i 秒です。
#プレイリストを再生すると、曲 1、曲 2、...、曲 N の順に流れます。曲 N が流れ終わると、再び曲 1 から順に流れていきます。ある曲の途中で次の曲が流れることはなく、曲が流れ終わると、その瞬間に次の曲が流れ始めます。
#プレイリストを再生してから T 秒後に流れているのはどの曲ですか？また、その曲が流れ始めてから何秒の時点ですか？
#ただし、T 秒後ちょうどに曲が切り替わるような入力は与えられません。
#
#制約
#1 ≦ N ≦ 10^5
#1 ≦ T ≦ 10^{18}
#1 ≦ A_i ≦ 10^9
#プレイリストを再生して T 秒後ちょうどに曲が切り替わることはない
#入力される値は全て整数
#
#入力
#入力は以下の形式で標準入力から与えられる。
#N T
#A_1 ... A_N
#
#出力
#プレイリストを再生してから T 秒後に流れている曲の番号と、その曲が流れ始めてから何秒たったかを表す整数を空白区切りで出力せよ。
#
#入力例 1
#3 600
#180 240 120
#
#出力例 1
#1 60
#プレイリストを再生してからの様子は次のようになります。
#0 秒後から 180 秒後まで曲 1 が流れる。
#180 秒後から 420 秒後まで曲 2 が流れる。
#420 秒後から 540 秒後まで曲 3 が流れる。
#540 秒後から 720 秒後まで曲 1 が流れる。
#720 秒後から 960 秒後まで曲 2 が流れる。
#.
#.
#.
#600 秒後の時点で流れているのは曲 1 であり、流れ始めて 60 秒の時点です。
#
#入力例 2
#3 281
#94 94 94
#
#出力例 2
#3 93
#
#入力例 3
#10 5678912340
#1000000000 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000
#
#出力例 3
#6 678912340

def 