#問題文
#長さ N の数列 A=(A_0,...,A_{N-1}) があります。
#次の条件を全て満たす整数の組 (x,y,z,w) が存在するか判定してください。
#0 ≦ x < y < z < w ≦ N
#A_x + A_{x+1} + ... + A_{y-1} = P
#A_y + A_{y+1} + ... + A_{z-1} = Q
#A_z + A_{z+1} + ... + A_{w-1} = R
#
#制約
#3 ≦ N ≦ 2× 10^5
#1 ≦ A_i ≦ 10^9
#1 ≦ P,Q,R ≦ 10^{15}
#入力に含まれる値は全て整数である
#
#入力
#入力は以下の形式で標準入力から与えられる。
#N P Q R
#A_0 A_1 ... A_{N-1}
#
#出力
#条件を満たす組が存在するなら Yes、存在しないなら No を出力せよ。  
#
#入力例 1
#10 5 7 5
#1 3 2 2 2 3 1 4 3 2
#
#出力例 1
#Yes
#(x,y,z,w)=(1,3,6,8) が条件を満たします。
#
#入力例 2
#9 100 101 100
#31 41 59 26 53 58 97 93 23
#
#出力例 2
#No
#
#入力例 3
#7 1 1 1
#1 1 1 1 1 1 1
#
#出力例 3
#Yes

def 