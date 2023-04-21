#問題文
#高橋君が 3 つのサイコロを振ったところそれぞれ a,b,c の目が出ました。
#a,b,c のうちある 2 つが同じときは残りの 1 つのサイコロの目を、同じものがないときは 0 を出力してください。
#
#制約
#1 ≦ a,b,c ≦ 6
#a,b,c は全て整数である。
#
#入力
#入力は以下の形式で標準入力から与えられる。
#a b c
#
#出力
#a,b,c のうちある 2 つが同じときは残りの 1 つのサイコロの目を、同じものがないときは 0 を出力せよ。
#
#入力例 1
#2 5 2
#
#出力例 1
#5
#1 つめと 3 つめのサイコロの目がともに 2 であるので、残り 1 つの目である 5 を出力します。
#
#入力例 2
#4 5 6
#
#出力例 2
#0
#サイコロの目はどの 2 つも相異なるため 0 を出力します。
#
#入力例 3
#1 1 1
#
#出力例 3
#1
#どの 2 つのサイコロの目も同じであり、そのいずれを選んだ場合でも残り 1 つの目は 1 となります。

def 