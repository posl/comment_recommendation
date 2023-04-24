Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    S = input()
    T = input()
    for i in range(len(S)):
        S = S[-1] + S[:-1]
        if S == T:
            print("Yes")
            return
    print("No")

=======
Suggestion 2

def main():
    S = input()
    T = input()
    for i in range(len(S)):
        S = S[1:] + S[0]
        if S == T:
            print('Yes')
            return
    print('No')

=======
Suggestion 3

def main():
    S = input()
    T = input()
    if S == T:
        print("Yes")
    else:
        for i in range(len(S)):
            S = S[-1] + S[:-1]
            if S == T:
                print("Yes")
                break
        else:
            print("No")

=======
Suggestion 4

def main():
    S = input()
    T = input()
    if S == T:
        print("Yes")
    else:
        for i in range(1, len(S)):
            if S[i:] + S[:i] == T:
                print("Yes")
                break
        else:
            print("No")

=======
Suggestion 5

def main():
    S = input()
    T = input()
    if S == T:
        print("Yes")
    else:
        for i in range(1, len(S)):
            if S[i:] + S[:i] == T:
                print("Yes")
                return
        print("No")

main()

=======
Suggestion 6

def main():
    s = input()
    t = input()
    if s == t:
        print("Yes")
        return
    for i in range(len(s)-1):
        s = s[-1] + s[:len(s)-1]
        if s == t:
            print("Yes")
            return
    print("No")

=======
Suggestion 7

def main():
    s = input()
    t = input()
    if s == t:
        print("Yes")
    else:
        for i in range(len(s)-1):
            s = s[len(s)-1] + s[:len(s)-1]
            if s == t:
                print("Yes")
                return
        print("No")
        return

=======
Suggestion 8

def main():
    S = input()
    T = input()
    if S == T:
        print("Yes")
        return
    for i in range(len(S)):
        S = S[-1] + S[:len(S)-1]
        if S == T:
            print("Yes")
            return
    print("No")

=======
Suggestion 9

def rotate(s):
    return s[-1] + s[0:-1]

=======
Suggestion 10

def is_match(s, t):
    # s = s[1:] + s[0] とすると、s の先頭の文字が末尾に移動する
    # この操作を繰り返して s が t に一致するかどうかを判定する
    for _ in range(len(s)):
        if s == t:
            return True

        s = s[1:] + s[0]

    return False
