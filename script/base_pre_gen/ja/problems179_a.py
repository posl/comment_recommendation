#問題文
#AtCoder 王国では、英小文字を用いる高橋語という言語が使われています。
#高橋語では、名詞の複数形は次のルールで綴られます。
#単数形の末尾が s 以外なら、単数形の末尾に s をつける
#単数形の末尾が s なら、単数形の末尾に es をつける
#高橋語の名詞の単数形 S が与えられるので、複数形を出力してください。
#
#制約
#S は長さ 1 以上 1000 以下の文字列
#S は英小文字のみを含む
#
#入力
#入力は以下の形式で標準入力から与えられる。
#S
#
#出力
#与えられた高橋語の複数形を出力せよ。
#
#入力例 1
#apple
#
#出力例 1
#apples
#apple の末尾は e なので、複数形は apples になります。
#
#入力例 2
#bus
#
#出力例 2
#buses
#bus の末尾は s なので、複数形は buses になります。
#
#入力例 3
#box
#
#出力例 3
#boxs

def 