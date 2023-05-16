#問題文
#数列 (A_1,...,A_K) を使って、高橋君と青木君が石取りゲームをします。
#最初、山には N 個の石があります。高橋君から順に、二人が交互に次の操作を行います。
#現在山にある石の個数以下であるような A_i を 1 つ選ぶ。山から A_i 個の石を取り除く。
#山から石がなくなったとき、ゲームは終了します。
#二人がともに、ゲーム終了までに自分が取り除いた石の個数を最大化しようとするとき、高橋君は何個の石を取り除くことができますか？
#
#制約
#1 ≦ N ≦ 10^4
#1 ≦ K ≦ 100
#1 = A_1 < A_2 < ... < A_K ≦ N
#入力に含まれる値は全て整数である
#
#入力
#入力は以下の形式で標準入力から与えられる。
#N K
#A_1 A_2 ... A_K
#
#出力
#答えを出力せよ。  
#
#入力例 1
#10 2
#1 4
#
#出力例 1
#5
#ゲームの進行の一例は以下の通りです。
#高橋君が山から 4 個の石を取り除く。
#青木君が山から 4 個の石を取り除く。
#高橋君が山から 1 個の石を取り除く。
#青木君が山から 1 個の石を取り除く。
#この例では高橋君は 5 個の石を取り除くことができます。高橋君が 6 個以上の石を取り除くことはできないためこれが最大です。  
#高橋君は 5 個の石を取り除くことができるゲームの進行の例には、他にも次のようなものがあります。
#高橋君が山から 1 個の石を取り除く。
#青木君が山から 4 個の石を取り除く。
#高橋君が山から 4 個の石を取り除く。
#青木君が山から 1 個の石を取り除く。
#
#入力例 2
#11 4
#1 2 3 6
#
#出力例 2
#8
#ゲームの進行の一例は以下の通りです。
#高橋君が山から 6 個の石を取り除く。
#青木君が山から 3 個の石を取り除く。
#高橋君が山から 2 個の石を取り除く。
#この例では高橋君は 8 個の石を取り除くことができます。高橋君が 9 個以上の石を取り除くことはできないためこれが最大です。  
#
#入力例 3
#10000 10
#1 2 4 8 16 32 64 128 256 512
#
#出力例 3
#5136

def 