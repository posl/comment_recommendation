#問題文
#非負整数 A,B,C,D,E,F があり、A× B× C≧ D× E× F をみたしています。
#(A× B× C)-(D× E× F) の値を 998244353 で割った余りを求めてください。
#
#制約
#0≦ A,B,C,D,E,F≦ 10^{18}
#A× B× C≧ D× E× F
#A,B,C,D,E,F は整数
#
#入力
#入力は以下の形式で標準入力から与えられる。
#A B C D E F
#
#出力
#(A× B× C)-(D× E× F) を 998244353 で割った余りを整数で出力せよ。  
#
#入力例 1
#2 3 5 1 2 4
#
#出力例 1
#22
#A× B× C=2× 3× 5=30, D× E× F=1× 2× 4=8 より、
#(A× B× C)-(D× E× F)=22 であり、これを 998244353 で割った余りである 22 を出力します。
#
#入力例 2
#1 1 1000000000 0 0 0
#
#出力例 2
#1755647
#A× B× C=1000000000, D× E× F=0 より、
#(A× B× C)-(D× E× F)=1000000000 であり、これを 998244353 で割った余りである 1755647 を出力します。
#
#入力例 3
#1000000000000000000 1000000000000000000 1000000000000000000 1000000000000000000 1000000000000000000 1000000000000000000
#
#出力例 3
#0
#(A× B× C)-(D× E× F)=0 であり、これを 998244353 で割った余りである 0 を出力します。

def 