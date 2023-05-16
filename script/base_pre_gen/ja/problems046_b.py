#問題文
#シカのAtCoDeerくんは一列に並んだ N 個のボールをそれぞれ K 色のペンキの色のうちのどれかで塗ろうとしています。見栄えが悪くならないように、隣り合ったボールは別の色で塗ることにします。ボールの塗り方としてあり得るものの個数を求めてください。
#
#制約
#1≦N≦1000
#2≦K≦1000
#答えは 2^{31}-1 以下
#
#入力
#入力は以下の形式で標準入力から与えられる。
#N K
#
#出力
#ボールの塗り方としてあり得るものの個数を出力せよ。
#
#入力例 1
#2 2
#
#出力例 1
#2
#色を0,1で表すと、左のボールを0で塗り、右のボールを1で塗る という方法と、 左のボールを1で塗り、右のボールを0で塗る という方法の2通りがあります。
#
#入力例 2
#1 10
#
#出力例 2
#10
#ボールは一つしか無いため,10色のうちどれを使っても良いので答えは10通りです。
#
#入力例 3
#10 8
#
#出力例 3
#322828856

def 