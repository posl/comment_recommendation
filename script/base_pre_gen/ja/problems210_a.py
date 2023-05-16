#問題文
#高橋君はキャベツ屋さんにやってきました。
#キャベツ屋さんでは、 キャベツを 1 個 X 円で買うことができます。
#ただし、キャベツを A 個よりも多く買う場合、A+1 個目以降に買うキャベツについては 1 個 Y 円で買うことができます。（ここで、Y < X が保証されます。）
#高橋君がキャベツを N 個買うために必要な金額を出力してください。
#
#制約
#1 ≦ N ≦ 10^5
#1 ≦ A ≦ 10^5
#1 ≦ Y < X ≦ 100
#入力はすべて整数
#
#入力
#入力は以下の形式で標準入力から与えられる。
#N A X Y
#
#出力
#高橋君が N 個のキャベツを買うために必要な金額を出力せよ。
#
#入力例 1
#5 3 20 15
#
#出力例 1
#90
#1 個目から 3 個目までのキャベツは、1 個 20 円で買うことができます。
#4 個目と 5 個目のキャベツは、1 個 15 円で買うことができます。
#よって、5 個のキャベツを買うために必要な金額は、20+20+20+15+15 = 90 円です。
#
#入力例 2
#10 10 100 1
#
#出力例 2
#1000

def 