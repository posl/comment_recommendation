#問題文
#l が奇数のとき，l 個の数 a_1, a_2, ..., a_l の中央値とは，a_1, a_2, ..., a_l の中で ((l+1)/(2)) 番目に大きい値のことを言います．
#N 個の数 X_1, X_2, ..., X_N が与えられます．ここで，N は偶数です．
#i = 1, 2, ..., N に対して，X_1, X_2, ..., X_N から X_i のみを除いたもの，すなわち X_1, X_2, ..., X_{i-1}, X_{i+1}, ..., X_N の中央値を B_i とします．
#i = 1, 2, ..., N に対して，B_i を求めてください．
#
#制約
#2 ≦ N ≦ 200000
#N は偶数
#1 ≦ X_i ≦ 10^9
#入力はすべて整数
#
#入力
#入力は以下の形式で標準入力から与えられる。
#N
#X_1 X_2 ... X_N
#
#出力
#N 行出力せよ．
#i 行目には B_i を出力せよ．
#
#入力例 1
#4
#2 4 4 3
#
#出力例 1
#4
#3
#3
#4
#X_2, X_3, X_4 の中央値は 4 なので，B_1 = 4 です．
#X_1, X_3, X_4 の中央値は 3 なので，B_2 = 3 です．
#X_1, X_2, X_4 の中央値は 3 なので，B_3 = 3 です．
#X_1, X_2, X_3 の中央値は 4 なので，B_4 = 4 です．
#
#入力例 2
#2
#1 2
#
#出力例 2
#2
#1
#
#入力例 3
#6
#5 5 4 4 3 3
#
#出力例 3
#4
#4
#4
#4
#4
#4

def 