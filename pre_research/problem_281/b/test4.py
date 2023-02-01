#問題文
#英大文字と数字からなる文字列 S が与えられるので、S が以下の条件を満たすか判定してください。
#S は次の文字または文字列をこの順番で連結して得られる。
#一文字の英大文字
#100000 以上 999999 以下の整数を 10 進表記して得られる長さ 6 の文字列
#一文字の英大文字
#
#制約
#S は英大文字と数字からなる
#S の長さは 1 以上 10 以下
#
#入力
#入力は以下の形式で標準入力から与えられる。
#S
#
#出力
#S が問題文中の条件を満たすなら Yes と、満たさないなら No と出力せよ。
#
#入力例 1
#Q142857Z
#
#出力例 1
#Yes
#
#入力例 2
#AB912278C
#
#出力例 2
#No
#
#入力例 3
#X900000
#
#出力例 3
#No
#
#入力例 4
#K012345K
#
#出力例 4
#No

def main():
    S = input()
    ans = "Yes"
    if S[0] not in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        ans = "No"
    if S[-1] not in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        ans = "No"
    if S[1:-1].isdigit() == False:
        ans = "No"
    if len(S[1:-1]) != 6:
        ans = "No"
    if int(S[1:-1]) < 100000 or int(S[1:-1]) > 999999:
        ans = "No"
    print(ans)

if __name__ == '__main__':
    main()