#問題文
#シカのAtCoDeerくんは友達のTopCoDeerくんとあるゲームをして対戦しています。
#このゲームは N ターンからなります。各ターンではそれぞれのプレイヤーはじゃんけんのグーかパーを出します。ただし、各プレイヤーは次の条件を満たす必要があります。
#(※) 各ターンの後で、(今までにパーを出した回数)≦(今までにグーを出した回数)　を満たす
#このゲームでの各プレイヤーの得点は、(勝ったターンの数) - (負けたターンの数) です。
#AtCoDeerくんは特殊能力を持っているので、ゲームが始まる前にTopCoDeerくんの出す N ターンの手を全て知ることが出来ました。 AtCoDeerくんの各ターンでの手を決めて、AtCoDeerくんの得点を最大化してください。
#TopCoDeerくんの出す手の情報は文字列 s で与えられます。 s の i(1≦i≦N) 文字目が gのときは i ターン目でTopCoDeerくんがグーを出すことを、 pのときはパーを出すことを表します。
#
#制約
#1≦N≦10^5
#N=|s|
#s の各文字はgかp
#s で表される手は、条件(※)を満たしている
#
#入力
#入力は以下の形式で標準入力から与えられる。
#s
#
#出力
#AtCoDeerくんの得点の最大値を出力せよ。
#
#入力例 1
#gpg
#
#出力例 1
#0
#常に相手とあいこになるように手を出すことで、0点を取ることができて、これが最大値です。
#
#入力例 2
#ggppgggpgg
#
#出力例 2
#2
#例えばグー,パー,グー,パー,グー,グー,パー,パー,グー,パー と出すことで、 3回勝って1回負けているので得点は2点になり、これが最大値です。

def 