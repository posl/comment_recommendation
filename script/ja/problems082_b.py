#問題文
#英小文字のみからなる文字列 s, t が与えられます。
#あなたは、s の文字を好きな順に並べ替え、文字列 s' を作ります。
#また、t の文字を好きな順に並べ替え、文字列 t' を作ります。
#このとき、辞書順で s' < t' となるようにできるか判定してください。
#
#注釈
#長さ N の文字列 a = a_1 a_2 ... a_N および長さ M の文字列 b = b_1 b_2 ... b_M について、辞書順で a < b であるとは、次の 2 つの条件のいずれかが成り立つことをいう;
#N < M かつ a_1 = b_1, a_2 = b_2, ..., a_N = b_N である。
#ある i (1 ≦ i ≦ N, M) が存在して、a_1 = b_1, a_2 = b_2, ..., a_{i - 1} = b_{i - 1} かつ a_i < b_i である。 ただし、文字どうしはアルファベット順で比較される。
#例えば、xy < xya であり、atcoder < atlas である。
#
#制約
#s, t の長さは 1 以上 100 以下である。
#s, t は英小文字のみからなる。
#
#入力
#入力は以下の形式で標準入力から与えられる。
#s
#t
#
#出力
#辞書順で s' < t' となるようにできるならば Yes を、できないならば No を出力せよ。
#
#入力例 1
#yx
#axy
#
#出力例 1
#Yes
#例えば、yx を xy と並べ替え、axy を yxa と並べ替えれば、xy < yxa となります。
#
#入力例 2
#ratcode
#atlas
#
#出力例 2
#Yes
#例えば、ratcode を acdeort と並べ替え、atlas を tslaa と並べ替えれば、acdeort < tslaa となります。
#
#入力例 3
#cd
#abc
#
#出力例 3
#No
#cd, abc をそれぞれどのように並べ替えても、目標を達成できません。
#
#入力例 4
#w
#ww
#
#出力例 4
#Yes
#
#入力例 5
#zzz
#zzz
#
#出力例 5
#No

def 