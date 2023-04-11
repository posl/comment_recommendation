#問題文
#すぬけ君はビーカーに砂糖水を作ろうとしています。
#最初ビーカーは空です。すぬけ君は以下の 4 種類の操作をそれぞれ何回でも行うことができます。一度も行わない操作があっても構いません。
#操作 1: ビーカーに水を 100A [g] 入れる。
#操作 2: ビーカーに水を 100B [g] 入れる。
#操作 3: ビーカーに砂糖を C [g] 入れる。
#操作 4: ビーカーに砂糖を D [g] 入れる。
#すぬけ君の実験環境下では、水 100 [g] あたり砂糖は E [g] 溶けます。
#すぬけ君はできるだけ濃度の高い砂糖水を作りたいと考えています。
#ビーカーに入れられる物質の質量 (水の質量と砂糖の質量の合計) が F [g] 以下であり、
#ビーカーの中に砂糖を溶け残らせてはいけないとき、
#すぬけ君が作る砂糖水の質量と、それに溶けている砂糖の質量を求めてください。
#答えが複数ある場合はどれを答えても構いません。
#水 a [g] と砂糖 b [g] を混ぜた砂糖水の濃度は ((100b)/(a + b)) [%]です。
#また、この問題では、砂糖が全く溶けていない水も濃度 0 [%] の砂糖水と考えることにします。
#
#制約
#1 ≦ A < B ≦ 30
#1 ≦ C < D ≦ 30
#1≦ E ≦ 100
#100A ≦ F ≦ 3,000
#A, B, C, D, E, F はすべて整数である。
#
#入力
#入力は以下の形式で標準入力から与えられる。
#A B C D E F
#
#出力
#整数を空白区切りで 2 つ出力せよ。
#1 つ目は求める砂糖水の質量、2 つ目はそれに溶けている砂糖の質量とせよ。
#
#入力例 1
#1 2 10 20 15 200
#
#出力例 1
#110 10
#この入力例の状況では、水 100 [g] あたり砂糖は 15 [g] 溶けます。
#また、ビーカーに物質を 200 [g] まで入れることができます。
#操作 1 と操作 3 を 1 回ずつ行うことで 110 [g] の砂糖水を作ることができます。
#また、これ以上濃度の高い砂糖水を作ることはできません。
#たとえば、以下のような操作は条件を満たしません。
#操作 1 と操作 4 を 1 回ずつ行うと、ビーカーに砂糖が溶け残ってしまいます。
#操作 2 を 1 回と操作 3 を 3 回行うと、ビーカーの中の物質の量が 200 [g] を超えてしまいます。
#
#入力例 2
#1 2 1 2 100 1000
#
#出力例 2
#200 100
#ほかに、たとえば以下の出力
#も正解となります。
#400 200
#一方、以下の出力は不正解となります。
#300 150
#なぜなら、砂糖が 150 [g] 溶けた 300 [g] の砂糖水を作るにはビーカーに水をちょうど 150 [g] 入れる必要がありますが、そのようなことは不可能だからです。
#
#入力例 3
#17 19 22 26 55 2802
#
#出力例 3
#2634 934

def 