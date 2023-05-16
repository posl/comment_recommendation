#問題文
#xy 平面上に N 人の人 1,2,...,N がおり、人 i は座標 (X_i,Y_i) にいます。
#このうち、 K 人の人 A_1,A_2,...,A_K に同じ強さの明かりを持たせます。
#座標 (x,y) にいる人が強さ R の明かりを持っている時、その明かりによって中心 (x,y) 、半径 R の円の内部全体(境界を含む)が照らされます。
#すべての人が少なくとも 1 つの明かりによって照らされるために必要な明かりの強さの最小値を求めてください。
#
#制約
#入力は全て整数
#1 ≦ K < N ≦ 1000
#1 ≦ A_1 < A_2 < ... < A_K ≦ N
#|X_i|,|Y_i| ≦ 10^5
#i ≠ j ならば (X_i,Y_i) ≠ (X_j,Y_j)
#
#入力
#入力は以下の形式で標準入力から与えられる。
#N K
#A_1 A_2 ... A_K
#X_1 Y_1
#X_2 Y_2
#.
#.
#.
#X_N Y_N
#
#出力
#答えを実数として出力せよ。
#出力された解と想定解との絶対誤差または相対誤差が 10^{-5} 以下であるならば、出力は正しいと見なされる。
#
#入力例 1
#4 2
#2 3
#0 0
#0 1
#1 2
#2 0
#
#出力例 1
#2.23606797749978969
#この入力では人が 4 人おり、そのうち人 2,3 が明かりを持ちます。
#R ≧ (5)^(1/2) ≈ 2.236068 である時、すべての人が少なくとも 1 つの明かりによって照らされます。
#
#入力例 2
#2 1
#2
#-100000 -100000
#100000 100000
#
#出力例 2
#282842.712474619009
#
#入力例 3
#8 3
#2 6 8
#-17683 17993
#93038 47074
#58079 -57520
#-41515 -89802
#-72739 68805
#24324 -73073
#71049 72103
#47863 19268
#
#出力例 3
#130379.280458974768

def 