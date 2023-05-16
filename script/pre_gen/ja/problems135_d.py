#問題文
#文字列 S が与えられます。S の各文字は、数字 (0 ～ 9) か ? です。
#? を数字に置き換えてできる整数のうち、13 で割って 5 あまる数は何通りあるでしょうか？ただし、頭文字が 0 である場合も整数とみなすものとします。
#答えは非常に大きくなる可能性があるため、10^9+7 で割ったあまりを答えてください。
#
#制約
#S は数字 (0 ～ 9) と ? からなる文字列。
#1 ≦ |S| ≦ 10^5
#
#入力
#入力は以下の形式で標準入力から与えられます。
#S
#
#出力
#条件を満たす整数の個数を 10^9+7 で割ったあまりを出力してください。
#
#入力例 1
#??2??5
#
#出力例 1
#768
#たとえば 482305, 002865, 972665 などが条件を満たします。
#
#入力例 2
#?44
#
#出力例 2
#1
#044 のみが条件を満たします。
#
#入力例 3
#7?4
#
#出力例 3
#0
#条件を満たす整数を作ることが不可能な場合もあります。
#
#入力例 4
#?6?42???8??2??06243????9??3???7258??5??7???????774????4?1??17???9?5?70???76???
#
#出力例 4
#153716888

def 