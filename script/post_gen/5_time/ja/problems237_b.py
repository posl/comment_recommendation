#問題文
#H 行 W 列の行列 A が与えられます。
#A の上から i 行目、左から j 列目の要素は A_{i,j} です。   
#ここで、W 行 H 列の行列 B を、上から i 行目、左から j 列目の要素が A_{j,i} と一致するような行列として定めます。
#すなわち、B は A の転置行列です。  
#B を出力してください。
#
#制約
#1≦ H,W ≦ 10^5
#H × W ≦ 10^5
#1 ≦ A_{i,j} ≦ 10^9
#入力は全て整数である
#
#入力
#入力は以下の形式で標準入力から与えられる。
#H W
#A_{1,1} A_{1,2} ... A_{1,W}
#A_{2,1} A_{2,2} ... A_{2,W}
#.
#.
#.
#A_{H,1} A_{H,2} ... A_{H,W}
#
#出力
#B を以下の形式で出力せよ。  
#B_{1,1} B_{1,2} ... B_{1,H}
#B_{2,1} B_{2,2} ... B_{2,H}
#.
#.
#.
#B_{W,1} B_{W,2} ... B_{W,H}
#
#入力例 1
#4 3
#1 2 3
#4 5 6
#7 8 9
#10 11 12
#
#出力例 1
#1 4 7 10
#2 5 8 11
#3 6 9 12
#たとえば A_{2,1}=4 なので、転置行列 B の上から 1 行目、左から 2 列目の要素は 4 になります。  
#
#入力例 2
#2 2
#1000000000 1000000000
#1000000000 1000000000
#
#出力例 2
#1000000000 1000000000
#1000000000 1000000000

def 