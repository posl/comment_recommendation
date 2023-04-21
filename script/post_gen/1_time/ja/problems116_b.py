#問題文
#数列 a={a_1,a_2,a_3,......} は、以下のようにして定まります。
#初項 s は入力で与えられる。
#関数 f(n) を以下のように定める: n が偶数なら f(n) = n/2、n が奇数なら f(n) = 3n+1。
#i = 1 のとき a_i = s、i > 1 のとき a_i = f(a_{i-1}) である。
#このとき、次の条件を満たす最小の整数 m を求めてください。
#a_m = a_n (m > n) を満たす整数 n が存在する。
#
#制約
#1 ≦ s ≦ 100
#入力はすべて整数である。
#a のすべての要素、および条件を満たす最小の m は 1000000 以下となることが保証される。
#
#入力
#入力は以下の形式で標準入力から与えられます。
#s
#
#出力
#条件を満たす最小の整数 m を出力してください。
#
#入力例 1
#8
#
#出力例 1
#5
#a={8,4,2,1,4,2,1,4,2,1,......} です。a_5=a_2 なので、答えは 5 です。
#
#入力例 2
#7
#
#出力例 2
#18
#a={7,22,11,34,17,52,26,13,40,20,10,5,16,8,4,2,1,4,2,1,......} です。
#
#入力例 3
#54
#
#出力例 3
#114

def 