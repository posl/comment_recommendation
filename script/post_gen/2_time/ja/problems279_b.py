#問題文
#英小文字からなる文字列 S,T が与えられるので、 T が S の(連続する)部分文字列かどうか判定してください。
#なお、文字列 X に以下の操作を 0 回以上施して文字列 Y が得られる時、またその時に限り Y は X の(連続する)部分文字列であると言います。
#以下の 2 つの操作から 1 つを選択して、その操作を行う。
#X の先頭の 1 文字を削除する。
#X の末尾の 1 文字を削除する。
#
#例えば tag は voltage の(連続する)部分文字列ですが、 ace は atcoder の(連続する)部分文字列ではありません。
#
#制約
#S,T は英小文字からなる
#1 ≦ |S|,|T| ≦ 100 ( |X| は文字列 X の長さ )
#
#入力
#入力は以下の形式で標準入力から与えられる。
#S
#T
#
#出力
#T が S の(連続する)部分文字列なら Yes 、そうでないなら No と出力せよ。
#
#入力例 1
#voltage
#tag
#
#出力例 1
#Yes
#tag は voltage の(連続する)部分文字列です。
#
#入力例 2
#atcoder
#ace
#
#出力例 2
#No
#ace は atcoder の(連続する)部分文字列ではありません。
#
#入力例 3
#gorilla
#gorillagorillagorilla
#
#出力例 3
#No
#
#入力例 4
#toyotasystems
#toyotasystems
#
#出力例 4
#Yes
#S=T である場合もあります。

def 