#問題文
#同じ文字列を 2 つ並べてできる文字列のことを偶文字列と呼ぶことにします。
#例えば、 xyzxyz や aaaaaa は偶文字列ですが、ababab や xyzxy は偶文字列ではありません。
#アルファベットの小文字からなる偶文字列 S が与えられます。
# S の末尾の文字を 1 文字以上消して作れる偶文字列のうち、最も長い偶文字列の長さを求めて下さい。
#与えられる入力では、条件を満たす 1 文字以上の文字列が存在することが保証されています。
#
#制約
#2 ≦ |S| ≦ 200
#S は小文字のアルファベットのみからなる偶文字列である。
#S に対して、条件を満たす 1 文字以上の文字列が存在する。
#
#入力
#入力は以下の形式で標準入力から与えられる。
#S
#
#出力
#答えとなる文字列の長さを出力せよ。
#
#入力例 1
#abaababaab
#
#出力例 1
#6
#abaababaab は偶文字列ですが、 1 文字も消していないので条件を満たしません。
#abaababaa は偶文字列ではありません。
#abaababa は偶文字列ではありません。
#abaabab は偶文字列ではありません。
#abaaba は偶文字列です。よって、答えは abaaba の長さである 6 です。
#
#入力例 2
#xxxx
#
#出力例 2
#2
#xxx は偶文字列ではありません。
#xx は偶文字列です。
#
#入力例 3
#abcabcabcabc
#
#出力例 3
#6
#条件を満たす文字列は abcabc なので、答えは 6 です。
#
#入力例 4
#akasakaakasakasakaakas
#
#出力例 4
#14
#条件を満たす文字列は akasakaakasaka なので、答えは 14 です。

def 