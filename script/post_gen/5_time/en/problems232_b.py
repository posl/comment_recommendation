Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    s = input()
    t = input()
    if len(s) != len(t):
        print("No")
    else:
        for i in range(len(s)):
            if s[i:] + s[:i] == t:
                print("Yes")
                return
        print("No")
    return

=======
Suggestion 2

def main():
    S = input()
    T = input()
    if S == T:
        print("Yes")
        return
    for i in range(len(S)):
        if S[i:] + S[:i] == T:
            print("Yes")
            return
    print("No")

=======
Suggestion 3

def main():
    s = input()
    t = input()
    for i in range(len(s)):
        if s[i] != t[i]:
            print("No")
            return
    print("Yes")

=======
Suggestion 4

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
Suggestion 5

def solve():
    s = input()
    t = input()
    for i in range(len(s)):
        if s == t:
            print("Yes")
            return
        s = s[-1] + s[0:-1]
    print("No")

=======
Suggestion 6

def main():
    S = input()
    T = input()
    if S == T:
        print('Yes')
    else:
        for i in range(1, len(S)):
            if S[i:] + S[:i] == T:
                print('Yes')
                break
        else:
            print('No')

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
        print('Yes')
    else:
        print('No')

=======
Suggestion 9

def solve(s, t):
    for i in range(len(s)):
        if s[i:] + s[:i] == t:
            return True
    return False

=======
Suggestion 10

def solve():
    #import sys
    #input = sys.stdin.readline
    s = input()
    t = input()
    if s == t:
        print("Yes")
    else:
        print("No")
    return 0
