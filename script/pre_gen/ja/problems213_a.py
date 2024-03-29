#問題文
#0 以上 255 以下の整数 A,B が与えられます。 A  xor C=B となる 0 以上の整数 C を求めてください。
#なお、そのような C はただ 1 つ存在し、0 以上 255 以下であることが証明されます。
# xor  とは
#整数 a, b のビットごとの排他的論理和 a  xor  b は、以下のように定義されます。
# a  xor  b を二進表記した際の 2^k (k ≧ 0) の位の数は、a, b を二進表記した際の 2^k の位の数のうち一方のみが 1 であれば 1、そうでなければ 0 である。
#例えば、3  xor  5 = 6 となります (二進表記すると: 011  xor  101 = 110)。
#
#
#制約
#0≦ A,B ≦ 255
#入力に含まれる値は全て整数である
#
#入力
#入力は以下の形式で標準入力から与えられる。
#A B
#
#出力
#答えを出力せよ。  
#
#入力例 1
#3 6
#
#出力例 1
#5
#3 は 二進表記で 11、5 は二進表記で 101 なので、これらの xor は二進表記で 110 であり、十進表記で 6 です。
#このように、3  xor  5 = 6 となるので、答えは 5 です。
#
#入力例 2
#10 12
#
#出力例 2
#6

def 