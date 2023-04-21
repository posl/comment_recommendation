#問題文
#ボールが N 個あり、 i 番目のボールには整数 A_i が書かれています。
#k=1,2,...,N に対して以下の問題を解いて、答えをそれぞれ出力してください。  
#k 番目のボールを除いた N-1 個のボールから、書かれている整数が等しいような異なる 2 つのボールを選び出す方法の数を求めてください。選ぶ順序は考慮しません。
#
#制約
#3 ≦ N ≦ 2 × 10^5
#1 ≦ A_i ≦ N
#入力はすべて整数である。
#
#入力
#入力は以下の形式で標準入力から与えられる。  
#N
#A_1 A_2 ... A_N
#
#出力
#k=1,2,...,N に対する答えを順番に一行ずつ出力せよ。
#
#入力例 1
#5
#1 1 2 1 2
#
#出力例 1
#2
#2
#3
#2
#3
#例えば k=1 のとき、残りのボールに書かれている数はそれぞれ {1,2,1,2} です。
#この中から書かれている数が等しいような異なる 2 つのボールを選び出す方法は 2 通りあります。
#したがって、 k=1 に対する問題の答えは 2 です。
#
#入力例 2
#4
#1 2 3 4
#
#出力例 2
#0
#0
#0
#0
#どの 2 つのボールを選び出しても、書かれている数は等しくありません。
#
#入力例 3
#5
#3 3 3 3 3
#
#出力例 3
#6
#6
#6
#6
#6
#どの 2 つのボールを選び出しても、書かれている数が等しいです。
#
#入力例 4
#8
#1 2 1 4 2 1 4 1
#
#出力例 4
#5
#7
#5
#7
#7
#5
#7
#5

def 