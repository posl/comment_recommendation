#問題文
#ある街に、N 人のすぬけ君(すぬけ君 1 、すぬけ君 2 、 ...、 すぬけ君 N )が住んでいます。
#この街には、 K 種類のお菓子(お菓子 1 、 お菓子 2 、....、お菓子 K )が売られています。お菓子 i を持っているのは、すぬけ君 A_{i, 1}, A_{i, 2}, ..., A_{i, {d_i}} の計 d_i 人です。
#高橋君は今からこの街を回り、お菓子を 1 つも持っていないすぬけ君にいたずらをします。このとき、何人のすぬけ君がいたずらを受けるでしょうか。
#
#制約
#入力は全て整数
#1 ≦ N ≦ 100
#1 ≦ K ≦ 100
#1 ≦ d_i ≦ N
#1 ≦ A_{i, 1} < ... < A_{i, d_i} ≦ N
#
#入力
#入力は以下の形式で標準入力から与えられる。
#N K
#d_1
#A_{1, 1} ... A_{1, d_1}
#.
#.
#.
#d_K
#A_{K, 1} ... A_{K, d_K}
#
#出力
#答えを出力せよ。
#
#入力例 1
#3 2
#2
#1 3
#1
#3
#
#出力例 1
#1
#
#すぬけ君 1 はお菓子 1 を持っています。
#すぬけ君 2 はお菓子を持っていません。
#すぬけ君 3 はお菓子 1, 2 を持っています。
#以上より、いたずらを受けるのはすぬけ君 2 の一人です。
#
#入力例 2
#3 3
#1
#3
#1
#3
#1
#3
#
#出力例 2
#2

def 