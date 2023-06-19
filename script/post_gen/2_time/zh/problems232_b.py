Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    S = input()
    T = input()
    if S == T:
        print("Yes")
    else:
        print("No")

=======
Suggestion 2

def solve():
    s = raw_input()
    t = raw_input()
    if len(s) != len(t):
        return False
    for i in range(len(s)):
        if s == t:
            return True
        s = s[-1] + s[:-1]
    return False

=======
Suggestion 3

def main():
    S = input()
    T = input()
    for i in range(26):
        s = ""
        for j in range(len(S)):
            s += chr((ord(S[j]) - ord("a") + i) % 26 + ord("a"))
        if s == T:
            print("Yes")
            exit()
    print("No")

=======
Suggestion 4

def main():
    S = input()
    T = input()
    if len(S) == len(T):
        for i in range(len(S)):
            if S[i] != T[i]:
                if (ord(S[i]) + 1) % 97 == ord(T[i]) % 97:
                    pass
                else:
                    print("No")
                    exit()
        print("Yes")
    else:
        print("No")

main()

=======
Suggestion 5

def main():
    S = input()
    T = input()
    if len(S) != len(T):
        print("No")
    else:
        for i in range(len(S)):
            if ord(S[i]) != ord(T[i]) and (ord(S[i]) + 1) != ord(T[i]):
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
        print('No')
        return
    for i in range(len(s)):
        if s[i] != t[i]:
            print('No')
            return
    print('Yes')

=======
Suggestion 7

def move(s, k):
    l = len(s)
    ret = ''
    for i in range(l):
        ret += chr((ord(s[i]) - ord('a') + k) % 26 + ord('a'))
    return ret

=======
Suggestion 8

def main():
    s = input()
    t = input()
    if len(s) != len(t):
        print("No")
        return
    for i in range(len(s)):
        if s[i] != t[i]:
            print("No")
            return
    print("Yes")
    return

=======
Suggestion 9

def fun():
    s = input()
    t = input()
    if len(s) != len(t):
        print("No")
        return
    for i in range(len(s)):
        if ord(s[i]) - ord(t[i]) >= 0:
            if ord(s[i]) - ord(t[i]) > 1:
                print("No")
                return
        else:
            if ord(s[i]) - ord(t[i]) < -1:
                print("No")
                return
    print("Yes")
    return

=======
Suggestion 10

def main():
    s = input()
    t = input()

    if (s == t):
        print("Yes")
        return
    else:
        for i in range(1, len(s)):
            if (s[i:] + s[:i] == t):
                print("Yes")
                return

    print("No")
