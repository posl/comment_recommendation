#問題文
#2N 個のボールがあります。各ボールには 1 以上 N 以下の整数によって表される色が塗られており、各色で塗られたボールはちょうど 2 個ずつ存在します。
#これらのボールが、底が地面と平行になるように置かれた M 本の筒に入れられています。はじめ、i  (1 ≦ i ≦ M) 本目の筒には k_i 個のボールが入っており、上から j  (1 ≦ j ≦ k_i) 番目のボールの色は a_{i, j} です。
#あなたの目標は、以下の操作を繰り返すことで M 本の筒全てを空にすることです。
#異なる 2 本の空でない筒を選び、それぞれの筒の一番上にあるボールを取り出して捨てる。ここで、取り出して捨てた 2 つのボールは同じ色で塗られている必要がある。
#目標が達成可能かを判定してください。
#
#制約
#1 ≦ N ≦ 2 × 10^5
#2 ≦ M ≦ 2 × 10^5
#1 ≦ k_i (1 ≦ i ≦ M)
#1 ≦ a_{i,j} ≦ N (1 ≦ i ≦ M,1 ≦ j ≦ k_i)
#sum_{i=1}^{M} k_i = 2N
#全ての x (1 ≦ x ≦ N) について、1 ≦ i ≦ M かつ 1 ≦ j ≦ k_i かつ a_{i,j}=x なる整数の組 (i,j) はちょうど 2 つ存在する
#入力は全て整数
#
#入力
#入力は以下の形式で標準入力から与えられる。
#N M
#k_1
#a_{1,1} a_{1,2} ... a_{1,k_1}
#k_2
#a_{2,1} a_{2,2} ... a_{2,k_2}
#.
#.
#.
#k_M
#a_{M,1} a_{M,2} ... a_{M,k_M}
#
#出力
#目標が達成可能なら Yes を、達成不可能なら No を出力せよ。
#
#入力例 1
#2 2
#2
#1 2
#2
#1 2
#
#出力例 1
#Yes
#以下のように操作を行えばよいです。
#1 つ目の筒と 2 つ目の筒を選び、それぞれの筒の一番上にあるボールを取り出して捨てる。捨てられるボールの色は共に 1 であり等しいので、この操作は有効である。
#1 つ目の筒と 2 つ目の筒を選び、それぞれの筒の一番上にあるボールを取り出して捨てる。捨てられるボールの色は共に 2 であり等しいので、この操作は有効である。
#
#入力例 2
#2 2
#2
#1 2
#2
#2 1
#
#出力例 2
#No
#そもそも一度も操作を行うことができないため、目標を達成する、すなわち M 本の筒全てを空にすることは不可能です。

def 