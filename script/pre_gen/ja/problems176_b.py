#問題文
#整数 N が 9 の倍数であることと、N を十進法で表したときの各桁の数の和が 9 の倍数であることは同値です。
#N が 9 の倍数であるか判定してください。
#
#制約
#0 ≦ N < 10^{200000}
#N は整数
#
#入力
#入力は以下の形式で標準入力から与えられる。
#N
#
#出力
#N が 9 の倍数ならば Yes、そうでないなら No を出力せよ。
#
#入力例 1
#123456789
#
#出力例 1
#Yes
#各桁の数の和は 1+2+3+4+5+6+7+8+9=45 であり、45 は 9 の倍数なので、123456789 は 9 の倍数です。
#
#入力例 2
#0
#
#出力例 2
#Yes
#
#入力例 3
#31415926535897932384626433832795028841971693993751058209749445923078164062862089986280
#
#出力例 3
#No

def 