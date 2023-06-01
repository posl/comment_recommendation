Synthesizing 10/10 solutions

=======
Suggestion 1

def rotate(s, t):
    if len(s) != len(t):
        return False
    for i in range(len(s)):
        s = s[-1] + s[0:-1]
        if s == t:
            return True
    return False

=======
Suggestion 2

def solve():
    s = input()
    t = input()
    if len(s) != len(t):
        print("No")
        return
    for i in range(len(s)):
        if s == t:
            print("Yes")
            return
        s = s[-1] + s[:-1]
    print("No")
solve()

=======
Suggestion 3

def rotate(s):
    return s[-1] + s[:-1]

=======
Suggestion 4

def main():
    S = input()
    T = input()
    if len(S) != len(T):
        print("No")
        return
    for i in range(len(S)):
        if S == T:
            print("Yes")
            return
        S = S[-1] + S[0:-1]
    print("No")

=======
Suggestion 5

def main():
    s = input()
    t = input()
    for i in range(len(s)):
        if s == t:
            print("Yes")
            return
        s = s[1:] + s[0]
    print("No")

=======
Suggestion 6

def main():
    S = input()
    T = input()
    for i in range(len(S)):
        if S == T:
            print("Yes")
            break
        else:
            S = S[-1] + S[:-1]
    else:
        print("No")

=======
Suggestion 7

def check(s, t):
    if len(s) != len(t):
        return False
    for i in range(len(s)):
        s = s[-1] + s[0:-1]
        if s == t:
            return True
    return False

s = input()
t = input()

=======
Suggestion 8

def main():
    s = input()
    t = input()
    if len(s) != len(t):
        print('No')
        return
    for i in range(len(s)):
        if s == t:
            print('Yes')
            return
        s = s[1:] + s[0]
    print('No')

=======
Suggestion 9

def main():
    s = input()
    t = input()
    if s == t:
        print("Yes")
    else:
        print("No")

=======
Suggestion 10

def main():
    s = input()
    t = input()
    if len(s) != len(t):
        print('No')
        return
    for i in range(len(s)):
        if s == t:
            print('Yes')
            return
        else:
            s = s[-1] + s[:-1]
    print('No')
