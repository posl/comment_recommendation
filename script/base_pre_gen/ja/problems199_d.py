#問題文
#N 頂点 M 辺の単純無向グラフがあります。頂点には 1 から N までの、辺には 1 から M までの番号がついています。
#辺 i は頂点 A_i と頂点 B_i を結んでいます。
#このグラフの各頂点を赤、緑、青の 3 色のいずれかで塗る方法であって、以下の条件を満たすものの数を求めてください。  
#辺で直接結ばれている 2 頂点は必ず異なる色で塗られている
#なお、使われない色があっても構いません。  
#
#制約
#1 ≦ N ≦ 20
#0 ≦ M ≦ ((N(N - 1))/(2))
#1 ≦ A_i ≦ N
#1 ≦ B_i ≦ N
#与えられるグラフは単純 (多重辺や自己ループを含まない)
#
#入力
#入力は以下の形式で標準入力から与えられる。
#N M
#A_1 B_1
#A_2 B_2
#A_3 B_3
#.
#.
#.
#A_M B_M
#
#出力
#答えを出力せよ。  
#
#入力例 1
#3 3
#1 2
#2 3
#3 1
#
#出力例 1
#6
#頂点 1, 2, 3 の色をそれぞれ c_1, c_2, c_3 とし、赤、緑、青をそれぞれ R, G, B で表すと、以下の 6 通りが条件を満たします。  
#c_1c_2c_3 =  RGB
#c_1c_2c_3 =  RBG
#c_1c_2c_3 =  GRB
#c_1c_2c_3 =  GBR
#c_1c_2c_3 =  BRG
#c_1c_2c_3 =  BGR
#
#入力例 2
#3 0
#
#出力例 2
#27
#辺がないため、各頂点の色を自由に決めることができます。  
#
#入力例 3
#4 6
#1 2
#2 3
#3 4
#2 4
#1 3
#1 4
#
#出力例 3
#0
#条件を満たす塗り方が存在しない場合もあります。  
#
#入力例 4
#20 0
#
#出力例 4
#3486784401
#答えは 32 ビット符号付き整数型に収まらないことがあります。  

def 