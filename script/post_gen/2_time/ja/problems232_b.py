Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    s = input()
    t = input()
    for i in range(len(s)):
        if s == t:
            print("Yes")
            return
        s = s[-1] + s[:-1]
    print("No")

=======
Suggestion 2

def main():
    s = input()
    t = input()
    for i in range(len(s)):
        if s[i] != t[i]:
            print("No")
            return
    print("Yes")

=======
Suggestion 3

def main():
    s = input()
    t = input()
    flag = False
    for i in range(len(s)):
        if s[i:] + s[:i] == t:
            flag = True
            break
    if flag:
        print('Yes')
    else:
        print('No')

=======
Suggestion 4

def main():
    s = input()
    t = input()
    for i in range(len(s)):
        if s[i] != t[i]:
            print('No')
            return
    print('Yes')

=======
Suggestion 5

def main():
    s = input()
    t = input()
    for i in range(len(s)):
        if s[i] != t[i]:
            print("No")
            break
    else:
        print("Yes")

=======
Suggestion 6

def main():
    s = input()
    t = input()
    if len(s) != len(t):
        print("No")
        return
    else:
        for i in range(len(s)):
            if s[i] != t[i]:
                if ord(s[i]) + 1 == ord(t[i]):
                    continue
                elif ord(s[i]) + 1 == ord("z") and ord(t[i]) == ord("a"):
                    continue
                else:
                    print("No")
                    return
        print("Yes")

=======
Suggestion 7

def main():
    s = input()
    t = input()
    if s == t:
        print("Yes")
    else:
        print("No")

=======
Suggestion 8

def main():
    s = input()
    t = input()
    if s == t:
        print("Yes")
        return

    for i in range(len(s)):
        if s[i:] + s[:i] == t:
            print("Yes")
            return

    print("No")

main()

=======
Suggestion 9

def main():

    s = input()
    t = input()

    if len(s) != len(t):
        print("No")
        exit()

    for i in range(len(s)):
        if s[i] != t[i]:
            print("No")
            exit()

    print("Yes")

main()

=======
Suggestion 10

def solve():
    # === 入力 ===
    # S
    S = input()
    # T
    T = input()

    # === 処理 ===
    # S と T の長さは等しい
    # S の長さと T の長さは等しい
    # なので、S の長さでループさせる
    for i in range(len(S)):
        # S の i 番目の文字
        s = S[i]
        # T の i 番目の文字
        t = T[i]
        # S の i 番目の文字と T の i 番目の文字が異なる場合
        if s != t:
            # No を出力して終了
            print("No")
            return
    # S と T が一致する場合
    # Yes を出力
    print("Yes")
