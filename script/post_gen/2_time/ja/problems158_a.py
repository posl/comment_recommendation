Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    S = input()
    if S[0] == S[1] or S[1] == S[2] or S[0] == S[2]:
        print("No")
    else:
        print("Yes")

=======
Suggestion 2

def main():
    S = input()
    if S[0] == S[1]:
        print("No")
    elif S[1] == S[2]:
        print("No")
    else:
        print("Yes")

=======
Suggestion 3

def main():
    s = input()
    if s[0] == s[1] or s[1] == s[2]:
        print("No")
    else:
        print("Yes")

=======
Suggestion 4

def main():
    s = input()
    if s[0] == s[1] and s[1] == s[2]:
        print('No')
    else:
        print('Yes')

=======
Suggestion 5

def main():
    s = input()
    if s[0] == s[1] or s[1] == s[2]:
        print('No')
    else:
        print('Yes')

=======
Suggestion 6

def main():
    s = input()
    print("Yes" if s[0] != s[1] or s[1] != s[2] or s[0] != s[2] else "No")

=======
Suggestion 7

def main():
    S = input()

    if S == "AAA" or S == "BBB":
        print("No")
    else:
        print("Yes")

=======
Suggestion 8

def main():
    # 入力
    S = input()
    # 出力
    if S[0] == S[1]:
        print("No")
    elif S[1] == S[2]:
        print("No")
    elif S[2] == S[0]:
        print("No")
    else:
        print("Yes")

=======
Suggestion 9

def main():
    # 標準入力から文字列を取得
    s = input()
    # s[0]とs[1]の文字が同じかどうか
    if s[0] == s[1]:
        # s[1]とs[2]の文字が同じかどうか
        if s[1] == s[2]:
            # s[0]とs[1]とs[2]の文字が全て同じなのでNoを出力
            print('No')
        else:
            # s[0]とs[1]の文字が同じで、s[1]とs[2]の文字が違うなのでYesを出力
            print('Yes')
    else:
        # s[0]とs[1]の文字が違うかつ、s[1]とs[2]の文字が同じなのでYesを出力
        print('Yes')
