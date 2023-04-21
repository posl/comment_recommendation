#問題文
#キーエンスには N 個の部署があり、i(1 ≦ i ≦ N) 番目の部署には A_i 人の社員が所属しています。異なる部署に同じ社員が所属していることはありません。
#キーエンスは、部署をまたいだ全社横断プロジェクトを計画しています。1 つのプロジェクトは K 個の相異なる部署から 1 人ずつ選出して作り、ちょうど K 人から構成されるようにします。
#プロジェクトは最大でいくつ作れますか？ただし、1 人が複数のプロジェクトに参加することはできません。
#
#制約
#1 ≦ K ≦ N ≦ 2 × 10^5
#1 ≦ A_i ≦ 10^{12}
#入力は全て整数
#
#入力
#入力は以下の形式で標準入力から与えられる。
#N K
#A_1 A_2 ... A_N
#
#出力
#プロジェクトの個数の最大値を出力せよ。
#
#入力例 1
#3 3
#2 3 4
#
#出力例 1
#2
#3 個の部署それぞれから 1 人ずつ選出したプロジェクトを 2 つ作ることができます。
#
#入力例 2
#4 2
#1 1 3 4
#
#出力例 2
#4
#
#入力例 3
#4 3
#1 1 3 4
#
#出力例 3
#2

def 