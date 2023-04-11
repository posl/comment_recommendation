#問題文
#すぬけくんは 6 面サイコロで遊ぶことにしました。
#サイコロは 1 から 6 までの整数がそれぞれの面に書かれており、向かい合う面に書かれた数の和はどれも 7 です。
#すぬけくんはサイコロの好きな面が上向きになるように置いたのち何回か以下の操作を行います。
#操作：サイコロを手前、奥、左、右のどれかの方向に 90° だけ回転させる。その後、上を向いている面に書かれた数を y として y 点得る。
#例えば、図のように 1 と書かれた面が上を向いており、手前側の面に 5 が、右側の面に 4 が書かれている状況を考えます。
#図に示されるように右方向に回転させることで 3 と書かれた面が上を向くようにすることが可能です。
#その他、左方向に回転させた場合は 4 と書かれた面が、手前方向に回転させた場合は 2 と書かれた面が、奥方向に回転させた場合は 5 と書かれた面が上を向くようにすることが可能です。
#
#すぬけくんが合計で x 点以上得るために必要な最小の操作回数を求めなさい。
#
#制約
#1 ≦ x ≦ 10^{15}
#x は整数
#
#入力
#入力は以下の形式で標準入力から与えられる。
#x
#
#出力
#答えを出力せよ。
#
#入力例 1
#7
#
#出力例 1
#2
#
#入力例 2
#149696127901
#
#出力例 2
#27217477801

def 