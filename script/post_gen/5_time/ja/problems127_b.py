#問題文
#ある池に生えている藻類は、以下のように成長します。
#西暦 i 年になる瞬間に生えている重さの合計を x_i グラムとすると、
#i≥2000 に対して、以下の式が成り立ちます:
#x_{i+1} = rx_i - D
#r, D, x_{2000} が与えられます。x_{2001}, ..., x_{2010} を計算し、順に出力してください。
#
#制約
#2 ≤ r ≤ 5
#1 ≤ D ≤ 100
#D < x_{2000} ≤ 200
#入力はすべて整数
#
#入力
#入力は以下の形式で標準入力から与えられる。
#r D x_{2000}
#
#出力
#10 行出力せよ。i 行目 (1 ≤ i ≤ 10) には x_{2000+i} を整数で出力せよ。
#
#入力例 1
#2 10 20
#
#出力例 1
#30
#50
#90
#170
#330
#650
#1290
#2570
#5130
#10250
#例えば、x_{2001} = rx_{2000} - D = 2 × 20 - 10 = 30 、 x_{2002} = rx_{2001} - D = 2 × 30 - 10 = 50 です。
#
#入力例 2
#4 40 60
#
#出力例 2
#200
#760
#3000
#11960
#47800
#191160
#764600
#3058360
#12233400
#48933560

def 