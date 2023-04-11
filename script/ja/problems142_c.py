#問題文
#高橋くんは N 人の生徒たちのいるクラスの担当教師です。
#生徒たちには 1 から N までの出席番号が重複なく割り当てられています。
#今日は全ての生徒たちが相異なるタイミングで登校しました。
#高橋くんは、出席番号 i の生徒が登校した時点で、教室に A_i 人の生徒たちがいたことを記録しています(出席番号 i の生徒を含む)。
#記録された情報を元に、生徒たちの登校した順番を復元してください。
#
#制約
# 1 ≦ N ≦ 10^5 
# 1 ≦ A_i ≦ N 
# A_i ≠ A_j  (i ≠ j)
#入力はすべて整数
#
#入力
#入力は以下の形式で標準入力から与えられる。
#N
#A_1 A_2 ... A_N
#
#出力
#生徒たちの出席番号を登校した順に出力せよ。
#
#入力例 1
#3
#2 3 1
#
#出力例 1
#3 1 2
#最初に出席番号 3 の生徒が登校しました。
#続いて出席番号 1 の生徒が登校しました。
#最後に出席番号 2 の生徒が登校しました。
#
#入力例 2
#5
#1 2 3 4 5
#
#出力例 2
#1 2 3 4 5
#
#入力例 3
#8
#8 2 7 3 4 5 6 1
#
#出力例 3
#8 2 4 5 6 7 3 1

def 