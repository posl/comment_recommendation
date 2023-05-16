#問題文
#高橋君は、英小文字から成る文字列 S を持っています。
#この S から始めて、ある与えられた手順に従って文字列を作ることにしました。
#手順は Q 回の操作から成ります。操作 i(1 ≦ i ≦ Q) では、まず整数 T_i が与えられます。
#T_i = 1 のとき : 文字列 S の前後を反転する。
#T_i = 2 のとき : 追加で整数 F_i と英小文字 C_i が与えられる。
#F_i = 1 のとき : 文字列 S の先頭に C_i を追加する。
#F_i = 2 のとき : 文字列 S の末尾に C_i を追加する。
#
#高橋君のために、手順の後に最終的にできる文字列を求めてあげてください。
#
#制約
#1 ≦ |S| ≦ 10^5
#S は英小文字から成る
#1 ≦ Q ≦ 2 × 10^5
#T_i = 1 または 2
#F_i = 1 または 2
#C_i は英小文字である
#
#入力
#入力は以下の形式で標準入力から与えられる。
#S
#Q
#Query_1
#:
#Query_Q
#3 行目から Q + 2 行目の Query_i は、以下の 2 つのいずれかである。
#1
#T_i = 1 として操作を行うことを表す。
#2 F_i C_i
#T_i = 2 として操作を行うことを表す。
#
#出力
#手順の後に最終的にできる文字列を出力せよ。
#
#入力例 1
#a
#4
#2 1 p
#1
#2 2 c
#1
#
#出力例 1
#cpa
#Q = 4 回の操作を行います。初め S は a です。
#操作 1 : S の先頭に p を追加する。S は pa となる。
#操作 2 : S の前後を反転する。S は ap となる。
#操作 3 : S の末尾に c を追加する。S は apc となる。
#操作 4 : S の前後を反転する。S は cpa となる。
#よって最終的にできる文字列は cpa となります。
#
#入力例 2
#a
#6
#2 2 a
#2 1 b
#1
#2 2 c
#1
#1
#
#出力例 2
#aabc
#Q = 6 回の操作を行います。初め S は a です。
#操作 1 : S は aa となる。
#操作 2 : S は baa となる。
#操作 3 : S は aab となる。
#操作 4 : S は aabc となる。
#操作 5 : S は cbaa となる。
#操作 6 : S は aabc となる。
#よって最終的にできる文字列は aabc となります。
#
#入力例 3
#y
#1
#2 1 x
#
#出力例 3
#xy

def 