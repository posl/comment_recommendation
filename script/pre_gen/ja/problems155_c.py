#問題文
#N 枚の投票用紙があり、i (1 ≦ i ≦ N) 枚目には文字列 S_i が書かれています。
#書かれた回数が最も多い文字列を全て、辞書順で小さい順に出力してください。
#
#制約
#1 ≦ N ≦ 2 × 10^5
#S_i は英小文字のみからなる文字列 (1 ≦ i ≦ N)
#S_i の長さは 1 以上 10 以下 (1 ≦ i ≦ N)
#
#入力
#入力は以下の形式で標準入力から与えられる。
#N
#S_1
#:
#S_N
#
#出力
#あてはまる文字列を全て辞書順で小さい順に、改行区切りで出力せよ。
#
#入力例 1
#7
#beat
#vet
#beet
#bed
#vet
#bet
#beet
#
#出力例 1
#beet
#vet
#書かれた回数は beet と vet が 2 回、beat と bed と bet が 1 回です。したがって、2 回書かれた beet と vet を出力します。
#
#入力例 2
#8
#buffalo
#buffalo
#buffalo
#buffalo
#buffalo
#buffalo
#buffalo
#buffalo
#
#出力例 2
#buffalo
#
#入力例 3
#7
#bass
#bass
#kick
#kick
#bass
#kick
#kick
#
#出力例 3
#kick
#
#入力例 4
#4
#ushi
#tapu
#nichia
#kun
#
#出力例 4
#kun
#nichia
#tapu
#ushi

def 