#問題文
#あるプログラミングコンテストの予選に N 人が参加し、参加者全員が異なる順位を得ました。 
#長さ N の文字列 S が与えられ、この文字列は決勝への参加希望の有無を表現します。具体的には下記の通りです。
#S の i 文字目が o なら、予選 i 位の参加者が決勝への参加を希望した。
#S の i 文字目が x なら、予選 i 位の参加者が決勝への参加を希望しなかった。
#決勝への参加を希望した参加者のうち順位の小さい方から K 人が予選を通過します。
#以下の条件を満たす長さ N の文字列 T を出力してください。
#予選 i 位の参加者が予選を通過する場合、 T の i 文字目は o
#予選 i 位の参加者が予選を通過しない場合、 T の i 文字目は x
#
#制約
#N,K は整数
#1 ≦ K ≦ N ≦ 100
#S は o と x からなる長さ N の文字列
#S には少なくとも K 個の o が含まれる
#
#入力
#入力は以下の形式で標準入力から与えられる。
#N K
#S
#
#出力
#答えを出力せよ。
#
#入力例 1
#10 3
#oxxoxooxox
#
#出力例 1
#oxxoxoxxxx
#この入力の場合、予選の参加者は N=10 人であり、予選を通過する人数は K=3 人です。
#予選 1 位の参加者は決勝への参加を希望しているため、予選を通過します。この時点で、通過者は 1 人です。
#予選 2,3 位の参加者は決勝への参加を希望していないため、予選を通過しません。
#予選 4 位の参加者は決勝への参加を希望しているため、予選を通過します。この時点で、通過者は 2 人です。
#予選 5 位の参加者は決勝への参加を希望していないため、予選を通過しません。
#予選 6 位の参加者は決勝への参加を希望しているため、予選を通過します。この時点で、通過者は 3 人です。
#ここで、予選を通過した人数が 3 人となりました。なので、予選 7 位以下の参加者は予選を通過しません。

def 