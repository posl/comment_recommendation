#問題文
#いろはちゃんは、人気の日本製ゲーム「ÅtCoder」で遊びたい猫のすぬけ君のために日本語を教えることにしました。
#日本語で鉛筆を数えるときには、助数詞として数の後ろに「本」がつきます。この助数詞はどんな数につくかで異なる読み方をします。具体的には、999 以下の正の整数 N について、「N 本」と言うときの「本」の読みは
#N の 1 の位が 2, 4, 5, 7, 9 のとき hon
#N の 1 の位が 0, 1, 6, 8 のとき pon
#N の 1 の位が 3 のとき bon
#です。
#N が与えられるので、「N 本」と言うときの「本」の読みを出力してください。
#
#制約
#N は 999 以下の正の整数
#
#入力
#入力は以下の形式で標準入力から与えられる。
#N
#
#出力
#答えを出力せよ。
#
#入力例 1
#16
#
#出力例 1
#pon
#16 の 1 の位は 6 なので、「本」の読みは pon です。
#
#入力例 2
#2
#
#出力例 2
#hon
#
#入力例 3
#183
#
#出力例 3
#bon

def 