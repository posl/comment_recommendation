#問題文
#文字列 S が与えられます。S のそれぞれの文字は英大文字または英小文字です。
#S が次の条件すべてを満たすか判定してください。
#S の先頭の文字は大文字の A である。
#S の先頭から 3 文字目と末尾から 2 文字目の間（両端含む）に大文字の C がちょうど 1 個含まれる。
#以上の A, C を除く S のすべての文字は小文字である。
#
#制約
#4 ≤ |S| ≤ 10 （|S| は文字列 S の長さ）
#S のそれぞれの文字は英大文字または英小文字である。
#
#入力
#入力は以下の形式で標準入力から与えられる。
#S
#
#出力
#S が問題文中の条件すべてを満たすなら AC、そうでなければ WA と出力せよ。
#
#入力例 1
#AtCoder
#
#出力例 1
#AC
#1 文字目が A、3 文字目が C でそれ以外の文字はすべて小文字であり、すべての条件を満たします。
#
#入力例 2
#ACoder
#
#出力例 2
#WA
#2 文字目が C であってはいけません。
#
#入力例 3
#AcycliC
#
#出力例 3
#WA
#最後の文字が C であってもいけません。
#
#入力例 4
#AtCoCo
#
#出力例 4
#WA
#C を 2 個以上含んではいけません。
#
#入力例 5
#Atcoder
#
#出力例 5
#WA
#C を 1 個も含まないのもいけません。

def 