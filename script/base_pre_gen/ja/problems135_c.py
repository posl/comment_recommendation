#問題文
#N+1 個の街があり、i 番目の街は A_i 体のモンスターに襲われています。
#N 人の勇者が居て、i 番目の勇者は i 番目または i+1 番目の街を襲っているモンスターを合計で B_i 体まで倒すことができます。
#N 人の勇者がうまく協力することで、合計して最大で何体のモンスターを倒せるでしょうか。
#
#制約
#入力は全て整数である。
#1 ≦ N ≦ 10^5
#1 ≦ A_i ≦ 10^9
#1 ≦ B_i ≦ 10^9
#
#入力
#入力は以下の形式で標準入力から与えられる。
#N
#A_1 A_2 ... A_{N+1}
#B_1 B_2 ... B_N
#
#出力
#合計して倒せるモンスターの数の最大値を出力せよ。
#
#入力例 1
#2
#3 5 2
#4 5
#
#出力例 1
#9
#以下のようにモンスターを倒すと、合計 9 体のモンスターを倒すことができ、このときが最大です。
#1 番目の勇者が 1 番目の街を襲っているモンスターを 2 体、2 番目の街を襲っているモンスターを 2 体倒します。
#2 番目の勇者が 2 番目の街を襲っているモンスターを 3 体、3 番目の街を襲っているモンスターを 2 体倒します。
#
#入力例 2
#3
#5 6 3 8
#5 100 8
#
#出力例 2
#22
#
#入力例 3
#2
#100 1 1
#1 100
#
#出力例 3
#3

def 