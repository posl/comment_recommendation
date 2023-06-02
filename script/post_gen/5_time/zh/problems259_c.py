Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    S = input()
    T = input()
    if S == T:
        print("Yes")
        return
    if len(S) < len(T):
        print("No")
        return
    if len(S) == len(T):
        print("Yes")
        return
    #S长度大于T
    #S中是否存在T的子串
    if T in S:
        print(

=======
Suggestion 2

def main():
    s = input()
    t = input()
    if len(s) == len(t):
        for i in range(len(s) - 1):
            if s[i] == s[i + 1]:
                s = s[:i + 1] + s[i] + s[i + 1:]
                break
        if s == t:
            print("Yes")
        else:
            print("No")
    else:
        print("No")

=======
Suggestion 3

def main():
    S = input()
    T = input()
    if len(S) + 1 == len(T):
        if S == T[:-1]:
            print("Yes")
        else:
            print("No")
    else:
        print("No")

=======
Suggestion 4

def main():
    S = input()
    T = input()
    S_len = len(S)
    T_len = len(T)
    if S_len >= 2 and S_len <= 2*10**5 and T_len >= 2 and T_len <= 2*10**5:
        if S == T:
            print("Yes")
        else:
            for i in range(S_len-1):
                if S[i] == S[i+1]:
                    S = S[0:i+1] + S[i] + S[i+1:]
                    if S == T:
                        print("Yes")
                        break
                    else:
                        print("No")
    else:
        print("No")

=======
Suggestion 5

def main():
    s = input()
    t = input()

    if len(s) + 1 != len(t):
        print("No")
        return

    for i in range(len(s)):
        if s[i] != t[i]:
            print("No")
            return

    print("Yes")

=======
Suggestion 6

def main():
    S = input()
    T = input()
    if S == T[:-1]:
        print("Yes")
    else:
        print("No")

=======
Suggestion 7

def is_subsequence(s, t):
    t = iter(t)
    return all(c in t for c in s)

s = input()
t = input()

=======
Suggestion 8

def solve():
    s = input()
    t = input()
    while len(s) < len(t):
        if s[-1] == t[len(s)-1]:
            s += s[-1]
        else:
            print("No")
            return
    if s == t:
        print("Yes")
    else:
        print("No")

=======
Suggestion 9

def main():
    s = input()
    t = input()
    if len(s) + 1 == len(t):
        for i in range(len(s)):
            if s[i] != t[i]:
                print("No")
                return
        print("Yes")
    else:
        print("No")
