#問題文
#4 桁の暗証番号 X_1X_2X_3X_4 が与えられます。
#番号は先頭の桁が 0 であることもあり得ます。
#暗証番号は以下のいずれかの条件をみたすとき弱い暗証番号と呼ばれます。
#4 桁とも同じ数字である。
#1≦ i≦ 3 をみたす任意の整数 i について、 X_{i+1} が、 X_i の次の数字である。
#ただし、 0≦ j≦ 8 について j の次の数字は j+1 であり、 9 の次の数字は 0 である。 
#与えられた暗証番号が弱い暗証番号ならば Weak を、そうでないならば Strong を出力してください。
#
#制約
#0 ≦ X_1, X_2, X_3, X_4 ≦ 9
#X_1, X_2, X_3, X_4 は整数である。
#
#入力
#入力は以下の形式で標準入力から与えられる。
#X_1X_2X_3X_4
#
#出力
#与えられた暗証番号が弱い暗証番号ならば Weak を、そうでないならば Strong を出力せよ。
#
#入力例 1
#7777
#
#出力例 1
#Weak
#4 桁ともすべて 7 であるため、 1 つめの条件をみたしており、弱い暗証番号です。
#
#入力例 2
#0112
#
#出力例 2
#Strong
#1 桁目と 2 桁目が異なっており、 3 桁目は 2 桁目の次の数字ではないため、どちらの条件もみたしていません。
#
#入力例 3
#9012
#
#出力例 3
#Weak
#9 の次の数字が 0 であることに注意してください。

def 