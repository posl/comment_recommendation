#問題文
#高橋君はあるプログラミングコンテストが行われているサイトに参加しています。 
#ここでは, コンテストに出場した時にこの順位に応じて「パフォーマンス」というものがつき、それによってレーティング (整数とは限らない) が次のように変化します。
#現在のレーティングを a とする。  
#次のコンテストで, パフォーマンス b を取ったとする。  
#そのとき, レーティングは a と b の平均まで変化する。  
#例えば, レーティングが 1 の人が次のコンテストでパフォーマンス 1000 を取ったら, レーティングは 1 と 1000 の平均である 500.5 になります。  
#高橋君は, 現在のレーティングが R で, 次のコンテストでレーティングをちょうど G にしたいと思っています。
#そのとき, 高橋君が取るべきパフォーマンスを求めなさい。  
#
#制約
#0 ≦ R, G ≦ 4500
#入力はすべて整数
#
#入力
#入力は以下の形式で標準入力から与えられる。  
#R
#G
#
#出力
#高橋君が取るべきパフォーマンスを出力しなさい。  
#
#入力例 1
#2002
#2017
#
#出力例 1
#2032
#高橋君の今のレーティングは 2002 です。
#次のコンテストでパフォーマンス 2032 を取ると、レーティングは 2002 と 2032 の平均である 2017 となり、目標を達成することができます。  
#
#入力例 2
#4500
#0
#
#出力例 2
#-4500
#現在のレーティングと目標のレーティングは 0 以上 4500 以下ですが、0 未満のパフォーマンスも取ることができます。  

def 