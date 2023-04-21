#問題文
#整数の多重集合 S があります。はじめ S は空です。
#Q 個のクエリが与えられるので順に処理してください。
#クエリは次の 3 種類のいずれかです。
#1 x : S に x を 1 個追加する。
#2 x c : S から x を min(c, (S に含まれる x の個数 )) 個削除する。
#3 : (S の最大値  )- (S の最小値 ) を出力する。このクエリを処理するとき、 S が空でないことが保証される。
#
#
#制約
#1 ≦ Q ≦ 2× 10^5
#0 ≦ x ≦ 10^9
#1 ≦ c ≦ Q
#3 のクエリを処理するとき、S は空でない。
#入力は全て整数
#
#入力
#入力は以下の形式で標準入力から与えられる。
#Q
#query_1
#.
#.
#.
#query_Q
#i 番目のクエリを表す query_i は以下の 3 種類のいずれかである。
#1 x
#2 x c
#3 
#
#出力
#3 のクエリに対する答えを順に改行区切りで出力せよ。
#
#入力例 1
#8
#1 3
#1 2
#3
#1 2
#1 7
#3
#2 2 3
#3
#
#出力例 1
#1
#5
#4
#多重集合 S は以下のように変化します。
#1 番目のクエリ : S に 3 を追加する。S は {3 } となる。
#2 番目のクエリ : S に 2 を追加する。S は {2, 3} となる。
#3 番目のクエリ : S = {2, 3} の最大値は 3 、最小値は 2 なので、 3-2=1 を出力する。
#4 番目のクエリ : S に 2 を追加する。S は {2,2,3 } となる。
#5 番目のクエリ : S に 7 を追加する。S は {2, 2,3, 7} となる。
#6 番目のクエリ : S = {2,2,3, 7} の最大値は 7 、最小値は 2 なので、 7-2=5 を出力する。
#7 番目のクエリ : S に含まれる 2 の個数は 2 個なので、 [min(2,3)] = 2 個の 2 を S から削除する。S は {3, 7} となる。
#8 番目のクエリ : S = {3, 7} の最大値は 7 、最小値は 3 なので、 7-3=4 を出力する。
#
#入力例 2
#4
#1 10000
#1 1000
#2 100 3
#1 10
#
#出力例 2
#クエリ 3 が含まれない場合、何も出力してはいけません。

def 