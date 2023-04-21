#問題文
#長さ 2N の文字列 S があります。
#この文字列に対して Q 個のクエリが与えられます。i 番目のクエリでは 3 つの整数 T_i, A_i, B_i が与えられるので、以下の処理をします。  
#T_i = 1 のとき : S の A_i 文字目と B_i 文字目を入れ替える
#T_i = 2 のとき : S の前半 N 文字と後半 N 文字を入れ替える(A_i, B_i の値は用いない)
#    例えば S が FLIP のときにこのクエリを処理すると、S は IPFL となる。
#これら Q 個のクエリを与えられた順に全て処理した後の S を出力してください。  
#
#制約
#1 ≦ N ≦ 2 × 10^5
#S は長さ 2N の英大文字のみからなる文字列
#1 ≦ Q ≦ 3 × 10^5
#T_i は 1 または 2
#T_i = 1 のとき、1 ≦ A_i < B_i ≦ 2N
#T_i = 2 のとき、A_i = B_i = 0
#
#入力
#入力は以下の形式で標準入力から与えられる。
#N
#S
#Q
#T_1 A_1 B_1
#T_2 A_2 B_2
#T_3 A_3 B_3
#.
#.
#.
#T_Q A_Q B_Q
#
#出力
#クエリ処理後の S を出力せよ。  
#
#入力例 1
#2
#FLIP
#2
#2 0 0
#1 1 4
#
#出力例 1
#LPFI
#1 番目のクエリでは S の前半 N 文字と後半 N 文字を入れ替えるため、S は IPFL となります。
#2 番目のクエリでは S の 1 文字目と 4 文字目を入れ替えるため、S は LPFI となります。  
#
#入力例 2
#2
#FLIP
#6
#1 1 3
#2 0 0
#1 1 2
#1 2 3
#2 0 0
#1 1 4
#
#出力例 2
#ILPF

def 