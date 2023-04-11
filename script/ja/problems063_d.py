#問題文
#あなたが散歩していると、突然 N 体の魔物が出現しました。それぞれの魔物は 体力 という値を持ち、i 体目の魔物の出現時の体力は h_i です。体力が 0 以下となった魔物は直ちに消滅します。
#幸い、あなたは熟練の魔法使いであり、爆発を引き起こして魔物を攻撃できます。一回の爆発では、以下のように魔物の体力を減らすことができます。
#生存している魔物を一体選び、その魔物を中心に爆発を引き起こす。爆発の中心となる魔物の体力は A 減り、その他の魔物の体力はそれぞれ B 減る。ここで、A と B はあらかじめ定まった値であり、A > B である。
#すべての魔物を消し去るためには、最小で何回の爆発を引き起こす必要があるでしょうか？
#
#制約
#入力値はすべて整数である。
#1 ≤ N ≤ 10^5
#1 ≤ B < A ≤ 10^9
#1 ≤ h_i ≤ 10^9
#
#入力
#入力は以下の形式で標準入力から与えられる。
#N A B
#h_1
#h_2
#:
#h_N
#
#出力
#すべての魔物を消し去るために必要な最小の爆発の回数を出力せよ。
#
#入力例 1
#4 5 3
#8
#7
#4
#2
#
#出力例 1
#2
#以下のようにして、2 回の爆発ですべての魔物を消し去ることができます。
#まず、体力が 8 の魔物を中心に爆発を引き起こす。4 体の魔物の体力はそれぞれ 3, 4, 1, -1 となり、最後の魔物は消滅する。
#次に、残りの体力が 4 の魔物を中心に爆発を引き起こす。残っていた 3 体の魔物の体力はそれぞれ 0, -1, -2 となり、すべての魔物が消滅する。
#
#入力例 2
#2 10 4
#20
#20
#
#出力例 2
#4
#それぞれの魔物を中心に 2 回ずつ、合計で 4 回の爆発を引き起こす必要があります。
#
#入力例 3
#5 2 1
#900000000
#900000000
#1000000000
#1000000000
#1000000000
#
#出力例 3
#800000000

def 