#問題文
#Atcoder国では、郵便番号は A+B+1 文字からなり、A+1 文字目はハイフン -、それ以外の全ての文字は 0 以上 9 以下の数字です。
#文字列 S が与えられるので、Atcoder国の郵便番号の形式を満たすかどうか判定してください。
#
#制約
#1≦A,B≦5
#|S|=A+B+1
#S は 0 以上 9 以下の数字、およびハイフン - からなる
#
#入力
#入力は以下の形式で標準入力から与えられる。
#A B
#S
#
#出力
#S がAtcoder国の郵便番号の形式を満たすならば Yes 、そうでなければ No を出力せよ。
#
#入力例 1
#3 4
#269-6650
#
#出力例 1
#Yes
#S の A+1 文字目がハイフンで、それ以外の全ての文字が 0 以上 9 以下の数字なので、Atcoder国の郵便番号の形式を満たしています。
#
#入力例 2
#1 1
#---
#
#出力例 2
#No
#S の A+1 文字目以外もハイフンとなっており、Atcoder国の郵便番号の形式を満たしていません。
#
#入力例 3
#1 2
#7444
#
#出力例 3
#No

def 