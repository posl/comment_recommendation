#問題文
#高橋君はプロのパティシエになり, AtCoder Beginner Contest 100 を記念して, 「ABC洋菓子店」というお店を開いた.  
#ABC洋菓子店では, N 種類のケーキを売っている.
#各種類のケーキには「綺麗さ」「おいしさ」「人気度」の 3 つの値を持ち, i 種類目のケーキの綺麗さは x_i, おいしさは y_i, 人気度は z_i である.
#これらの値は 0 以下である可能性もある.  
#りんごさんは, ABC洋菓子店で M 個のケーキを食べることにした. 彼は次のように, 食べるケーキの組み合わせを選ぶことにした.  
#同じ種類のケーキを 2 個以上食べない.
#上の条件を満たしつつ, (綺麗さの合計の絶対値) + (おいしさの合計の絶対値) + (人気度の合計の絶対値) が最大になるように選ぶ.
#このとき, りんごさんが選ぶケーキの (綺麗さの合計の絶対値) + (おいしさの合計の絶対値) + (人気度の合計の絶対値) の最大値を求めなさい.  
#
#制約
#N は 1 以上 1  000 以下の整数
#M は 0 以上 N 以下の整数
#x_i, y_i, z_i  (1 ≦ i ≦ N) は, それぞれ -10  000  000  000 以上 10  000  000  000 以下の整数.
#
#入力
#入力は以下の形式で標準入力から与えられる.  
#N M
#x_1 y_1 z_1
#x_2 y_2 z_2
# :  :
#x_N y_N z_N
#
#出力
#りんごさんが選ぶケーキの (綺麗さの合計の絶対値) + (おいしさの合計の絶対値) + (人気度の合計の絶対値) の最大値を出力しなさい.  
#
#入力例 1
#5 3
#3 1 4
#1 5 9
#2 6 5
#3 5 8
#9 7 9
#
#出力例 1
#56
#2, 4, 5 種類目のケーキを食べることを考える. そのとき, 「綺麗さ」「おいしさ」「人気度」の合計はそれぞれ次のようになる.  
#綺麗さ：1 + 3 + 9 = 13
#おいしさ：5 + 5 + 7 = 17
#人気度：9 + 8 + 9 = 26
#このときの (綺麗さの合計の絶対値) + (おいしさの合計の絶対値) + (人気度の合計の絶対値) は 13 + 17 + 26 = 56 となり, これが最大になる.  
#
#入力例 2
#5 3
#1 -2 3
#-4 5 -6
#7 -8 -9
#-10 11 -12
#13 -14 15
#
#出力例 2
#54
#1, 3, 5 種類目のケーキを食べることを考える. そのとき, 「綺麗さ」「おいしさ」「人気度」の合計はそれぞれ次のようになる.  
#綺麗さ：1 + 7 + 13 = 21
#おいしさ：(-2) + (-8) + (-14) = -24
#人気度：3 + (-9) + 15 = 9
#このときの (綺麗さの合計の絶対値) + (おいしさの合計の絶対値) + (人気度の合計の絶対値) は 21 + 24 + 9 = 54 となり, これが最大になる.  
#
#入力例 3
#10 5
#10 -80 21
#23 8 38
#-94 28 11
#-26 -2 18
#-69 72 79
#-26 -86 -54
#-72 -50 59
#21 65 -32
#40 -94 87
#-62 18 82
#
#出力例 3
#638
#3, 4, 5, 7, 10 種類目のケーキを食べると, 綺麗さの合計は -323, おいしさの合計は 66, 人気度の合計は 249 となる.
#このときの (綺麗さの合計の絶対値) + (おいしさの合計の絶対値) + (人気度の合計の絶対値) は 323 + 66 + 249 = 638 となり, これが最大になる.  
#
#入力例 4
#3 2
#2000000000 -9000000000 4000000000
#7000000000 -5000000000 3000000000
#6000000000 -1000000000 8000000000
#
#出力例 4
#30000000000
#ケーキの綺麗さ, おいしさ, 人気度や出力
#すべき値が, 32bit 整数に収まらない場合もある.  

def 