#問題文
#とある世界では、今日はクリスマスイブです。
#高羽氏の庭には N 本の木が植えられています。i 本目の木 (1 ≦ i ≦ N) の高さは h_i メートルです。
#彼は、これらの木のうち K 本を選んで電飾を施すことにしました。より美しい光景をつくるために、できるだけ近い高さの木を飾り付けたいです。
#より具体的には、飾り付ける木のうち最も高いものの高さを h_{max} メートル、最も低いものの高さを h_{min} メートルとすると、h_{max} - h_{min} が小さいほど好ましいです。h_{max} - h_{min} は最小でいくつにすることができるでしょうか？
#
#制約
#2 ≦ K < N ≦ 10^5
#1 ≦ h_i ≦ 10^9
#h_i は整数である。
#
#入力
#入力は以下の形式で標準入力から与えられる。
#N K
#h_1
#h_2
#:
#h_N
#
#出力
#h_{max} - h_{min} としてありうる最小の値を出力せよ。
#
#入力例 1
#5 3
#10
#15
#11
#14
#12
#
#出力例 1
#2
#1, 3, 5 本目の木を飾り付けると h_{max} = 12, h_{min} = 10 となり h_{max} - h_{min} = 2 で、これが最適です。
#
#入力例 2
#5 3
#5
#7
#5
#7
#7
#
#出力例 2
#0
#2, 4, 5 本目の木を飾り付けると h_{max} = 7, h_{min} = 7 となり h_{max} - h_{min} = 0 で、これが最適です。
#これらの入力例では木の数がそれほど多くありませんが、最大で 10 万本の木がある可能性に注意してください (ここに 10 万行の入力例を貼るわけにはいかないのです)。

def 