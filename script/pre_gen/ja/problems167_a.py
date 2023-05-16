#問題文
#高橋君はとあるWebサービスに会員登録しようとしています。
#まずIDを S として登録しようとしました。しかし、このIDは既に他のユーザーによって使用されていました。
#そこで、高橋君は S の末尾に 1 文字追加した文字列をIDとして登録することを考えました。
#高橋君は新しくIDを T として登録しようとしています。これが前述の条件を満たすか判定してください。
#
#制約
#S, T は英小文字列
#1 ≦ |S| ≦ 10
#|T| = |S| + 1
#
#入力
#入力は以下の形式で標準入力から与えられる。
#S
#T
#
#出力
#T が問の条件を満たすならば Yes と、そうでないならば No と出力せよ。
#
#入力例 1
#chokudai
#chokudaiz
#
#出力例 1
#Yes
#chokudaiz は chokudai の末尾に z を追加して得られる文字列です。
#
#入力例 2
#snuke
#snekee
#
#出力例 2
#No
#snekee は snuke の末尾に英小文字を 1 文字追加して得られる文字列ではありません。
#
#入力例 3
#a
#aa
#
#出力例 3
#Yes

def 