#問題文
#正の整数 X が以下の条件を満たすとき、 X はルンルン数であると言います。  
#X を(leading zeroなしで)十進数表記した際に、隣り合うどの 2 つの桁の値についても、差の絶対値が 1 以下
#例えば、 1234 , 1 , 334 などはルンルン数ですが、 31415 , 119 , 13579 などはルンルン数ではありません。  
#正の整数 K が与えられます。小さい方から K 番目のルンルン数を求めてください。
#
#制約
#1 ≦ K ≦ 10^5
#入力はすべて整数である。
#
#入力
#入力は以下の形式で標準入力から与えられる。  
#K
#
#出力
#答えを出力せよ。
#
#入力例 1
#15
#
#出力例 1
#23
#小さい方から 15 番目までのルンルン数を順に並べると、
#1,
#2,
#3,
#4,
#5,
#6,
#7,
#8,
#9,
#10,
#11,
#12,
#21,
#22,
#23
#ですので、答えは 23 です。
#
#入力例 2
#1
#
#出力例 2
#1
#
#入力例 3
#13
#
#出力例 3
#21
#
#入力例 4
#100000
#
#出力例 4
#3234566667
#答えが 32 ビット符号付き整数の範囲に収まらない可能性があるので注意してください。

def 