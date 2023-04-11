#問題文
#駅の待合室に座っているjoisinoお姉ちゃんは、切符を眺めています。
#切符には 4 つの 0 以上 9 以下の整数 A,B,C,D が整理番号としてこの順に書かれています。
#A op1 B op2 C op3 D = 7 となるように、op1,op2,op3 に + か - を入れて式を作って下さい。
#なお、答えが存在しない入力は与えられず、また答えが複数存在する場合はどれを出力してもよいものとします。
#
#制約
#0≦A,B,C,D≦9
#入力は整数からなる
#答えが存在しない入力は与えられない
#
#入力
#入力は以下の形式で標準入力から与えられる。
#ABCD
#
#出力
#作った式を、=7 の部分を含めて出力せよ。
#ただし、記号は半角で出力せよ。
#また、数字と記号の間に空白を入れてはならない。
#
#入力例 1
#1222
#
#出力例 1
#1+2+2+2=7
#1 + 2 + 2 + 2 = 7 が条件を満たします。
#
#入力例 2
#0290
#
#出力例 2
#0-2+9+0=7
#この他に、0 - 2 + 9 - 0 = 7 が条件を満たします。
#
#入力例 3
#3242
#
#出力例 3
#3+2+4-2=7

def 