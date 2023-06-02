Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    S = input()
    T = input()
    if S in T*2:
        print('Yes')
    else:
        print('No')

=======
Suggestion 2

def main():
    s = input()
    t = input()
    if s == t:
        print("Yes")
        return
    for i in range(1, len(s)):
        if s[i:] + s[:i] == t:
            print("Yes")
            return
    print("No")

=======
Suggestion 3

def main():
    S = input()
    T = input()
    if len(S) == len(T):
        if T in S + S:
            print("Yes")
        else:
            print("No")

=======
Suggestion 4

def main():
    s = input()
    t = input()
    if len(s) != len(t):
        return print("No")
    else:
        for i in range(len(s)):
            s = s[-1] + s[:-1]
            if s == t:
                return print("Yes")
        return print("No")

=======
Suggestion 5

def is_equal(s, t):
    if len(s) != len(t):
        return False
    if s == t:
        return True
    for i in range(len(s)):
        s = s[1:] + s[0]
        if s == t:
            return True
    return False

=======
Suggestion 6

def rotateString(s, t):
    if len(s) != len(t):
        return False
    if s == t:
        return True
    for i in range(1, len(s)):
        if s[i:] + s[:i] == t:
            return True
    return False

=======
Suggestion 7

def main():
    S = input()
    T = input()
    if len(S) != len(T):
        print("No")
        return
    for i in range(len(S)):
        S = S[1:] + S[0]
        if S == T:
            print("Yes")
            return
    print("No")

=======
Suggestion 8

def main():
    s = input()
    t = input()
    if s in t+t:
        print('Yes')
    else:
        print('No')

=======
Suggestion 9

def rotate(s):
    return s[-1] + s[:-1]

=======
Suggestion 10

def is_equal(s1, s2):
    if s1 == s2:
        return True
    else:
        return False
