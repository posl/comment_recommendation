#問題文
#英小文字からなる文字列 S が与えられます。 
#S の先頭に a をいくつか（ 0 個でも良い）つけ加えて回文にすることができるか判定してください。 
#ただし、長さ N の文字列 A=A_1A_2... A_N が回文であるとは、すべての 1≦ i≦ N について A_i=A_{N+1-i} が成り立っていることをいいます。
#
#制約
#1 ≦ | S | ≦ 10^6
#S は英小文字のみからなる。
#
#入力
#入力は以下の形式で標準入力から与えられる。
#S
#
#出力
#S の先頭に a をいくつかつけ加えて回文にすることができるならば Yes を、そうでないならば No を出力せよ。
#
#入力例 1
#kasaka
#
#出力例 1
#Yes
#kasaka の先頭に a を 1 つ付け加えることによって、akasaka となり回文となるため Yes を出力します。
#
#入力例 2
#atcoder
#
#出力例 2
#No
#atcoder の先頭に a をいくつ付け加えても回文となる事はありません。
#
#入力例 3
#php
#
#出力例 3
#Yes
#php はそれ自体回文です。S の先頭に付け加える a は 0 個でも許されるため、Yes を出力します。

def 