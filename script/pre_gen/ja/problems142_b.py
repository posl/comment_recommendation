#問題文
#高橋君の仲間たちは N 人で遊園地に遊びにいきました。
#遊園地の一番人気のジェットコースターに乗るためには、身長が K cm以上必要です。
#高橋君の i 番目の仲間の身長は h_i cm です。
#高橋君の仲間たちのうち、一番人気のジェットコースターに乗ることができる人の数を求めてください。
#
#制約
# 1 ≦ N ≦ 10^5 
# 1 ≦ K ≦ 500 
# 1 ≦ h_i ≦ 500
#入力はすべて整数
#
#入力
#入力は以下の形式で標準入力から与えられる。
#N K
#h_1 h_2 ... h_N
#
#出力
#高橋君の仲間たちのうち、一番人気のジェットコースターに乗ることのできる人の数を出力してください。
#
#入力例 1
#4 150
#150 140 100 200
#
#出力例 1
#2
#一番人気のジェットコースターに乗ることができるのは、1 番目の仲間と 4 番目の仲間の 2 人です。
#
#入力例 2
#1 500
#499
#
#出力例 2
#0
#
#入力例 3
#5 1
#100 200 300 400 500
#
#出力例 3
#5

def 