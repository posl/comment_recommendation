#問題文
#N 人の人が東西方向に一列に並んでいます。
#それぞれの人は、東または西を向いています。
#誰がどの方向を向いているかは長さ N の文字列 S によって与えられます。
#西から i 番目に並んでいる人は、S_i = E なら東を、S_i = W なら西を向いています。
#あなたは、N 人のうち誰か 1 人をリーダーとして任命します。
#そして、リーダー以外の全員に、リーダーの方向を向くように命令します。
#このとき、リーダーはどちらの方向を向いていても構いません。
#並んでいる人は、向く方向を変えるのを嫌っています。
#そのためあなたは、向く方向を変える人数が最小になるようにリーダーを選びたいです。
#向く方向を変える人数の最小値を求めてください。
#
#制約
#2 ≦ N ≦ 3 × 10^5
#|S| = N
#S_i は E または W である
#
#入力
#入力は以下の形式で標準入力から与えられる。
#N
#S
#
#出力
#向く方向を変える人数の最小値を出力せよ。
#
#入力例 1
#5
#WEEWW
#
#出力例 1
#1
#西から 3 番目に並んでいる人をリーダーに任命するとします。
#すると、西から 1 番目に並んでいる人は東を向かなくてはならないので、向く方向を変える必要があります。
#ほかの人は向く方向を変える必要がないので、この場合、向く方向を変える人は 1 人になります。
#向く方向を変える人を 0 人にすることは出来ないので、答えは 1 になります。
#
#入力例 2
#12
#WEWEWEEEWWWE
#
#出力例 2
#4
#
#入力例 3
#8
#WWWWWEEE
#
#出力例 3
#3

def 