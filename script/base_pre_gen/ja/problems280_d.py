#問題文
#2 以上の整数 K が与えられます。
#正の整数 N であって、N! が K の倍数となるようなもののうち最小のものを求めてください。
#ただし、N! は N の階乗を表し、問題の制約下で、そのような N が必ず存在することが証明できます。
#
#制約
#2≦ K≦ 10^{12}
#K は整数
#
#入力
#入力は以下の形式で標準入力から与えられる。
#K
#
#出力
#N! が K の倍数となるような最小の正整数 N を出力せよ。  
#
#入力例 1
#30
#
#出力例 1
#5
#1!=1
#2!=2× 1=2
#3!=3× 2× 1=6
#4!=4× 3× 2× 1=24
#5!=5× 4× 3× 2× 1=120
#より、N! が 30 の倍数となる最小の正整数 N は 5 です。よって、5 を出力します。
#
#入力例 2
#123456789011
#
#出力例 2
#123456789011
#
#入力例 3
#280
#
#出力例 3
#7

def 