#問題文
#N+M 個のボールがあります。各ボールには整数が 1 つ書かれています。
#これらのボールに書かれている数について、  
#N 個のボールに書かれている数は偶数
#M 個のボールに書かれている数は奇数
#であることがわかっています。  
#これらの N+M 個のボールの中から 2 つ選んで、書かれた数の和が偶数になる方法の数を求めてください。選ぶ順序は考慮しません。  
#なお、この方法の数はボールに書かれている整数の実際の値によらないことが示せます。  
#
#制約
#0 ≦ N,M ≦ 100
#2 ≦ N+M
#入力はすべて整数である。
#
#入力
#入力は以下の形式で標準入力から与えられる。  
#N M
#
#出力
#答えを出力せよ。
#
#入力例 1
#2 1
#
#出力例 1
#1
#例えば 3 つのボールに書かれている数がそれぞれ 1,2,4 であるとすると、  
#1 が書かれたボールと 2 が書かれたボールを選ぶと、和は奇数
#1 が書かれたボールと 4 が書かれたボールを選ぶと、和は奇数
#2 が書かれたボールと 4 が書かれたボールを選ぶと、和は偶数
#であるので、答えは 1 です。
#
#入力例 2
#4 3
#
#出力例 2
#9
#
#入力例 3
#1 1
#
#出力例 3
#0
#
#入力例 4
#13 3
#
#出力例 4
#81
#
#入力例 5
#0 3
#
#出力例 5
#3

def 