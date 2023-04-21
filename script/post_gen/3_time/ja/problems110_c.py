#問題文
#英小文字のみからなる文字列 S, T が与えられます。
#文字列 S に対して、次の操作を何度でも行うことができます。
#操作: 2つの異なる英小文字 c_1, c_2 を選び、S に含まれる全ての c_1 を c_2 に、c_2 を c_1 に置き換える
#0 回以上操作を行って、S を T に一致させられるか判定してください。
#
#制約
#1 ≦ |S| ≦ 2 × 10^5
#|S| = |T|
#S, T は英小文字のみからなる
#
#入力
#入力は以下の形式で標準入力から与えられる。
#S
#T
#
#出力
#S を T に一致させられる場合は Yes、そうでない場合は No を出力せよ。
#
#入力例 1
#azzel
#apple
#
#出力例 1
#Yes
#次のように操作を行えば、azzel を apple にできます。
#c_1 として e を、c_2 として l を選ぶと、azzel が azzle になる
#c_1 として z を、c_2 として p を選ぶと、azzle が apple になる
#
#入力例 2
#chokudai
#redcoder
#
#出力例 2
#No
#どのように操作を行っても chokudai を redcoder にできません。
#
#入力例 3
#abcdefghijklmnopqrstuvwxyz
#ibyhqfrekavclxjstdwgpzmonu
#
#出力例 3
#Yes

def 