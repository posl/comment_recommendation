#問題文
#長さ N の整数列 A=(A_1,A_2,...,A_N) が与えられます。
#あなたは以下の連続する操作をちょうど一度だけ行います。
#整数 x (0≦ x ≦ N) を選ぶ。x として 0 を選んだ場合何もしない。 x として 1 以上の整数を選んだ場合、A_1,A_2,...,A_x をそれぞれ L で置き換える。
#整数 y (0≦ y ≦ N) を選ぶ。y として 0 を選んだ場合何もしない。 y として 1 以上の整数を選んだ場合、A_{N},A_{N-1},...,A_{N-y+1} をそれぞれ R で置き換える。
#操作後の A の要素の総和として考えられる最小値を求めてください。
#
#制約
#1 ≦ N ≦ 2× 10^5
#-10^9 ≦ L, R≦ 10^9
#-10^9 ≦ A_i≦ 10^9
#入力は全て整数
#
#入力
#入力は以下の形式で標準入力から与えられる。
#N L R
#A_1 A_2 ... A_N
#
#出力
#答えを出力せよ。
#
#入力例 1
#5 4 3
#5 5 0 6 3
#
#出力例 1
#14
#x=2,y=2 として操作をすると、数列 A = (4,4,0,3,3) となり、要素の総和は 14 になります。
#これが達成可能な最小値です。
#
#入力例 2
#4 10 10
#1 2 3 4
#
#出力例 2
#10
#x=0,y=0 として操作をすると、数列 A = (1,2,3,4) となり、要素の総和は 10 になります。
#これが達成可能な最小値です。
#
#入力例 3
#10 -5 -3
#9 -6 10 -1 2 10 -1 7 -15 5
#
#出力例 3
#-58
#L,R,A_i は負であることがあります。

def 