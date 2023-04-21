#問題文
#ロジャーは、彼のもとに突如現れた 1000000000000001 匹の犬をすべて飼うことを決意しました。犬たちにはもともと 1 から 1000000000000001 までの番号がふられていましたが、ロジャーは彼らに以下のルールで名前を授けました。
#1,2,...,26 番の番号がついた犬はその順に a,b,...,z と命名されます。
#27,28,29,...,701,702  番の番号がついた犬はその順に aa,ab,ac,...,zy,zz と命名されます。
#703,704,705,...,18277,18278  番の番号がついた犬はその順に aaa,aab,aac,...,zzy,zzz と命名されます。
#18279,18280,18281,...,475253,475254  番の番号がついた犬はその順に aaaa,aaab,aaac,...,zzzy,zzzz と命名されます。
#475255,475256,...  番の番号がついた犬はその順に aaaaa,aaaab,... と命名されます。
#(以下省略)
#つまり、ロジャーが授けた名前を番号順に並べると:
#a,b,...,z,aa,ab,...,az,ba,bb,...,bz,...,za,zb,...,zz,aaa,aab,...,aaz,aba,abb,...,abz,...,zzz,aaaa,... のようになります。
#ロジャーはあなたに問題を出しました。
#「番号 N の犬の名前を答えよ。」
#
#制約
#N は整数
# 1 ≦ N ≦ 1000000000000001
#
#入力
#入力は以下の形式で標準入力から与えられる。
#N
#
#出力
#ロジャーの問題に対する答えを、英小文字のみからなる文字列として出力せよ。
#
#入力例 1
#2
#
#出力例 1
#b
#
#入力例 2
#27
#
#出力例 2
#aa
#
#入力例 3
#123456789
#
#出力例 3
#jjddja

def 