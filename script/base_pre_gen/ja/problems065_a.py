#問題文
#高橋君は胃が強いので、賞味期限を X 日まで過ぎた食品を食べてもお腹を壊しません。
#賞味期限を X+1 日以上過ぎた食品を食べると、お腹を壊します。
#また、賞味期限を過ぎずに食べると、おいしく感じます。そうでない場合、おいしく感じません。
#高橋君は、賞味期限の A 日前に食品を買ってきて、買ってから B 日後に食べました。
#高橋君が食品をおいしく感じた場合 delicious を、おいしくは感じなかったがお腹は壊さなかった場合 safe を、お腹を壊した場合 dangerous を出力するプログラムを作成してください。
#
#制約
#1 ≦ X,A,B ≦ 10^9
#
#入力
#入力は以下の形式で標準入力から与えられる。
#X A B
#
#出力
#高橋君が食品をおいしく感じた場合 delicious を、おいしくは感じなかったがお腹は壊さなかった場合 safe を、お腹を壊した場合 dangerous を出力せよ。
#
#入力例 1
#4 3 6
#
#出力例 1
#safe
#賞味期限を 3 日過ぎて食べるので、おいしくは感じませんが、お腹も壊しません。
#
#入力例 2
#6 5 1
#
#出力例 2
#delicious
#賞味期限を過ぎていないので、おいしく感じます。
#
#入力例 3
#3 7 12
#
#出力例 3
#dangerous
#賞味期限を 5 日過ぎて食べるので、お腹を壊します。

def 