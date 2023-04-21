#問題文
#N 人の人がいます。i  (1 ≦ i ≦ N) 人目の人の姓は S_i、名は T_i です。
#同姓同名であるような人の組が存在するか、すなわち 1 ≦ i < j ≦ N かつ S_i=S_j かつ T_i=T_j を満たすような整数対 (i,j) が存在するか判定してください。
#
#制約
#2 ≦ N ≦ 1000
#N は整数
#S_i,T_i は英小文字のみからなる長さ 1 以上 10 以下の文字列
#
#入力
#入力は以下の形式で標準入力から与えられる。
#N
#S_1 T_1
#S_2 T_2
#.
#.
#.
#S_N T_N
#
#出力
#同姓同名であるような人の組が存在するなら Yes を、存在しないなら No を出力せよ。
#
#入力例 1
#3
#tanaka taro
#sato hanako
#tanaka taro
#
#出力例 1
#Yes
#1 人目の人と 3 人目の人が同姓同名です。
#
#入力例 2
#3
#saito ichiro
#saito jiro
#saito saburo
#
#出力例 2
#No
#同姓同名であるような人の組は存在しません。
#
#入力例 3
#4
#sypdgidop bkseq
#bajsqz hh
#ozjekw mcybmtt
#qfeysvw dbo
#
#出力例 3
#No

def 